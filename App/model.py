from contextlib import suppress


class Notes:

    def __init__(self, path: str = ''):
        self._notes: list[dict[str, str]] = []
        self._path = path

    def load_notes(self):
        with suppress(Exception):
          with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for note in data:
              note = note.strip().split(';')
              self._notes.append({'id': note[0], 'datetime': note[1], 'title': note[2], 'note': note[3]})

    def save_notes(self):
        data = []
        for note in self._notes:
            data.append(';'.join([value for value in note.values()]))
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    def get_notes(self) -> list[dict[str, str]]:
        return self._notes

    def get_max_id(self) -> int:
        if self._notes:
            max_id = max(int(value['id']) for value in self._notes)+1
        else:
            max_id = 1
        return max_id

    def add_note(self, note: dict[str, str]):
        self._notes.append(note)
        return note.get('title')

    def del_note(self, index: int):
        return self._notes.pop(index-1).get('title')

    def search_notes(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for note in self._notes:
            for field in note.values():
                if word.lower().strip() in field.lower().strip():
                    result.append(note)
                    break
        return result

    def change_notes(self, note: dict[str, str], index: int):
      with suppress(Exception):
        if len(note['title']) > 0:
            self._notes[index-1]['title'] = note['title']
      with suppress(Exception):
        if len(note['note']) > 0:
            self._notes[index-1]['note'] = note['note']
      with suppress(Exception):
        self._notes[index-1]['datetime'] = note['datetime']