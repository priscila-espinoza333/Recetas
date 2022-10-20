from flask import Flask

#Inicializamos la app 
app = Flask(__name__) 

#Ejecutamos la variable app
app.secret_key = "Llave requete secreta"