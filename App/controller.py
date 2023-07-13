import text
import view
import model

def start():
		while True:
				choice = view.main_menu() # вывод меню и предоставление выбора
				match choice:
						case 1: # Открыть файл
								model.open_notes_list()
								view.print_message(text.load_successful)
						case 2: # Записать файл
								model.save_notes_list()
								view.print_message(text.save_successful)
						case 3: # Показать заметки
								notes_list = model.get_notes_list()
								view.print_notes(notes_list, text.load_error)
						case 4: # Добавить заметку 
								note = view.input_note(text.input_new_note, text.cancel_input)
								name = model.add_note(note)
								view.print_message(text.new_note_successful(name)) # type: ignore
						case 5: # Найти заметку
								word = view.input_search(text.input_search)
								result = model.search_notes_list(word)
								view.print_notes(result, text.empty_search(word))
						case 6: # Изменить заметку
								notes_list = model.get_notes_list()
								index = view.input_index(text.input_index, notes_list, text.load_error)
								note = view.input_note(text.input_new_note, text.cancel_input)
								result = model.change_notes_list(note, index)
								view.print_message(text.change_successful(note))
						case 7: # Удалить заметку 
								notes_list = model.get_notes_list()
								index = view.input_index(text.index_del_note, notes_list, text.load_error)
								name = model.del_note(index)
								view.print_message(text.del_note(name)) # type: ignore
						case 8:
								break
