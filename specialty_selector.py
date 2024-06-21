from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

Builder.load_file("specialty_selector.kv")

class LayoutStackChoices(StackLayout):
    pass

class LayoutTextCheckBox(BoxLayout):
    pass

class SpecialitySelector(ScrollView):
    pass
