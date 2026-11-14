
from configuracion import Session
from crear_base_entidades import Veterinario

sesion = Session()

try:
    resultados = sesion.query(Veterinario).filter(
        Veterinario.nombres == "Ana"
    ).all()

    print("VETERINARIOS CON EL NOMBRE ANA")
    print("--------------------------------")

    for veterinario in resultados:
        print(
            f"Nombre: {veterinario.nombres} "
            f"{veterinario.apellidos}"
        )
        print(f"Correo: {veterinario.correo}")

finally:
    sesion.close()
