
from sqlalchemy import or_

from configuracion import Session
from crear_base_entidades import Clinica

sesion = Session()

try:
    resultados = sesion.query(Clinica).filter(
        or_(
            Clinica.nombre == "Veterinaria San Francisco",
            Clinica.nombre == "Veterinaria Huellitas"
        )
    ).all()

    print("CLINICAS QUE CUMPLEN UNA DE LAS CONDICIONES")
    print("--------------------------------------------")

    for clinica in resultados:
        print(f"Nombre: {clinica.nombre}")
        print(f"Direccion: {clinica.direccion}")
        print(f"Veterinario responsable: {clinica.veterinario_responsable}")
        print("--------------------------------------------")

finally:
    sesion.close()
