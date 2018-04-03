#pip install flask
#pip install sqlalchemy
#pip install mysqlclient

from flask import Flask, json, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from flask_marshmallow import marshmallow
from marshmallow_sqlalchemy import ModelSchema
from tactic import Category, CategorySchema, Tactic, TacticSchema
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
session = sessionmaker()
session.configure(bind=engine)
s = session()

@app.route("/")
def hello():
    #return list of possible calls?
    return "nvapi"

@app.route("/cat")
def cat():
    return category.name

@app.route("/categories")
def categories():
    #print("# of categories")
    allCategories = s.query(Category).all()
    #print(len(allCategories))
    categorySchema = CategorySchema(many=True)
    dump_data = categorySchema.dump(allCategories)
    #print(dump_data)
    return jsonify(dump_data)

@app.route("/category_hierarchy")
def categories():
    return jsonify("Not Yet Implemented")

#TODO: implement query string search filter arguments
#      1) list of categories
#      2) Whole word search (requires full-text index in db)
#TODO: build adhoc query based on search arguments
@app.route("/tactics")
def tactics():
    allTactics = s.query(Tactic).all()
    print(allTactics[0].categories[0].name)
    tacticSchema = TacticSchema(many=True)
    dump_data = tacticSchema.dump(allTactics)
    return jsonify(dump_data)


if __name__ == "__main__":
    app.run()
