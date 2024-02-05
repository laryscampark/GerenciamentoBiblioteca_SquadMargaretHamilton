import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

#criacao da tbl
#cursor.execute('CREATE TABLE usuario(id_usuario INT, nome VARCHAR (100),telefone INT, endereco VARCHAR (100),nacionalidade VARCHAR (100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE livro(id_livro INT, titulo VARCHAR (100), editora VARCHAR (100), autor VARCHAR(100), genero VARCHAR(100));')
#cursor.execute('CREATE TABLE biblioteca(id_usuario INT, id_livro INT, nome VARCHAR (100),telefone INT, nacionalidade VARCHAR (100), PRIMARY KEY(id_usuario,id_livro), FOREIGN KEY (id_livro) REFERENCES livro(id_livro),FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario));')
#cursor.execute('CREATE TABLE exemplares(id_usuario INT, id_livro INT, data_emprestimo DATE, data_devolucao DATE, limite_renovacao INT, estado_exemplar VARCHAR(100), PRIMARY KEY(id_usuario, id_livro), FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario), FOREIGN KEY(id_livro) REFERENCES livro(id_livro));')

#alteracao na tbl 

      
      
conexao.commit()
conexao.close

