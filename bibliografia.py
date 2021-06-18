# com autor: SOBRENOME, Nome. Título da matéria. Nome do site. Disponível
# em: #  <URL>. Acesso em: dia, mês e ano.
# sem autor: TÍTULO da matéria. Nome do site, ano. Disponível em: <URL>.
# Acesso em: dia, mês e ano.

import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('TealMono')
        # Layout
        layout = [
            [sg.Text('Nome do Autor')],
            [sg.Input(key='nome', size=(60, 0))],
            [sg.Text('Sobrenome do Autor (em maiúsculo)')],
            [sg.Input(key='sobrenome', size=(60, 0))],
            [sg.Text('Título da Matéria')],
            [sg.Input(key='titulo', size=(60, 0))],
            [sg.Text('Nome do Site')],
            [sg.Input(key='nomeSite', size=(60, 0))],
            [sg.Text('Data do Acesso (dd/mm/aaaa)')],
            [sg.Input(key='data', size=(60, 0))],
            [sg.Text('URL da página')],
            [sg.Input(key='url', size=(60, 0))],

            [sg.Button('Gerar')],

            [sg.Output(size=(80, 8))]
        ]
        # Janela
        self.janela = sg.Window("Criador de Referências").layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            sobrenome = self.values['sobrenome']
            titulo = self.values['titulo']
            nomeSite = self.values['nomeSite']
            data = self.values['data']
            url = self.values['url']

            print(
                f'{sobrenome.upper()}, {nome}. {titulo}; {nomeSite}. Disponível em: <{url}>. Acesso em: {data}.')


tela = TelaPython()
tela.Iniciar()
