import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

#criacao da tbl
#cursor.execute('CREATE TABLE usuario(id_usuario INT, nome VARCHAR (100),telefone INT, endereco VARCHAR (100),nacionalidade VARCHAR (100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE livro(id_livro INT, titulo VARCHAR (100), editora VARCHAR (100), autor VARCHAR(100), genero VARCHAR(100));')
#cursor.execute('CREATE TABLE biblioteca(id_usuario INT, id_livro INT, nome VARCHAR (100),telefone INT, nacionalidade VARCHAR (100), PRIMARY KEY(id_usuario,id_livro), FOREIGN KEY (id_livro) REFERENCES livro(id_livro),FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario));')
#cursor.execute('CREATE TABLE exemplares(id_usuario INT, id_livro INT, data_emprestimo DATE, data_devolucao DATE, limite_renovacao INT, estado_exemplar VARCHAR(100), PRIMARY KEY(id_usuario, id_livro), FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario), FOREIGN KEY(id_livro) REFERENCES livro(id_livro));')

#alteracao na tbl 
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone ') renomear 

#deletar tbl
#cursor.execute('DROP TABLE produtos')

#inserir dados 
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone) VALUES (1,"ISADORA", "FRANCA", "oi@oioi.com", 4320-0987 )')
#cursor.execute('INSERT INTO gerentes(id, nome, endereco,email) VALUES (8 ,"CINTIA", "ARARAQUARA", "oi@oioi.com" )')

#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1,"ISADORA", "FRANCA", "oi@oioi.com", 43200987 )')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone) VALUES (2,"MARIA", "BOITUVA", "ola@oioi.com", 43200965 )')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone) VALUES (3,"LUZIA", "SOROCABA", "xau@oioi.com", 43200945 )')
#cursor.execute('INSERT INTO usuario(id, nome, endereco,email, telefone) VALUES (4,"ANA", "CAPELA", "oie@oioi.com", 4320035 )')

#excluir dados 
#cursor.execute('DELETE FROM usuario where id=1')

#visualizar os dados 
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
#for usuario in dados: 
 #   print(usuario)

#cursor.execute('UPDATE usuario SET endereco="MINAS GERAIS" WHERE nome="ANA"')
  
#LIMIT e DISTINCT
#dados = cursor.execute('SELECT * FROM usuario LIMIT 3')
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 1')

#GROUP BY e HAVING 
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3 ')

#JOIN's 
#JOIN - INNER JOIN 
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

#JOIN - Left JOIN 
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

#JOIN - RIGHT JOIN 
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

#JSUBCONSULTAS 

      
      
conexao.commit()
conexao.close

