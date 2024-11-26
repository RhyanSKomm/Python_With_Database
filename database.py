import mysql.connector
from tkinter import ttk, messagebox
import tkinter as tk
import ui

def conexao_banco():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca2'
        )

        print("deu certo a conexao")
        return cnx
    except:
        print("Deu erro na conexao")

def buscar_todos(tabela):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "SELECT isbn, titulo, autor FROM {}".format(tabela)
        cursor.execute(query)
        registros = cursor.fetchall()

        return registros

    except:
        print("Não foi possivel selecionar todos da tabela {}".format(tabela))
    
    finally:
        cursor.close()

def buscar_produto_nome(nome):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "SELECT * FROM livro WHERE titulo LIKE '%{}%'".format(nome)
        cursor.execute(query)
        registros = cursor.fetchall()

        # for registro in registros:
        #     tree.insert("", tk.END, values=registro)

        resposta = []
        for row in registros:
            resposta = [{"isbn": row[0], "titulo": row[1], "autor": row[3]}]
        
        return resposta
    
    except:
        print("Não encontrei esse registro")
    
    finally:
        cursor.close()

def buscar_produto_id(id_produto):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "SELECT * FROM livro WHERE id = {}".format(id_produto)

        cursor.execute(query)

        resultado = cursor.fetchone()

        if resultado:
            return {
                "isbn": resultado[0],
                "titulo": resultado[1],
                "autor": resultado[2],
                "ano_publicacao": resultado[3],
                "id_categoria": resultado[4]
            }
    except:
        messagebox.showerror("ALERTA!!!!", "Não foi possível encontrar o registro com esse id")

def cadastra_produto(titulo, autor, ano_publicacao, id_categoria):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "INSERT INTO livro (titulo, autor, ano_publicacao, id_categoria) values (%s, %s, %s, %s)"

        cursor.execute(query, (titulo, autor, ano_publicacao, id_categoria))

        conexao.commit()

        messagebox.showwarning("Sucesso", "Produto cadastrado com sucesso")
    except:
        messagebox.showerror("Erro", "Nâo foi possivel inserir um produto")

def excluir_produto(produto_id):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "DELETE FROM livro WHERE isbn = {}".format(produto_id)

        cursor.execute(query)
        conexao.commit()

        messagebox.showinfo("AVISO!!!", "Registrado deletado com sucesso")
    except:
        messagebox.showerror("Erro", "Não foi possível excluir o produto")

def atualizar_produto(produto_id, titulo, autor, ano_publicacao, id_categoria, nova_janela):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = """ UPDATE livro set 
            titulo = %s, autor = %s, ano_publicacao = %s, id_categoria = %s
            WHERE id = %s
            """

        cursor.execute(query, (titulo, autor, ano_publicacao, id_categoria, produto_id))

        conexao.commit()

        nova_janela.destroy()

        messagebox.showinfo("ALERTA!!!", "Produto alterado com sucesso")

    except:
        messagebox.showerror("AVISO!!!!", "Não foi possível atualizar o registro")
