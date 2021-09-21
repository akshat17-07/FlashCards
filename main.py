import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from csv_module import csv_reader, csv_writer
import random

selected_course = ""

class MainWindow(Screen):
    pass

class SelectWindow(Screen):
    subject = ObjectProperty(None)

    def btn(self):
        if csv_reader(self.subject.text):
            global selected_course
            selected_course = self.subject.text.upper()
            return True
        return False

class ReviewWindow(Screen):
    question = ObjectProperty(None)
    answer = ObjectProperty(None)

    def btn(self):
        data = csv_reader(selected_course)
        ran = random.choice(data[1:])
        self.question.text = ran[0]
        self.answer.text = ran[1]

class AddWindow(Screen):
    question = ObjectProperty(None)
    answer = ObjectProperty(None)
    subject = ObjectProperty(None)

    def btn(self):

        subject = self.subject.text
        subject = subject.upper()


        if subject != "":
            data = [self.question.text, self.answer.text]

            csv_writer(subject, data)

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
