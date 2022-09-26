from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from .baseProxy import proxy_entity
from ..controllers import SizeController
from .base import create, update, get_by_id, get_all

size = Blueprint('size', __name__)

@size.before_request
def proxy_size():
    proxy_entity()

@size.route('/', methods=POST)
def create_size():
    return create(SizeController)


@size.route('/', methods=PUT)
def update_size():
    return update(SizeController)


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return get_by_id(SizeController, _id)


@size.route('/', methods=GET)
def get_sizes():
    return get_all(SizeController)

