import os
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ColorProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from functools import partial

Builder.load_file("catalog.kv")


class CatalogLayout(BoxLayout):
    widgets = []
    current_app = ObjectProperty(None)
    def update_widgets(self, dir_name):
        print(os.listdir(os.path.join("choices", dir_name)))
        if len(self.widgets) > 0:
            for widget in self.widgets:
                self.remove_widget(widget)

        list_of_files = os.listdir(os.path.join("choices", dir_name))
        for i in sorted(list_of_files):
            file_name = self.return_name_without_extension(i)
            file_extention = os.path.splitext(i)
            path_to_file = os.path.join("choices", dir_name, i)

            if file_extention[1] == ".txt":
                function = partial(self.current_app.main_screen_manager.push_screen,
                                   "SheetViewer",
                                   path_to_file=path_to_file,
                                   extension=file_extention[1])

            elif file_extention[1] in [".jpg", ".gif", ".jpeg", ".ico", ".png"]:
                function = partial(self.current_app.main_screen_manager.push_screen,
                                   "MindMapViewer",
                                   path_to_file=path_to_file,
                                   extension=file_extention[1])
            else:
                function = partial(print, "bad formats")

            widget = Button(text=file_name,
                            size_hint=(0.45, None),
                            height=dp(35),
                            pos_hint={"center_x": 0.5},
                            on_press=function)

            self.add_widget(widget)
            self.widgets.append(widget)

    @staticmethod
    def return_name_without_extension(base_name):
        base_name_split = base_name.split(".")
        return "".join(base_name_split[0:-1])


class Catalog(BoxLayout):
    catalog_name = StringProperty("")
    back_color = ColorProperty((0, 0, 0, 0))
    catalog_layout = ObjectProperty(None)
