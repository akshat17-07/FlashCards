import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class ReviewWindow(Screen):
    pass

class AddWindow(Screen):
    question = ObjectProperty(None)
    answer = ObjectProperty(None)

    def btn(self):
        print("Name", self.question.text)
        print("Email", self.answer.text)

        self.question.text = ""
        self.answer.text = ""


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("mymain.kv")

class MyMainApp(App):
    def build (self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
