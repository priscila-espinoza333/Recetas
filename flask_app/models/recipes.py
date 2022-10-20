from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #LEFT JOIN  
        self.first_name = data['first_name']