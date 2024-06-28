from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.properties import Clock, ObjectProperty
from kivy.uix.filechooser import FileChooserIconView
from kivy import platform
if platform == "android":
    from android.permissions import Permission, request_permissions

Builder.load_file("select_file.kv")


class FileSelector(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manage_path()

    def manage_path(self):
        if platform == "android":
            request_permissions([Permission.INTERNET,
                                Permission.READ_EXTERNAL_STORAGE,
                                Permission.WRITE_EXTERNAL_STORAGE])
        if platform == "android":
            self.path = "/storage/emulated/0/Download"
        elif platform == "ios":
            self.path = ""
        elif platform == "linux":
            self.path = os.path.expanduser("~/Downloads")
        elif platform == "win":
            self.path = os.path.expanduser("~/Downloads")

    def reset_path(self):
        self.manage_path()


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
            elif split_path[1].lower() == ".txt":
                self.current_app.main_screen_manager.get_screen("AddSheet").layout.read_text_file(path[0])
            self.current_app.main_screen_manager.pop_screen()
