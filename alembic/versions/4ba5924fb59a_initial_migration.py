"""Initial migration

Revision ID: 4ba5924fb59a
Revises: 
Create Date: 2024-07-30 12:27:15.630333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ba5924fb59a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nota',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fornecedor', sa.String(), nullable=False),
    sa.Column('numero_nota', sa.String(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('grupo', sa.String(), nullable=True),
    sa.Column('quantidade_estoque', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contagem',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('diferenca', sa.Integer(), nullable=False),
    sa.Column('codigo_produto', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['codigo_produto'], ['produtos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itens_nota',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('codigo_produto', sa.Integer(), nullable=False),
    sa.Column('codigo_nota', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['codigo_nota'], ['nota.id'], ),
    sa.ForeignKeyConstraint(['codigo_produto'], ['produtos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('itens_nota')
    op.drop_table('contagem')
    op.drop_table('produtos')
    op.drop_table('nota')
    # ### end Alembic commands ###