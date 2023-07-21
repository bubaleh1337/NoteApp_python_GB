from contextlib import suppress
from datetime import datetime
from json import load
from time import time
from Notes import Notes
from os import mkdir

class Model:
	__notes_list: list[dict[str, str]] = []
	__path = 'notes.txt'

	def open_notes_list(self):
		with open(self.__path, "r", encoding='UTF-8') as file:
			data = file.readlines()
			for note in data:
				note = note.strip().split(':')
				self.__notes_list.append({'title': note[0], 'date': note[1], 'note': note[2]})
		return self.__notes_list
# 'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	def save_notes_list(self):
		data = []
		for note in self.__notes_list:
			data.append(':'.join([value for value in note.values()]))
		with open(self.__path, 'w', encoding='UTF-8') as file:
			file.write('\n'.join(data))

	def get_notes_list(self) -> list[dict[str, str]]:
		return self.__notes_list

	def add_new_note(self, head: str, text: str):
		created_timestamp: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		note: Notes = Notes(created_timestamp, head, text)
		self.__notes_list.append({'title':note.get_head(), 'date':note.get_created_timestamp(), 'note':note.get_text()})
		return note.get_head

	def add_note(self, note: dict[str, str]):
		self.__notes_list.append(note)
		return note.get('title')
	
	def del_note(self, index: int):
		return self.__notes_list.pop(index-1).get('title') 

	def search_notes_list(self, word: str) -> list[dict[str, str]]:
		result: list[dict[str, str]] = []
		for note in self.__notes_list:
			for field in note.values():
				if word.lower().strip() in field.lower().strip():
					result.append(note)
					break
		return result

	def change_notes_list(self, note: dict, index: int):
		
		with suppress(Exception):
			if len(note['title']) > 0:
				self.__notes_list[index-1]['title'] = note['title']
		with suppress(Exception):
			if len(note['date']) > 0:
				self.__notes_list[index-1]['date'] = note['date']			
		with suppress(Exception):
			if len(note['note']) > 0:
				self.__notes_list[index-1]['note'] = note['note']
		return note.get('title')
