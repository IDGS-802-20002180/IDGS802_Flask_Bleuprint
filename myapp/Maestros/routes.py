
from flask import Blueprint
#Definimos el nombre que tendran nuestros decoradores
maestros=Blueprint('maestros',__name__)

@maestros.route('/getmaes',methods=["GET"])
def getmaes():
    return {'key':'Maestros'}