'''
			CABEÇALHO
_________________________________________________
	Esse software ...

Desenvolvedor: Firmino Massango
'''

from tkinter import *
from Variaveis import *


class Login(object):
	def __init__(self,inst):
		#Imagem
		imagem = PhotoImage(file = 'Imagens/usr.gif')
		self.imagemUser = Label(inst, image = imagem, bg = '#4B0082')
		self.imagemUser.image = imagem
		self.imagemUser.pack()

		#Criando compontes: Utilizador
		self.lbUser = Label(inst, text = 'Utilizador', bg = fundo, fg = 'white', font = fonte)
		self.txtUser = Entry(inst, border = 0, highlightbackground = txtClr, highlightcolor = txtClr, font = fonte2)

        #Criando Componentes: Senha
		self.lbPass = Label(inst, text = 'Senha', bg = fundo, fg = 'white', font = fonte)
		self.txtPass = Entry(inst, border = 0, highlightbackground = txtClr, highlightcolor = txtClr, show = '•', font = fonteSenha)

		#Botão confirmar
		self.btnConf = Button(inst, text = 'Confirmar', border = 0, bg = 'white', font = fonte1)

		#Botão limpar
		self.btnLimp = Button(inst, text = 'Limpar', border = 0, bg = 'white',font = fonte1, command = self.Limpar())

        #CheckButton e Botao p'ra senha esquecida
		self.btnCheck = Checkbutton(inst, text = 'Lembra - me', border = 0, fg= 'white',selectcolor = '#1500FF', highlightbackground = fundo,bg = fundo, font = fonte1)
		self.btnSenh = Button(inst, text = 'Esqueci a senha', border = 0, bg = fundo, fg = 'white', font = fonte1)

		#Pack
		self.lbUser.pack()
		self.txtUser.pack()
		self.lbPass.pack()
		self.txtPass.pack()
		self.btnConf.pack()
		self.btnLimp.pack()
		self.btnCheck.pack()
		self.btnSenh.pack()

		#Place
		self.lbUser.place(x =20, y = 190)
		self.txtUser.place(x =70, y = 230,height = 25, width = 255)
		self.lbPass.place(x =20, y = 260)
		self.txtPass.place(x =70, y = 300,height = 25, width = 255)
		self.btnConf.place(x = 110, y = 415, height = 30, width = 80)
		self.btnLimp.place(x = 195, y = 415, height = 30, width = 80)
		self.btnCheck.place(x =125, y = 350)
		self.btnSenh.place(x =120, y = 470, height = 22)


	def Limpar(self):
		pass


inst = Tk()										#Instanciando a classe Tk
inst['bg'] = fundo								#Alterando a cor do fundo
#ícone
#inst.wm_iconbitmap('~/Documentos/Python/logo.ico')

inst.title('Autenticação')						#Nome/título da janela
Login(inst)										#Assossiando a classe Login ao mestre(instância)
inst.geometry('350x500')						#Definindo o tamanho da janela
inst.resizable('False','False')					#Impedindo o redimensionamento da tela
inst.mainloop()									#Iniciando o programa
