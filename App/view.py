import text
from datetime import datetime, date, time


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_notes(notes: list[dict[str, str]], error: str):
    if notes:
        print('=' * 71)
        for i, note in enumerate(notes, 1):
            print(
                f'{i:>3} | {note.get("datetime"):<20} | {note.get("title"):<20} | {note.get("note"):<20}')
            if i == notes.__len__():
                print('=' * 71)
            else:
                print('-' * 71)
    else:
        print_message(error)


def input_notes(new_id: int, message: str, cancel: str) -> dict[str, str]:
    note = {}
    print(message)
    note['id'] = str(new_id)
    note['datetime'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for key, value in text.new_notes.items():
        data = input(value)
        match key:
            case 'title':
                if data:
                    note[key] = data
                else:
                    print_message(cancel)
            case 'note':
                if data:
                    note[key] = data
                else:
                    note[key] = ''
    return note


def input_index(message: str, notes: list, error: str) -> int:
    print_notes(notes, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(notes) + 1:
            return int(index)


def input_search(message: str) -> str:
    return input(message)