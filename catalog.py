import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ColorProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

Builder.load_file("catalog.kv")


class CatalogLayout(BoxLayout):
    widgets = []

    def update_widgets(self, dir_name):
        print(os.listdir(os.path.join("choices", dir_name)))
        if len(self.widgets) > 0:
            for widget in self.widgets:
                self.remove_widget(widget)

        for i in sorted(os.listdir(os.path.join("choices", dir_name))):
            file_name = self.return_name_without_extension(i)
            widget = Button(text=file_name, size_hint=(0.45, None), height=dp(35), pos_hint={"center_x": 0.5})
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
