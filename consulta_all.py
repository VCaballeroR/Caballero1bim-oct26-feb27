
from sqlalchemy import func

from configuracion import Session
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)

sesion = Session()

try:
    resultados = (
        sesion.query(
            Clinica.nombre,
            func.count(HistoriaClinica.id).label("total_historias")
        )
        .outerjoin(Consultorio, Clinica.id == Consultorio.clinica_id)
        .outerjoin(Veterinario, Consultorio.id == Veterinario.consultorio_id)
        .outerjoin(HistoriaClinica, Veterinario.id == HistoriaClinica.veterinario_id)
        .group_by(Clinica.id, Clinica.nombre)
        .all()
    )

    print("CLINICAS Y NUMERO DE HISTORIAS CLINICAS")
    print("----------------------------------------")

    for nombre, total in resultados:
        print(f"Clinica: {nombre} | Historias clinicas: {total}")

finally:
    sesion.close()
