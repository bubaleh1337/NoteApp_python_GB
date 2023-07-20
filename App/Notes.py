class Note:
	def __init__(self, created_timestamp: float, head: str,
              text: str, last_change_timestamp: float = None): # type: ignore
		self.__created_timestamp: int = int(created_timestamp)
		self.__head: str = head
		self.__text: str = text
		if last_change_timestamp is None:
			self.__lastchange_timestamp: int = int(created_timestamp)
		else:
			self.__lastchange_timestamp = int(last_change_timestamp)