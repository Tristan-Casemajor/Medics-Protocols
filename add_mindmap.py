import os
import shutil
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy import platform
Builder.load_file("add_mindmap.kv")


class PreviewImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform in ["android", "ios"]:
            self.size_hint = 1, 0.4


class AddMindMapLayout(BoxLayout):
    confirm_text = StringProperty("")
    confirm_label = ObjectProperty(None)

    def save_mind_map(self, source, destination, name):
        if source != "images/icon.png" and os.path.exists(source):
            try:
                extension = os.path.splitext(source)
                shutil.copy2(source, os.path.join(destination, name+extension[1]))
            except:
                self.confirm_label.height = dp(14)
                self.confirm_text = "Impossible d'enregistrer la fiche"
                Clock.schedule_once(self.reset_label_confirm, 2)
            else:
                self.confirm_label.height = dp(14)
                self.confirm_text = "Fiche enregistrée"
                Clock.schedule_once(self.reset_label_confirm, 2)

    def reset_label_confirm(self, *args):
        self.confirm_label.height = 0
        self.confirm_text = ""
