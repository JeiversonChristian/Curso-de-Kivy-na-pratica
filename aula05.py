from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    # key words arguments -> é para poder receber os argumentos da classe mãe, mesmo não sabendo quais são
    # 'kwargs' é um nome padrão, mas eu posso colocar qualquer nome
    def __init__(self, tarefas, **kwargs):
        # super().__init__() é para fazer rodar o init do BoxLayout antes, pois ao herdarmos dele
        # podemos acabar subescrevendo o seu init com o novo init
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=30))


class Test2(App):
    def build(self):
        return Tarefas(['tarefa A', 'tarefa B'], orientation='horizontal')

Test2().run()