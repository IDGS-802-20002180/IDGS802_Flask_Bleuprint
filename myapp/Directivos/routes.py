
from flask import Blueprint
#Definimos el nombre que tendran nuestros decoradores
dir=Blueprint('dir',__name__)

@dir.route('/getDir',methods=["GET"])
def getdir():
    return {'key':'Directivos'}