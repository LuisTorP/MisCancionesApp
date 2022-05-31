from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import engine, Base, session

class Coleccion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_album(self, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo).all()
        if len(busqueda) == 0:
            album = Album(titulo=titulo, ano=anio, descripcion=descripcion, medio=medio)
            session.add(album)
            session.commit()
            return True
        else:
            return False

    def editar_album(self, album_id, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo, Album.id != album_id).all()
        if len(busqueda) == 0:
            album = session.query(Album).filter(Album.id == album_id).first()
            album.titulo = titulo
            album.ano = anio
            album.descripcion = descripcion
            album.medio = medio
            session.commit()
            return True
        else:
            return False

    def dar_album_por_id(self, album_id):
        return session.query(Album).get(album_id).__dict__

if __name__ == '__main__':
    # Crea la BD
    Base.metadata.create_all(engine)

    coleccion =Coleccion()
    if coleccion.agregar_album("new weave", 2021, "Album original", Medio.DISCO):
        print(f'Se añadio el nuevo registro')
    else:
        print(f'Ya existe el titulo, no se añadio el registro')
    #editar_album(self, album_id, titulo, anio, descripcion, medio)#
    if coleccion.editar_album(1, "chicha", 2022, "Primicia", Medio.CASETE):
        print(f'Se actualizo el nuevo registro')
    else:
        print(f'Ya existe el titulo, no se actualizo el registro')
