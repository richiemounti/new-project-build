import copy

from flask import (
    Blueprint, request, jsonify, make_response
)


bp = Blueprint('office', __name__)

from politicer.views import Views
from politicer.models.office_models import Office, offices, officeTypes

# create a office
@bp.route('/v1/admin/office', methods=['POST'])
def create_office():
    data = Views.get_data()

    new_office = Office (
        data["name"],
        data["type"]
    )
    
    new_office.save_office()
    details = new_office.office_list()

    res = jsonify({"status": 201, "data": details})
    return make_response(res, 201)


# get all offices
@bp.route('/v1/user/office', methods=['GET'])
def offices_list():
    return make_response(jsonify({
        "status": 200,
        "data": [offices[x].serialize() for x in offices]
    }), 200)



# get specific office  #
@bp.route('/v1/user/office/<int:x>', methods=['GET'])
def office_details(x):
    office = get_offices(x)
    print(office)
    if office:
        return make_response(jsonify(
            {'status':200, 'data':office.office_list()}
        ), 200)
    
    return make_response(jsonify(
        {'status':404, "error":'Office with id {} not found'.format(x)}
    ))

def get_offices(x):
        if x in offices:
            return offices[x]
        return False

# update a specific office
@bp.route('/v1/admin/office/<int:x>', methods=['PATCH'])
def office_update(x):
    data = Views.get_data()

    if x in offices:
        offices[x].update_name(data['name'], data['type'])
        res = jsonify({"status": 202, "data": offices[x].office_list()})
        return make_response(res, 202)
    res = jsonify({"status": 404, "error": "office with id {} not found".format(x)})
    return make_response(res, 404)

