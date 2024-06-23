import os
import shutil
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

Builder.load_file("add_mindmap.kv")


class PreviewImage(Image):
    pass

class AddMindMapLayout(BoxLayout):
    def save_mind_map(self, source, destination):
        if source != "images/icon.png" and os.path.exists(source):
            shutil.copy2(source, destination)
