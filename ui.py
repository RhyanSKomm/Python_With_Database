import tkinter as tk
import database as db
from tkinter import ttk


def listagemLivros():
    novaJanela = tk.Toplevel()
    novaJanela.title("Listagem de livros")
    novaJanela.geometry("600x600")

    #Titulo da Janela
    labelTitulo = tk.Label(novaJanela,text="Listagem de Livros")
    labelTitulo.pack(pady=10)


    colunas = ("isbn","titulo","autor")
    tabelaProdutos = ttk.Treeview(novaJanela, columns=colunas, show="headings")
    tabelaProdutos.pack(fill="both")


    tabelaProdutos.heading("isbn", text="ID")
    tabelaProdutos.heading("titulo", text="Titulo")
    tabelaProdutos.heading("autor", text="Autor")


    tabelaProdutos.column("isbn",width=50)
    tabelaProdutos.column("titulo",width=50)
    tabelaProdutos.column("autor",width=50)

    btnListaProdutos = tk.Button(novaJanela, text="Listar Livros",command=lambda: carregarProdutos())
    btnListaProdutos.pack(pady=10)

    def carregarProdutos():
        registros = db.findAll("livro")

        for i in tabelaProdutos.get_children():
            tabelaProdutos.delete(i)
        for registro in registros:
            tabelaProdutos.insert("",tk.END,values=registro)

    # btnFechar = tk.Button(novaJanela, text="fechar", command=novaJanela.destroy)
    # btnFechar.pack(pady=10)








def abrir_janela_cadastra_produto():
    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Produtos")
    nova_janela.geometry("400x600")

    label_isbn = tk.Label(nova_janela, text="ISBN").pack(pady=10)
    input_isbn = tk.Entry(nova_janela)
    input_isbn.pack(pady=10)

    label_titulo = tk.Label(nova_janela, text="Titulo").pack(pady=10)
    input_titulo = tk.Entry(nova_janela)
    input_titulo.pack(pady=10)

    label_autor = tk.Label(nova_janela, text="Autor").pack(pady=10)
    input_autor = tk.Entry(nova_janela)
    input_autor.pack(pady=10)

    label_ano_publicacao = tk.Label(nova_janela, text="Ano de Publicação").pack(pady=10)
    input_ano_publicacao = tk.Entry(nova_janela)
    input_ano_publicacao.pack(pady=10)

    label_id_categoria = tk.Label(nova_janela, text="ID Categoria").pack(pady=10)
    input_id_categoria = tk.Entry(nova_janela)
    input_id_categoria.pack(pady=10)

    btn_cadastra_produto = tk.Button(nova_janela, text="Cadastrar", command=lambda:db.cadastra_livro(input_isbn.get(), input_titulo.get(), input_autor.get(), input_ano_publicacao.get(), input_id_categoria.get()))
    btn_cadastra_produto.pack(pady=10)





def telaPrincipal():
    root = tk.Tk()
    root.title('Biblioteca')
    root.geometry('600x600')
    

    btn_listar_livros = tk.Button(root, text="Listar todos os livros",command=listagemLivros)
    btn_listar_livros.pack(pady=10)
    
    
    btn_cadastra_livro = tk.Button(root, text="Cadastrar Produto", command=abrir_janela_cadastra_produto)
    btn_cadastra_livro.pack(pady=10)
    
    root.mainloop()