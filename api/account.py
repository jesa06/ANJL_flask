from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.account import Account

Account_api = Blueprint('account_api', __name__,
                    url_prefix='/api/Accounts')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(Account_api)

class AccountAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            email = body.get('email')
            if email is None or len(email) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            phonenumber = body.get('phonenumber')
            password = body.get('password')

            ''' #1: Key code block, setup USER OBJECT '''
            ao = Account(name=name, 
                      email=email)
            ao.phonenumber = phonenumber
            ao.password = password

            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                ao.set_password(password)
            if phonenumber is not None: 
                ao.phonenumber = phonenumber
            # convert to date type            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            Account = ao.create()
            # success returns json of user
            if Account:
                return jsonify(Account.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or email {email} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            accounts = Account.query.all()    # read/extract all users from database
            json_ready = [Account.read() for Account in accounts]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')