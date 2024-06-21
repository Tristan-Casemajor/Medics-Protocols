from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.properties import Clock, ObjectProperty

Builder.load_file("select_file.kv")



class SelectFileLayout(BoxLayout):
    current_app = ObjectProperty(None)
    def set_image(self, path):
        try:
            split_path = os.path.splitext(path[0])
        except:
            pass
        else:
            if split_path[1].lower() in [".png", ".jpg", ".gif", ".jpeg", ".ico"]:
                self.current_app.main_screen_manager.get_screen("AddMindMap").layout.preview_image.source = path[0]
                self.current_app.main_screen_manager.pop_screen()
