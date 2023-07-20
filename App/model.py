from contextlib import suppress
from datetime import datetime
import json
from time import time

class Notes:
 
	@staticmethod
	def from_dict(dict_note: dict):
		return Notes(created_timestamp=dict_note["created_timestamp"],
               head=dict_note["head"],
               text=dict_note["text"],
               last_change_timestamp=dict_note["last_change_timestamp"])

	def __init__(self, created_timestamp: float, head: str,
              text: str, last_change_timestamp: float = None): # type: ignore
		self.__created_timestamp: int = int(created_timestamp)
		self.__head: str = head
		self.__text: str = text
		if last_change_timestamp is None:
			self.__lastchange_timestamp: int = int(created_timestamp)
		else:
			self.__lastchange_timestamp = int(last_change_timestamp)

	def __dict__(self) -> dict:
		return {#"id": self.__id,
	  				"created_timestamp": self.__created_timestamp,
						"head": self.__head,
						"text": self.__text,
						"last_change_timestamp": self.__lastchange_timestamp}
	
	def get_created_timestamp(self) -> int:
		return self.__created_timestamp
	
	def get_last_change_timestamp(self) -> int:
		return self.__lastchange_timestamp
	
	def get_head(self) -> str:
		return self.__head
	
	def get_text(self) -> str:
		return self.__text
	
	def edit(self, field: str, new_content: str, change_timestamp: float) -> None:
		if field == "1":
			self.__head = new_content
		elif field == "2":
			self.__text = new_content
		self.__lastchange_timestamp = int(change_timestamp)


	__notes_list: list[dict[str, str]] = []
	__path = 'notes.txt'
	def open_notes_list(self, cancel):
		try:
			with open(self.__path, "r", encoding='utf-8') as read_file:
				temp = json.loads(read_file.read())# 'Kate:7444654:comment'
			for key, value in temp.items():
				self.__notes_list[int(key)] = value
		except:
			cancel
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
		created_timestamp: float = time()
		note: Notes = Notes(created_timestamp, head, text)
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
