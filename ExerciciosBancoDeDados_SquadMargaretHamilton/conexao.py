import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
#criacao da tbl
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR (100), endereco VARCHAR (100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR (100), endereco VARCHAR (100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR (100), endereco VARCHAR (100), email VARCHAR(100));')

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
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados: 
      print(usuario)
      
      
conexao.commit()
conexao.close