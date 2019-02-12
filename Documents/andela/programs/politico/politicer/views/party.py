import copy

from flask import (
    Blueprint, request, jsonify, make_response, abort
)


bp = Blueprint('party', __name__)

from politicer.views import Views
from politicer.models.party_models import Party, parties

# create a party
@bp.route('/v1/admin/party', methods=['POST'])
def create_party():
    data = Views.get_data()
   
    validateparty(data)

    new_party = Party (
        data["name"],
        data["hqAddress"],
        data["logoUrl"]
    )   

    new_party.save_party()
    details = new_party.detail_list()

    res = jsonify({"status": 201, "data": details})
    return make_response(res, 201)



# get all parties
@bp.route('/v1/user/party', methods=['GET'])
def parties_list():
    return make_response(jsonify({
        "status": 200,
        "data": [parties[x].serialize() for x in parties]
    }), 200)



# get specific party
@bp.route('/v1/user/party/<int:x>', methods=['GET'])
def party_details(x):
    if len(parties) == 0:
        pass
    if x in parties:
        details = parties[x].get_parties()
        res = jsonify({"status": 200, "data": details})
        return make_response(res, 200)

    res = jsonify({"status": 404, "error": "Party with id {} not found".format(x)})
    return (res, 404)

# update a specific party
@bp.route('/v1/admin/party/<int:x>', methods=['PATCH'])
def party_update(x):
    data = Views.get_data()

    if x in parties:
        parties[x].update_name(data['name'], data['hqAddress'])
        res = jsonify({"status": 202, "data": parties[x].detail_list()})
        return make_response(res, 202)

    res = jsonify({"status": 404, "error": "Party with id {} not found".format(x)})
    return (res, 404)

# delete a party
@bp.route('/v1/admin/party/<int:x>', methods=['DELETE'])
def party_delete(x):
    if x in parties:
        parties[x].delete_party()
        res = jsonify({"status": 200, "data": "Party {} deleted".format(x)})
        return (res, 200)


@bp.route('/v1/d')
def parties_delete(x):
    parties[x].delete_parties()
    res = jsonify({"status": 200, "data": "parties deleted"})
    return (res, 200)



'''
VALIDATIONS
'''
def validateparty(new_party):
    '''This function validates new party inputs '''

    for key, value in new_party.items():
        # ensure keys have values
        if not value:
            return abort(make_response(jsonify({"message":"{} is lacking. it is a required field".format(key)})))
        # validate length
        if key == "name" or key == "hqAddress":
            if len(value) < 3:
                return abort(make_response(jsonify({"message":"The {} provided is too short".format(key)}), 400))
            elif len(value) > 20:
                return abort(make_response(jsonify({"message":"The {} provided is too long".format(key)}), 400))

