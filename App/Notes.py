import uuid

class Notes:
	@staticmethod
	def from_dict(dict_note: dict):
		return Notes(id=dict_note["id"],
	       created_timestamp=dict_note["created_timestamp"],
				 head=dict_note["head"],
	       text=dict_note["text"],
	       last_change_timestamp=dict_note["last_change_timestamp"])

	def __init__(self, id: str, created_timestamp: str, head: str,
              text: str, last_change_timestamp: str = None): # type: ignore
		self.__id: str = str(uuid.uuid1())[0:3]
		self.__created_timestamp: str = str(created_timestamp)
		self.__head: str = head
		self.__text: str = text
		if last_change_timestamp is None:
			self.__lastchange_timestamp: str = str(created_timestamp)
		else:
			self.__lastchange_timestamp = str(last_change_timestamp)
			
	def __dict__(self) -> dict:
		return {"id": self.__id, 
	  			  "created_timestamp": self.__created_timestamp,
						"head": self.__head,
						"text": self.__text,
						"last_change_timestamp": self.__lastchange_timestamp}
	def get_id(self) -> str:
		return self.__id
	
	def get_created_timestamp(self) -> str:
		return self.__created_timestamp
	
	def get_last_change_timestamp(self) -> str:
		return self.__lastchange_timestamp
	
	def get_head(self) -> str:
		return self.__head
	
	def get_text(self) -> str:
		return self.__text
	
	def edit(self, field: str, new_content: str, change_timestamp: str) -> None:
		if field == "1":
			self.__head = new_content
		elif field == "2":
			self.__text = new_content
		self.__lastchange_timestamp = str(change_timestamp)

  