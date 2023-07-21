from datetime import datetime
from time import time
import text
from model import Notes
class View:

	@staticmethod
	def sort_by_create_date(note: Notes):
		return note.get_created_timestamp
	@staticmethod
	def sort_by_last_change_timestamp(note: Notes):
		return note.get_last_change_timestamp

	def main_menu(self) -> int: # печать меню и проверка на число от пользователя
		print(text.main_menu)
		while True:
			choice = input(text.input_choice) 
			if choice.isdigit() and 0 < int(choice) < 9: 
				return int(choice)

	def print_message(self, message: str): # печать любого сообщения 
		print('\n' + '=' * len(message)) 
		print(message)
		print('=' * len(message) + '\n')

	def print_notes(self, notes_list: list[dict[str, str]], error: str): # печать списка заметок 
		if notes_list:
			print('\n' + '=' * 71)
			for i, note in enumerate(notes_list, 1):
				print(f'{i:>3}. {note.get("title")}\t | \t{note.get("date")}\n\n {note.get("note"):<20}')
				print('=' * 71 + '\n')
		else:
				self.print_message(error)		

	def input_note(self, cancel: str): # введение заметки
		note = ""
		for value in text.new_note.items():
			data = input(value)
			if data:
				note = data
			else:
				self.print_message(cancel)
		return note

	def input_content(self, message: str) -> str:
		return input(message)

	def input_index(self, notes_list: list, message: str, error: str) -> int: # индексация
		self.print_notes(notes_list, error)
		while True:
			index = input(message)
			if index.isdigit() and 0 < int(index) < len(notes_list) + 1:
				return int(index)

	def input_search(self, message: str) -> str: # поиск
		self.print_message(message)
		return input(message)
	
	def input_num(self, msg: str) -> str:
		self.print_message(msg)
		while True:
			num = input(msg)
			if num == "1" or num == "2":
				return input(num)