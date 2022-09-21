from flask import  jsonify, request

def create(EntityController): 
    entity, error = EntityController.create(request.json)
    response = entity if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


def update(EntityController):
    entity, error = EntityController.update(request.json)
    response = entity if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


def get_by_id(EntityController,_id: int):
    entity, error = EntityController.get_by_id(_id)
    response = entity if not error else {'error': error}
    status_code = 200 if entity else 404 if not error else 400
    return jsonify(response), status_code


def get_all(EntityController):
    entities, error = EntityController.get_all()
    response = entities if not error else {'error': error}
    status_code = 200 if entities else 404 if not error else 400
    return jsonify(response), status_code