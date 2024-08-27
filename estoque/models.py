from sqlalchemy import Column, Integer, String, Sequence, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from estoque import Base


class Nota(Base):
    __tablename__= 'nota'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    fornecedor = Column(String, nullable=False)
    numero_nota = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)


class ItensNota(Base):
    __tablename__ = 'itens_nota'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    codigo_produto = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    codigo_nota = Column(Integer, ForeignKey('nota.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)


class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    grupo = Column(String, nullable=True)
    quantidade_estoque = Column(Integer, nullable=False)
    # valor_medio = Column(Float, nullable=False)
    

class Contagem(Base):
    __tablename__='contagem'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    diferenca = Column(Integer, nullable=False)
    codigo_produto = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    data = Column(Date, nullable=False)
    
    
# class Saida(Base):
    