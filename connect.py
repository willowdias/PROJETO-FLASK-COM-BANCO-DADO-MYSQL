import pymysql


conexao = pymysql.connect(db='cadastro', user='root', passwd='')

cursor = conexao.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS usuario (id int(11) NOT NULL AUTO_INCREMENT,nome VARCHAR(50) NOT NULL, senha  VARCHAR(50) NOT NULL,email  VARCHAR(100) NOT NULL,PRIMARY KEY (id))");
#cursor.execute("INSERT INTO usuario (nome, senha, email) VALUES ('victor','2020','willow18282@gmail.com' )")
#cursor.execute("UPDATE tb_cidades SET cidade =LOWER (cidade)")
#cursor.execute("SELECT *from usuario")
resultado = cursor.fetchall()


for linha in resultado :
    print(linha)
conexao.close()