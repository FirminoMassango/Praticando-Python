#Classe responsável por conectar o software com o banco de dados SQLite

import sqlite3


class Conexao():
	def __init__(self):
		self.conexao = sqlite3.connect('dados.db') 	
		self.criarTabela()

	def criarTabela(self):
		ct = self.conexao.cursor()
		ct.execute('''create table if not exists utilizador (
					idUser integer primary key autoincrement,
					nome text,
					telefone text,
					email text,
					username text,
					senha text				
					) ''')

		self.conexao.commit()
		ct.close()

