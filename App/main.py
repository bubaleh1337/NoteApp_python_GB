from controller import Controller
from model import Model
from view import View

view: View = View()
model: Model = Model()
controller: Controller = Controller(model=model, view=view)

controller.start()