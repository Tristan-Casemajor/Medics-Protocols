from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file("boxlayout_actionbar.kv")


class ButtonWithImageAtCenter(Button):
    image_source = StringProperty("")


class BoxLayoutActionBar(BoxLayout):
    pass