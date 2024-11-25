import mysql.connector
from tkinter import messagebox

def conexao_banco():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca2'
            )
        
        print('Deu certo a conexão')
        return cnx
    
    except:
          print('Deu erro na conexão')

def findAll(tabela):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = f"SELECT isbn,titulo,autor FROM {tabela}"
        cursor.execute(query)
        registros = cursor.fetchall()

        return registros

    except:
        print(f'Não foi possível listar todos da tabela {tabela}')


def findBook(nome):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = f"SELECT * FROM livro WHERE titulo LIKE '%{nome}%'"
        cursor.execute(query)
        registros = cursor.fetchall()
         
        
            
    except:
        print('Deu ruim')

def cadastra_livro(isbn,titulo, autor, ano_publicacao, id_categoria):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "INSERT INTO livro (isbn, titulo, autor, ano_publicacao, id_categoria) values (%s, %s, %s, %s,%s)"

        cursor.execute(query, (isbn,titulo, autor, ano_publicacao, id_categoria))
        
        conexao.commit()
        
        messagebox.showwarning("Sucesso", "Produto cadastrado com sucesso")
    except:
        messagebox.showerror("Erro", "Não foi possível cadastrar")


def excluir_produto(produto_id):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "DELETE FROM livro WHERE isbn = %s"
        cursor.execute(query,(produto_id))
    except:
        messagebox.showerror("Error","Não foi possível excluir o produto")