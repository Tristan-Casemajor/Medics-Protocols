from kivy import platform
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_file("menu.kv")

class AddButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform in ["android", "ios"]:
            self.font_size = dp(12)
        else:
            self.font_size = dp(15)


class Menu(BoxLayout):
    pass