#la clase base de las clases modelos
#los modelos o clases modelo son las clases que mapean a las tablas
from orm.config import BaseClass 
#Debemos importar SQLAlchemy los tipos de datos que usan las columnas de las tablas 
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
import datetime #para calcular la fecha/hora actual del servidor


#por convencion las clases tienen nombres en singular y comienzan con mayusculas
class Usuario(BaseClass):
    __tablename__="usuarios" #Nombre de la tabla en la bd
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(150))
    email=Column(String(150))
    password=Column(String(40))
    fecha_registro=Column(DateTime(timezone=True), default=datetime.datetime.now)

#Modelos implementados
class Compra(BaseClass):
    __tablename__="compras"
    id=Column(Integer, primary_key=True)
    id_usuario=Column(Integer, ForeignKey(Usuario.id))
    producto=Column(String(150))
    precio=Column(Float(150))

class Foto(BaseClass):
    __tablename__="fotos"
    id=Column(Integer, primary_key=True)
    id_usuario=Column(Integer, ForeignKey(Usuario.id))
    titulo=Column(String(100))
    descripcion=Column(String(150))
    ruta=Column(String(100))


