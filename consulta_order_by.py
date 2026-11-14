
from configuracion import Session
from crear_base_entidades import Consultorio

sesion = Session()

try:
    resultados = sesion.query(Consultorio).order_by(
        Consultorio.especialidad
    ).all()

    print("CONSULTORIOS ORDENADOS POR ESPECIALIDAD")
    print("----------------------------------------")

    for consultorio in resultados:
        print(f"Consultorio: {consultorio.nombre_numero}")
        print(f"Especialidad: {consultorio.especialidad}")
        print("----------------------------------------")

finally:
    sesion.close()
