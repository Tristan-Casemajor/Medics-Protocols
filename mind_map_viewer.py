from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter

Builder.load_file("mind_map_viewer.kv")


class ScatterMindMap(BoxLayout):
    image_path = StringProperty("")
