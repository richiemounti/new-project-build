from flask import request
from politicer.models.party_models import parties


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

    
    