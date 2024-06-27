from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("previous_bar.kv")


class PreviousBar(BoxLayout):
    image_source = StringProperty("")
    illustration = StringProperty("")