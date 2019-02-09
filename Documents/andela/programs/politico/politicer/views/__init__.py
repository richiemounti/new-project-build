from flask import request, make_response, jsonify
from politicer.models.party_models import parties
from politicer.models.office_models import offices

class Views(object):
        
    @staticmethod
    def get_data():

        data = request.get_json()
        return data
    '''
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        if not data:
            try:
                data = request.get_json(force=True)  
            except:
                data = dict() 
    '''
    @staticmethod
    def destroy_lists():
        parties.clear()
        offices.clear()
        return make_response(jsonify({"message":"Done", "status" : 200}))

    
    