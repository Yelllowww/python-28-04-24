import sqlite3
database = 'concessionaria.db'
conexao=sqlite3.connect(database)
cur=conexao.cursor()

sql='''CREATE TABLE if not exists tb_carro(
                    placa text primary key,
                    ano int not null,
                    modelo text not null)'''

cur.execute(sql)
cur.close()
conexao.close()
print("fechou a base de dados")

# import sqlite3
# database = 'concessionaria.db'
# conexao=sqlite3.connect(database)
# cur=conexao.cursor()
#
# sql = '''INSERT INTO tb_carro(placa,ano,modelo)
#                 VALUES('ABC1234',1980,'Sedan')'''
#
# sql2 = '''INSERT INTO tb_carro(placa,ano,modelo)
#                 values('DEF5678',1990,'Suv')'''
#
# cur.execute(sql)
# cur.execute(sql2)
# conexao.commit()
# cur.close()
# conexao.close()
# print("Conexão fechada")

# import sqlite3
# database = 'concessionaria.db'
# conexao=sqlite3.connect(database)
# cur=conexao.cursor()
#
# sql = '''SELECT * from tb_carro'''
# sql2 = '''SELECT placa,ano,modelo FROM tb_carro'''
#
# cur.execute(sql)
# consulta = cur.fetchall()
# if len(consulta) == 0:
#     print("Tabela vazia")
# else:
#     print(consulta)
# cur.execute(sql2)
# consulta = cur.fetchall()
# if len(consulta) == 0:
#     print("Coluna(s) vazias")
# else:
#     print(consulta)
# conexao.commit()
# cur.close()
# conexao.close()
# print("Conexão fechada")





