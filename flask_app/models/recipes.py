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

    
    @staticmethod
    def valida_receta(formulario):
        es_valido = True

        if len(formulario['name']) < 3:
            flash('El nombre de la receta debe tener al menos 3 caracteres', 'receta')
            es_valido = False
        
        if len(formulario['description']) < 3:
            flash('La descripción de la receta debe tener al menos 3 caracteres', 'receta')
            es_valido = False
        
        if len(formulario['instructions']) < 3:
            flash('Las instrucciones de la receta deben de tener al menos 3 caracteres', 'receta')
            es_valido = False
        
        if formulario['date_made'] == '':
            flash('Ingrese una fecha', 'receta')
            es_valido = False

        return es_valido
    
    @classmethod
    def save(cls, formulario):
        #formulario = {name: "Albondigas", description: "Albondigas de carne", instructions: ".....", date_made:"0000-00-00", under_30: 0, user_id: 1}
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s)"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL('recetas').query_db(query) #Lista de Diccionarios
         #result = [
        #    {id: 1, name: albondigas, description: bolitas de carne....}
        #    {id: 2, name: albondigas, description: bolitas de carne....}
        #    {id: 3, name: albondigas, description: bolitas de carne....}
        #    {id: 4, name: albondigas, description: bolitas de carne....}
        #    {id: 5, name: albondigas, description: bolitas de carne....}
        #]
        recipes = []

        for recipe in results:
            #recipe = diccionario
            recipes.append(cls(recipe)) #1.- cls(recipe) creamos la instancia en base al diccionario, 2.- recipes.append agrego esa instancia a la lista recipes
        
        return recipes

    @classmethod
    def get_by_id(cls, formulario):
        #formulario = {id: 1}
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s ;"
        result = connectToMySQL('recetas').query_db(query, formulario) #Al hacer un select recibimos una lista con UN diccionario dentro
        #result = [
        #    {id: 1, name: albondigas, description: bolitas de carne....}
        #]
        recipe = cls(result[0]) #result[0] = diccionario con todos los datos de la receta; cls() creamos la instancia en base a ese diccionario
        return recipe

    @classmethod
    def update(cls, formulario):
        #formulario = {name: Albondigas, description: bolitas de carne, instructions:......., recipe_id: 1}
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30=%(under_30)s WHERE id=%(recipe_id)s "
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        #formulario = {id: 1}
        query = "DELETE FROM recipes WHERE id = %(id)s"
        result = connectToMySQL('recetas').query_db(query, formulario)
        return result