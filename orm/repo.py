import orm.modelos as modelos
from sqlalchemy.orm import Session

#Esta funcion es llamada por api.py
#Para atender GET '/usuarios/{id}'
#select * from app.usuarios where id=id_usuario
def usuario_por_id(sesion:Session, id_Usuario:int):
    print("select * from app.usuarios where id=",id_Usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_Usuario).first()

#Select * from compras
#definicion de compra y foto
def compra_por_id(sesion:Session, id_Compra:int):
    print("Select * from compra where id= ", id_Compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_Compra).first()


def foto_por_id(sesion:Session, id_Foto:int):
    print("Select * from fotos where id= ", id_Foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_Foto).first()



