from kivy.app import App
from kivy.uix.button import Button

# a classe "Test" vai herdar as funcionalidades da classe "App" que importei
class Test(App):
    def build(self):
        return Button(text='Olá, mundo!')

# run é uma funcionalidade de App    
Test().run()