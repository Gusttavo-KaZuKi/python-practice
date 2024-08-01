from estoque import Base, engine, session
from estoque.models import *
from datetime import datetime

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
# session.add(nova_nota)
# session.commit()

# produtoss = session.query(Produtos.nome, Produtos.id).first()
# print(produtoss)