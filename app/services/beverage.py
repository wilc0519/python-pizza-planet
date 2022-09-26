from datetime import datetime
from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from .base import create, get_all, update, get_by_id
from .baseProxy import proxy_entity

beverage = Blueprint('beverage', __name__)

@beverage.before_request
def proxy_beverage():
   proxy_entity()

@beverage.route('/', methods=POST)
def create_beverage():
    return create(BeverageController)
   

@beverage.route('/', methods=PUT)
def update_beverage():
    return update(BeverageController)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
   return get_by_id(BeverageController, _id)


@beverage.route('/', methods=GET)
def get_beverages():
    return get_all(BeverageController)
