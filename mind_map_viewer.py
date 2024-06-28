from kivy import Config
from kivy import platform
if platform not in ["android", "ios"]:
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter

Builder.load_file("mind_map_viewer.kv")


class CustomScatter(Scatter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform in ["android", "ios"]:
            do_translation: False
        else:
            do_translation: True


class ScatterMindMap(BoxLayout):
    image_path = StringProperty("")
