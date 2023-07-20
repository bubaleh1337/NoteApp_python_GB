from controller import Controller
from model import Notes
from view import View

view: View = View()
model: Notes = Notes()
controller: Controller = Controller(model=, view=view)

controller.start()