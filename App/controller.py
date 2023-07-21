import text
from view import View
from model import Model, Notes

#self.model = model.Notes()

class Controller:
	def __init__(self, model: Model, view: View):
		self.model = model
		self.view = view

	def start(self):
		while True:
			choice = self.view.main_menu() # вывод меню и предоставление выбора
			match choice:
				case 1: # Открыть файл +
					self.model.open_notes_list()#self.view.print_message(text.cancel))
					self.view.print_message(text.load_successful)
				case 2: # Записать файл +
					self.model.save_notes_list()
					self.view.print_message(text.save_successful)
				case 3: # Показать заметки +
					notes_list = self.model.get_notes_list()
					self.view.print_notes(notes_list, text.load_error)
				case 4: # Добавить заметку +
					head_: str = self.view.input_content(text.content_head)
					text_: str = self.view.input_content(text.content_text)
					self.model.add_new_note(head_, text_)
					self.view.print_message(text.new_note_successful(head_)) # type: ignore
				case 5: # Найти заметку +
					word = self.view.input_search(text.input_search)
					result = self.model.search_notes_list(word)
					self.view.print_notes(result, text.empty_search(word))
				case 6: # Изменить заметку
					notes_list = self.model.get_notes_list()
					id = self.view.input_index(notes_list, text.input_index, text.load_error)
					field = self.view.input_note(text.cancel_input)
					note = self.view.input_note(text.cancel_input)
					result = self.model.edit_notes_list(id, field, note)
					self.view.print_message(text.change_successful(note))
				case 7: # Удалить заметку +
					notes_list = self.model.get_notes_list()
					id = self.view.input_index(notes_list, text.index_del_note, text.load_error)
					name = self.model.del_note(id)
					self.view.print_message(text.del_note(name)) # type: ignore
				case 8:
					break
