#import os
#import sys
from sqlalchemy import Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine
from marshmallow_sqlalchemy import ModelSchema

Base = declarative_base()

tacticCategories = Table('tactic_categories', Base.metadata,
    Column('tactic_id', Integer, ForeignKey('tactics.tactic_id')),
    Column('category_id', Integer, ForeignKey('categories.category_id'))
)

class Category(Base):
    __tablename__ = 'categories'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    category_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000))


class CategorySchema(ModelSchema):
    class Meta:
        model = Category

class Tactic(Base):
    __tablename__ = 'tactics'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    tactic_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    gene_sharp_number = Column(Integer)
    gene_sharp_sub = Column(String(5))
    categories = relationship("Category",
                    secondary=tacticCategories,
                    backref="parents")

class TacticSchema(ModelSchema):
    class Meta:
        model = Tactic
