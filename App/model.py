from contextlib import suppress
from datetime import datetime
from json import dump, load
from time import time
from Notes import Notes
from os import mkdir

class Model:
	__notes_list: list[dict] = []
	__path = 'notes.txt'

	def __init__(self):
		self.__cache: dict[int, Notes] = {}

	def open_notes_list(self):
		with open(self.__path, "r", encoding='UTF-8') as file:
			data = file.readlines()
			for note in data:
				note = note.strip().split(':')
				self.__notes_list.append({'id':note[0], 'title': note[1], 'date': note[2], 'note': note[3]})
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

	def get_max_id(self) -> int:
		if self.__notes_list:
			max_id = max(int(value['id']) for value in self.__notes_list)+1
		else:
			max_id = 1
		return max_id
	
	def add_new_note(self, head: str, text: str):
		id: int = self.get_max_id()
		created_timestamp: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		note: Notes = Notes(id, created_timestamp, head, text)
		self.__notes_list.append({'id':note.get_id(),'title':note.get_head(), 'date':note.get_created_timestamp(), 'note':note.get_text()})
		self.save_cache()
		return note.get_head
	
	def del_note(self, id: int):
		return self.__notes_list.pop(id-1).get('title') 

	def search_notes_list(self, word: str) -> list[dict[str, str]]:
		result: list[dict[str, str]] = []
		for note in self.__notes_list:
			for field in note.values():
				if word.lower().strip() in field.lower().strip():
					result.append(note)
					break
		return result
	
	def get_note_by_id(self, id: int) -> Notes:
		try:
			return self.__cache[id]
		except KeyError:
			return None # type: ignore
	
	def edit_notes_list(self, id: int, field: str, change: str):
		note: Notes = self.get_note_by_id(id)
		note.edit(field=field, new_content=change, change_timestamp=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
		self.save_cache()

		with suppress(Exception):
			if len(note.get_head()) > 0:
				self.__notes_list[id-1]['title'] = note.get_head()
		with suppress(Exception):
			if len(note.get_created_timestamp()) > 0:
				self.__notes_list[id-1]['date'] = note.get_created_timestamp()			
		with suppress(Exception):
			if len(note.get_text()) > 0:
				self.__notes_list[id-1]['note'] = note.get_text()
		return note.get_head()
	
	def save_cache(self) -> int:
		try:
			dict_notes: dict = {}
			for id in self.__cache:
				dict_notes[id]: dict = self.__cache[id].__dict__() # type: ignore
			with open(self.__path, "w", encoding="utf-8") as file:
				dump(dict_notes, file)
			return 0
		except IsADirectoryError:
			return 1