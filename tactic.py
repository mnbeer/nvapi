from sqlalchemy import Column, Table, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

Base = declarative_base()

tacticCategories = Table('tactic_categories', Base.metadata,
    Column('tactic_id', Integer, ForeignKey('tactics.tactic_id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.category_id'), primary_key=True)
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

class TacticLink(Base):
    __tablename__ = 'tactic_links'
    tactic_link_id = Column(Integer, primary_key=True)
    tactic_id = Column(Integer, ForeignKey('tactics.tactic_id'))
    tactic = relationship("Tactic", back_populates="links")
    url = Column(String(1000), nullable=False)
    sort_order = Column(Integer, nullable=False)

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
                    secondary=tacticCategories)
    links = relationship("TacticLink", back_populates="tactic")

class TacticLinkSchema(ModelSchema)
    tactic = fields.Integer(load_only=True)
    class Meta:
        model = TacticLink

class TacticSchema(ModelSchema):
    categories = fields.Nested(CategorySchema, many=True)
    links = fields.Nested(TacticLinkSchema, many=True)
    #TODO: return links order by sort_order (no hurry; currently just 1 link per tacktic)
    class Meta:
        model = Tactic
