from kivy import Config
from kivy import platform
if platform not in ["android", "ios"]:
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
else:
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter

Builder.load_file("mind_map_viewer.kv")


class CustomScatter(Scatter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scale_min = 0.5
        self.scale_max = 2.0
        if platform in ["android", "ios"]:
            self.do_translation = False
        else:
            self.do_translation = True


class ScatterMindMap(BoxLayout):
    image_path = StringProperty("")
