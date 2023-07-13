from datetime import datetime
import text

def main_menu() -> int: # печать меню и проверка на число от пользователя
	print(text.main_menu)
	while True:
		choice = input(text.input_choice) 
		if choice.isdigit() and 0 < int(choice) < 9: 
			return int(choice)

def print_message(message: str): # печать любого сообщения 
	print('\n' + '=' * len(message)) 
	print(message)
	print('=' * len(message) + '\n')

def print_notes(notes_list: list[dict[str, str]], error: str): # печать списка заметок 
	if notes_list:
		print('\n' + '=' * len(notes_list))
		for i, note in enumerate(notes_list, 1):
			print(f'{i:>3}. {note.get("title")}\t | \t{note.get("date")}\n\n {note.get("note"):<20}')
			print('=' * len(notes_list) + '\n')
	else:
			print_message(error)		

def input_note(message: str, cancel: str) -> dict[str, str]: # введение заметки
	note = {}
	print(message)
	for key, value in text.new_note.items():
		
		if (key == "date"): 
			note[value] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			continue
		else:
			data = input(value)
			if data:
				note[key] = data
			else:
				print_message(cancel)
	return note

def input_index(message: str, notes_list: list, error: str) -> int: # индексация
	print_notes(notes_list, error)
	while True:
		index = input(message)
		if index.isdigit() and 0 < int(index) < len(notes_list) + 1:
			return int(index)

def input_search(message: str) -> str: # поиск
	return input(message)