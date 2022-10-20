from flask import render_template, redirect, session, request
from flask_app import app

from flask_app.models.users import User
from flask_app.models.recipes import Recipe

@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session: #Con esto estamos comprobando que se inicia sesión
        return redirect('/')

    #En está sesión tengo el id de mi usuario (session['user_id'])
    #Requiero una función que con ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Aquí recibo la instancia de usuario en base a su id

    return render_template('new_recipe.html', user=user) #Aquí me retorna a html new_recipe

@app.route('/create/recipe', methods=['POST']) #con esto estoy creando una función para crear una receta 
def create_recipe():
    if 'user_id' not in session: 
        return redirect('/') #Aquí me retorna al home
    
    #Se valida la de Receta
    if not Recipe.valida_receta(request.form):
        return redirect('/new/recipe')
    
    #Se guarda la receta
    Recipe.save(request.form)

    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>') #Aquí estoy editando una receta
def edit_recipe(id):
    if 'user_id' not in session: #Comprobamos que inicia sesión
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    #la instancia de la receta que se debe desplegar en editar - en base al ID que recibimos en URL
    formulario_receta = {"id": id}
    recipe = Recipe.get_by_id(formulario_receta)

    return render_template('edit_recipe.html', user=user, recipe=recipe)


@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    if 'user_id' not in session: #Comprobamos que inicia sesión
        return redirect('/')

    #recibimos formulario = request.form 
    #request.form = {name: "Albondigas", description:"123"....... recipe_id:1}

    #Verificar que todos los datos esten correctos
    if not Recipe.valida_receta(request.form):
        return redirect('/edit/recipe/'+request.form['recipe_id']) #/edit/recipe/1

    
    Recipe.update(request.form) #Con esto guardo los cambios

    return redirect('/dashboard') #Me redirecciona a /dashboard

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    #Verificar que haya iniciado sesion
    if 'user_id' not in session: #Comprobamos que inicia sesión
        return redirect('/')

    
    formulario = {"id": id} #Con esto borramos 
    Recipe.delete(formulario)

    return redirect('/dashboard') #Redirigir a /dashboard

@app.route('/view/recipe/<int:id>')
def view_recipe(id):
    #Verificar que el usuario haya iniciado sesión
    if 'user_id' not in session: #Comprobamos que inicia sesión
        return redirect('/')

    #Saber cuál es el nombre del usuario que inicio sesión
    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    #Este es el objeto receta que queremos desplegar
    formulario_receta = {"id": id}
    recipe = Recipe.get_by_id(formulario_receta)

    #Aquí renderizar show_recipe.html
    return render_template('show_recipe.html', user=user, recipe=recipe)