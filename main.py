from estoque import Base, engine, session
from estoque.models import *
from datetime import date, datetime
import flet as ft 



def get_product():
    options=[]
    for product in session.query(Produtos).all():
        name = product.nome
        id = product.id
        option = ft.dropdown.Option(text=name,
                           key=id)
        options.append(option)
    return options


def main(page: ft.Page):
    page.title = "Programa Estoque"
    
    produto = ft.TextField(label="Digite o nome do produto", text_align=ft.TextAlign.LEFT)
    group = ft.TextField(label="Digite o grupo do produto", text_align=ft.TextAlign.LEFT)
    quantidade = ft.TextField(value="0", label="Digite a quantidade em estoque do produto:", text_align=ft.TextAlign.LEFT)
    produtos_cadastrados = ft.Dropdown(
        width=100,
        options=get_product()
    )
    lista_produtos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nome do Produto")),
            ft.DataColumn(ft.Text("Grupo do Produto")),
            ft.DataColumn(ft.Text("Quantidade em Estoque")),
        ]
    )
    
    def cadastrar(event):
        novo_produto = Produtos(nome=produto.value, grupo=group.value, quantidade_estoque=quantidade.value)
        session.add(novo_produto)
        session.commit()
        
        lista_produtos.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(novo_produto.id))),
                    ft.DataCell(ft.Text(novo_produto.nome)),
                    ft.DataCell(ft.Text(str(novo_produto.quantidade_estoque))),
                ]
            )
        )
        
        page.update()
        print('Produto salvo com sucesso')
    
    for product in session.query(Produtos).all():
        lista_produtos.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(product.id))),
                    ft.DataCell(ft.Text(product.nome)),
                    ft.DataCell(ft.Text(str(product.grupo))),
                    ft.DataCell(ft.Text(str(product.quantidade_estoque))),
                ]
            )
        )
    
    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        anchor.open_view()

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.RED,
        bar_hint_text="Search colors...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            for i in range(10)
        ],
    )
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Home",
                content=ft.Container(
                    content=ft.Text("Bem vindo ao programa de Controle de Estoque"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Cadastro",
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Nome do produto:"), 
                            produto,
                            ft.Text("Grupo do produto:"),
                            group,
                            ft.Text("Quantidade em estoque"),
                            quantidade,
                            ft.ElevatedButton("Cadastrar", on_click=cadastrar),
                        ],
                    ),
                ),
            ),
            ft.Tab(
                text="Listagem Produtos",
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Listagem de Produtos"),
                            lista_produtos,
                        ],
                    ),
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 3"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 4"),
            ),
            ft.Tab(
                text="Saida",
                content=ft.Container(
                    content=ft.Column(
                        [   
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.OutlinedButton(
                                        "Open Search View",
                                        on_click=lambda _: anchor.open_view(),
                                    ),
                                ],
                            ),
                            anchor,
                            # ft.Text("Quantidade"),
                            # quantidade,
                            # ft.ElevatedButton("Cadastrar", on_click=cadastrar),
                            # produtos_cadastrados,
                        ],
                    ),
                ),
            ),
        ],
        expand=1,
    )
        
    page.add(t)
    # txt_produto = ft.Text("Titulo do produto:")
    # produto = ft.TextField(label="Digite o titulo do produto...", text_align=ft.TextAlign.LEFT)
    # txt_quantidade = ft.Text("Quantidade em estoque")
    # quantidade = ft.TextField(value="0", label="Digite a quantidade em estoque do produto:", text_align=ft.TextAlign.LEFT)
    # btn_produto = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    
    # page.add(
    #     txt_produto,
    #     produto,
    #     txt_quantidade,
    #     quantidade,
    #     btn_produto
    # )

ft.app(target=main)

# Base.metadata.create_all(engine)

# nova_nota = Nota(fornecedor='Atacadao', numero_nota=25356, valor=25.00, data=15/10/2024)
# session.add(nova_nota)

# novo_prod = Produtos(nome='Leite', quantidade_estoque=5)
# session.add(novo_prod)
# session.commit()



# nova_contagem = Contagem(diferenca=3, codigo_produto=novo_prod.id, data=datetime.now())
# session.add(nova_contagem)
# session.commit()


# nova_nota = Nota(fornecedor='Atacadao', numero_nota='234431', valor=25.00, data=datetime.now())
# session.add(
    # nova_nota)
# session.commit()

# produtoss = session.query(Produtos.nome, Produtos.id).first()
# print(produtoss)

# novo_produto = Produtos(nome='Café', quantidade_estoque=3)
# nova_nota = Nota(fornecedor='SMH', numero_nota='55762', valor=32.00, data=datetime.now())
# session.add_all([novo_produto, nova_nota])
# session.commit()

# nova_nota = Nota(fornecedor='BBH', numero_nota='322', valor=8.00, data=date(2024, 5, 21))
# session.add(nova_nota)
# session.commit()