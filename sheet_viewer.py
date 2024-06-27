from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import textwrap

Builder.load_file("sheet_viewer.kv")


class ViewerLabel(Label):

    def update_text(self, path):
        try:
            file = open(path, "r", encoding="utf8")
            data = file.readlines()
            file.close()
        except Exception as e:
            print(e)
        else:
            text = ""
            for i in data:
                if i.index != 0:
                    text += f"\n{textwrap.fill(i, width=70)}"
                else:
                    text += textwrap.fill(i, width=70)
            self.text = text


class ScrollSheetViewer(ScrollView):
    viewer_label = ObjectProperty(None)
