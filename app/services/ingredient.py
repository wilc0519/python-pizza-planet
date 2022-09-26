from datetime import datetime
from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from .baseProxy import proxy_entity

from ..controllers import IngredientController
from .base import create, update, get_by_id, get_all

ingredient = Blueprint('ingredient', __name__)

@ingredient.before_request
def proxy_ingredient():
    proxy_entity()

@ingredient.route('/', methods=POST)
def create_ingredient():
    return create(IngredientController)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return update(IngredientController)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return get_by_id(IngredientController, _id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return get_all(IngredientController)
