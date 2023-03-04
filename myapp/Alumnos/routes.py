
from flask import Blueprint
#Definimos el nombre que tendran nuestros decoradores
alumnos=Blueprint('alumnos',__name__)

@alumnos.route('/getAlum',methods=["GET"])
def getalum():
    return {'key':'Alumnos'}
