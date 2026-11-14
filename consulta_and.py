
from sqlalchemy import and_

from configuracion import Session
from crear_base_entidades import HistoriaClinica

sesion = Session()

try:
    resultados = sesion.query(HistoriaClinica).filter(
        and_(
            HistoriaClinica.diagnostico == "Gastritis",
            HistoriaClinica.tratamiento == "Dieta especial y medicación"
        )
    ).all()

    print("HISTORIAS CLINICAS QUE CUMPLEN AMBAS CONDICIONES")
    print("------------------------------------------------")

    for historia in resultados:
        print(f"Mascota: {historia.nombre_mascota}")
        print(f"Fecha de atención: {historia.fecha_atencion}")
        print(f"Diagnóstico: {historia.diagnostico}")
        print(f"Tratamiento: {historia.tratamiento}")
        print("------------------------------------------------")

finally:
    sesion.close()
