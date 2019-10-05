from flask import render_template, url_for, escape
from app import application
import os
import json

with open("content.json") as f:
    CONTENT = json.load(f)

for i, recipe in enumerate(CONTENT['recipes']):
    recipe['slug'] = str(i)

@application.route('/index.html')
@application.route('/')
def index():
    return render_template('index.html', recipes = CONTENT["recipes"])

@application.route('/<slug>/')
def get_recipe(slug):
    for recipe in CONTENT["recipes"]:
        if recipe["slug"] == slug:
            return render_template('recipe.html', recipe = recipe)