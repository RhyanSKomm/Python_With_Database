import tkinter as tk
import database as db
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def abrir_janela_lista_produtos():
    nova_janela = tk.Toplevel()
    nova_janela.title("Listagem de Livro")
    nova_janela.geometry("600x600")

    def aplicar_filtro():

        for item in tabela_produtos.get_children():
            tabela_produtos.delete(item)
            
        registros_filtro = db.buscar_produto_nome(entry_descricao.get())

        for registro_filtro_aplicado in registros_filtro:
            tabela_produtos.insert("", "end", values=(
                registro_filtro_aplicado.get("isbn", ""),
                registro_filtro_aplicado.get("titulo", ""),
                registro_filtro_aplicado.get("autor", ""),
            ))

    # Titulo da minha Janela
    label_titulo = tk.Label(nova_janela, text="Listagem de Livro")
    label_titulo.pack(pady=10)

    tk.Label(nova_janela,text="Pesquise o livro").pack(pady=10)
    entry_descricao = tk.Entry(nova_janela, width=50)
    entry_descricao.pack(pady=10)

    btn_filtro = tk.Button(nova_janela, text="Filtrar", command=lambda:aplicar_filtro())
    btn_filtro.pack(pady=10)

    colunas = ("isbn", "Titulo", "Autor")
    tabela_produtos = ttk.Treeview(nova_janela, columns=colunas, show="headings")
    tabela_produtos.pack(fill="both")

    # Configura o cabeçalho do coluna
    tabela_produtos.heading("isbn", text="isbn")
    tabela_produtos.heading("titulo", text="titulo")
    tabela_produtos.heading("autor", text="autor")

    # Especificar tamanho das colunas
    tabela_produtos.column("isbn", width=50)
    tabela_produtos.column("titulo", width=250)
    tabela_produtos.column("autor", width=100)

    btn_lista_produtos = tk.Button(nova_janela, text="Listar Livro", command=lambda:carregar_produtos())
    btn_lista_produtos.pack(pady=10)


    def carregar_produtos():
        registros = db.buscar_todos("livro")

        for item in tabela_produtos.get_children():
            tabela_produtos.delete(item)

        for registro in registros:
            tabela_produtos.insert("", tk.END, values=registro)

    
    def excluir_registro():
        selected_item = tabela_produtos.selection()

        if selected_item:
            item = tabela_produtos.item(selected_item)

            produto_id = item["values"][0]

            db.excluir_produto(produto_id)

            nova_janela.destroy()

    def editar_registro():
        selected_item = tabela_produtos.selection()

        if selected_item:
            item = tabela_produtos.item(selected_item)

            produto_id = item["values"][0]

            abrir_janela_editar_registro(produto_id)
    

    btn_editar_registro = tk.Button(nova_janela, text="Editar Item Selecionado", command=lambda:editar_registro())
    btn_editar_registro.pack(pady=10)

    btn_delete = tk.Button(nova_janela, text="Deletar Item Selecionado", command=lambda: excluir_registro())
    btn_delete.pack(pady=10)

def abrir_janela_editar_registro(id_produto):
    lancamentos = db.buscar_produto_id(id_produto)

    nova_janela = tk.Toplevel()
    nova_janela.title("Editar Registro")
    nova_janela.geometry("600x600")

    tk.Label(nova_janela, text="ISBN DO PRODUTO").pack(pady=10)
    entry_id = tk.Entry(nova_janela)
    entry_id.insert(0, str(id_produto))
    entry_id.config(state="disabled")
    entry_id.pack(pady=10)

    tk.Label(nova_janela, text="Titulo").pack(pady=10)
    entry_descricao = tk.Entry(nova_janela)
    entry_descricao.insert(0, str(lancamentos.get('titulo', '')))
    entry_descricao.pack(pady=10)

    tk.Label(nova_janela, text="Autor").pack(pady=10)
    entry_cod_barras = tk.Entry(nova_janela)
    entry_cod_barras.insert(0, str(lancamentos.get('autor', '')))
    entry_cod_barras.pack(pady=10)

    tk.Label(nova_janela, text="Ano de Publicação").pack(pady=10)
    entry_preco = tk.Entry(nova_janela)
    entry_preco.insert(0, str(lancamentos.get('ano_publicacao', '')))
    entry_preco.pack(pady=10)

    tk.Label(nova_janela, text="Categoria").pack(pady=10)
    entry_categoria = tk.Entry(nova_janela)
    entry_categoria.insert(0, str(lancamentos.get('id_categoria', '')))
    entry_categoria.pack(pady=10)

    btn_salvar_alteracao = tk.Button(nova_janela, text="Salvar Alteração", command=lambda:db.atualizar_produto(
        id_produto, entry_descricao.get(), 
        entry_cod_barras.get(), 
        entry_preco.get(), 
        entry_categoria.get(),
        nova_janela
        ))
    btn_salvar_alteracao.pack(pady=10)
    
def abrir_janela_cadastro_produto():

    #METODO QUE LIMPA INPUTS
    def limpa_campos():
        input_descricao.delete(0, tk.END)
        input_preco.delete(0, tk.END)
        input_cod_barras.delete(0, tk.END)
        input_id_categoria.delete(0, tk.END)

    # METODO QUE SALVA PRODUTO NO BANCO E LIMPA OS INPUTS
    def salva_produto():
        db.cadastra_produto(
            input_descricao.get(), 
            input_cod_barras.get(), 
            input_preco.get(), 
            input_id_categoria.get()
        )

        limpa_campos()


    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Produto")
    nova_janela.geometry("400x600")

    # Label e Input da descrição
    label_descricao = tk.Label(nova_janela, text="Tiulo")
    label_descricao.pack(pady=0)

    input_descricao = tk.Entry(nova_janela)
    input_descricao.pack(pady=5)

    # Label e Input do preco
    label_preco = tk.Label(nova_janela, text="Autor")
    label_preco.pack(pady=0)

    input_preco = tk.Entry(nova_janela)
    input_preco.pack(pady=5)

    # Label e Input do Cod Barras
    label_cod_barras = tk.Label(nova_janela, text="Ano de Publicação")
    label_cod_barras.pack(pady=0)

    input_cod_barras = tk.Entry(nova_janela)
    input_cod_barras.pack(pady=5)

    # Label e Input Id Categoria
    label_id_categoria = tk.Label(nova_janela, text="Categoria")
    label_id_categoria.pack(pady=0)

    input_id_categoria = tk.Entry(nova_janela)
    input_id_categoria.pack(pady=5)

    # Botao que vai cadastrar o produto no banco de dados
    btn_cadastra_produto = tk.Button(nova_janela, text="Cadastrar", command=lambda:salva_produto())

    btn_cadastra_produto.pack(pady=10)

def tela_principal():
    root = tk.Tk()
    root.title("Biblioteca")
    root.geometry("600x600")
    
    btn_abrir_janela_listagem_produtos = tk.Button(root, text="Abrir lista de livros", command=abrir_janela_lista_produtos)
    btn_abrir_janela_listagem_produtos.pack(pady=10)

    btn_abrir_janela_cadastro_produto = tk.Button(root, text="Cadastrar Produto", command=abrir_janela_cadastro_produto)
    btn_abrir_janela_cadastro_produto.pack(pady=10)
 
    root.mainloop()