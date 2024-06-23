import os
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

Builder.load_file("specialty_selector.kv")


class LayoutStackChoices(StackLayout):
    choice = StringProperty("")
    def protect_selection(self, current_widget, *args):
        widgets = args
        if not current_widget.active:
            self.choice = ""
        else:
            for widget in widgets:
                widget.active = False
            self.choice = os.path.join("choices", current_widget.name)
        print(self.choice)
        print(os.path.exists(self.choice))


class LayoutTextCheckBox(BoxLayout):
    pass


class SpecialitySelector(ScrollView):
    layout_stack = ObjectProperty(None)
