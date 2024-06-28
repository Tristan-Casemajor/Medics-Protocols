import os

from kivy.graphics import Color, Rectangle
from kivy.properties import Clock
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("add_sheet.kv")

class AddSheetLayout(BoxLayout):
    text_input_sheet = ObjectProperty(None)
    confirm_label = ObjectProperty(None)
    confirm_text = StringProperty("")
    browse_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(0.139, 0.207, 0.218, 1))
            self.separator = Rectangle(pos=(0, self.height/1.215), size=(self.width, dp(5)))
        Clock.schedule_interval(self.set_size, 1/30)


    def set_size(self, *args):
        self.separator.pos = 0, self.browse_button.pos[1]-dp(11)
        self.separator.size = self.width, dp(5)

    def read_text_file(self, path):
        try:
            file = open(path, "r", encoding="utf8")
            data = file.read()
            file.close()
        except:
            self.text_input_sheet.text = "Impossible de charger la fiche (mauvais format)"
        else:
            self.text_input_sheet.text = data

    def save_sheet(self, name, text, destination):
        try:
            file = open(os.path.join(destination, name+".txt"), "w", encoding="utf8")
            file.write(text)
            file.close()
        except Exception as e:
            print(e)

        self.confirm_label.height = dp(14)
        self.confirm_text = "Fiche enregistrée"
        Clock.schedule_once(self.reset_label_confirm, 2)

    def reset_label_confirm(self, *args):
        self.confirm_label.height = 0
        self.confirm_text = ""

