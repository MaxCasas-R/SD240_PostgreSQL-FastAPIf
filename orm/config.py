#ELengine permitira configurar la conexion a la bd
from sqlalchemy import create_engine
#El session maker permite hacer consultas
#Por cada consulta se abre y se cierra una sesion, 
from sqlalchemy.orm import sessionmaker #y con esto ya podemos hacer una configuracion de la conexion
#declarative_base, permite definir la clase base para mapear las tablas de la BD
from sqlalchemy.ext.declarative import declarative_base

#1.- Configurar la conexión BD
#Creamos la URL de la BD -> servidorBd://usuario:password@url:puerto/nombreBD
URL_BASE_DATOS = "postgresql://usuario_ejemplo:18112003@localhost:5432/base_ejemplo"
#Conectamos mediante el esquema app 
engine= create_engine (URL_BASE_DATOS, 
                       connect_args={
                           "options": "-csearch_path=app"
                       })

#2. Obtenemos la clase que nos permite crear objetos tipo session
SessionClass = sessionmaker(engine)
#Crear una funcion para obtener objetos de la clase tipo SessionClass
def generador_sesion():
    sesion = SessionClass
    try:
        yield sesion #equivalente a return sesion pero de manera segura
    finally:
        sesion.close()

#3.- Obtenemos la clase base para mapear tablas 
BaseClass = declarative_base()