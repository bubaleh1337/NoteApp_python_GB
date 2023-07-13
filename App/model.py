from contextlib import suppress

notes_list: list[dict[str, str]] = []
path = 'notes.txt'

def open_notes_list():
	global notes_list, path
	with open(path, 'r', encoding='UTF-8') as file:
		data = file.readlines() # 'Kate:7444654:comment'
	for note in data:
		note = note.strip().split(':') # .strip() - очищение начало и конец строки
		notes_list.append({'title': note[0], 'note': note[1], 'comment': note[2]})

def save_notes_list():
	global notes_list, path
	data = []
	for note in notes_list:
		data.append(':'.join([value for value in note.values()]))
	with open(path, 'w', encoding='UTF-8') as file:
		file.write('\n'.join(data))

def get_notes_list() -> list[dict[str, str]]:
	global notes_list
	return notes_list

def add_note(note: dict[str, str]):
	global notes_list
	notes_list.append(note)
	return note.get('title')

def del_note(index: int): 
	global notes_list
	return notes_list.pop(index-1).get('title') 

def search_notes_list(word: str) -> list[dict[str, str]]:
	result: list[dict[str, str]] = []
	for note in notes_list:
		for field in note.values():
			if word.lower().strip() in field.lower().strip():
				result.append(note)
				break
	return result

def change_notes_list(note: dict, index: int):
	global notes_list
	
	with suppress(Exception):
		if len(note['title']) > 0:
			notes_list[index-1]['title'] = note['title']
	with suppress(Exception):
		if len(note['note']) > 0:
			notes_list[index-1]['note'] = note['note']
