
from datetime import date

from configuracion import Session
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)

# Abrir una sesión para trabajar con la base de datos
sesion = Session()

try:
    # Evitar insertar los mismos datos si ejecutamos el archivo otra vez
    if sesion.query(Clinica).first() is not None:
        print("La base de datos ya contiene información.")
    else:

        # CLINICA 1
        clinica1 = Clinica(
            nombre="Veterinaria San Francisco",
            direccion="Av. Amazonas y Naciones Unidas",
            veterinario_responsable="Ana Torres",
            consultorios=[
                Consultorio(
                    nombre_numero="Consultorio 1",
                    especialidad="Medicina general",
                    veterinarios=[
                        Veterinario(
                            nombres="Ana",
                            apellidos="Torres",
                            correo="ana@veterinaria.com",
                            licencia_profesional="VET-001",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=date(2026, 10, 5),
                                    diagnostico="Gastritis",
                                    tratamiento="Dieta especial y medicación",
                                    nombre_mascota="Max"
                                ),
                                HistoriaClinica(
                                    fecha_atencion=date(2026, 10, 8),
                                    diagnostico="Infección intestinal",
                                    tratamiento="Antibióticos y reposo",
                                    nombre_mascota="Luna"
                                )
                            ]
                        )
                    ]
                ),
                Consultorio(
                    nombre_numero="Consultorio 2",
                    especialidad="Cirugía",
                    veterinarios=[
                        Veterinario(
                            nombres="Luis",
                            apellidos="Mendoza",
                            correo="luis@veterinaria.com",
                            licencia_profesional="VET-002",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=date(2026, 10, 10),
                                    diagnostico="Fractura de pata",
                                    tratamiento="Cirugía y rehabilitación",
                                    nombre_mascota="Rocky"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        # CLINICA 2
        clinica2 = Clinica(
            nombre="Clínica Veterinaria Patitas",
            direccion="Av. 9 de Octubre",
            veterinario_responsable="María López",
            consultorios=[
                Consultorio(
                    nombre_numero="Consultorio 1",
                    especialidad="Medicina felina",
                    veterinarios=[
                        Veterinario(
                            nombres="María",
                            apellidos="López",
                            correo="maria@patitas.com",
                            licencia_profesional="VET-003",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=date(2026, 10, 12),
                                    diagnostico="Infección respiratoria",
                                    tratamiento="Medicamento y control",
                                    nombre_mascota="Michi"
                                ),
                                HistoriaClinica(
                                    fecha_atencion=date(2026, 10, 15),
                                    diagnostico="Conjuntivitis",
                                    tratamiento="Gotas oftálmicas",
                                    nombre_mascota="Nube"
                                )
                            ]
                        )
                    ]
                ),
                Consultorio(
                    nombre_numero="Consultorio 2",
                    especialidad="Medicina canina",
                    veterinarios=[
                        Veterinario(
                            nombres="Carlos",
                            apellidos="Vera",
                            correo="carlos@patitas.com",
                            licencia_profesional="VET-004",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=date(2026, 10, 18),
                                    diagnostico="Dermatitis",
                                    tratamiento="Champú medicado",
                                    nombre_mascota="Toby"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        # CLINICA 3
        clinica3 = Clinica(
            nombre="Veterinaria Huellitas",
            direccion="Calle Los Ceibos",
            veterinario_responsable="Sofía Ramírez",
            consultorios=[
                Consultorio(
                    nombre_numero="Consultorio 1",
                    especialidad="Medicina preventiva",
                    veterinarios=[
                        Veterinario(
                            nombres="Sofía",
                            apellidos="Ramírez",
                            correo="sofia@huellitas.com",
                            licencia_profesional="VET-005",
                            historias_clinicas=[]
                        )
                    ]
                )
            ]
        )

        # Agregar las clínicas y sus datos relacionados
        sesion.add_all([clinica1, clinica2, clinica3])

        # Guardar los cambios en la base de datos
        sesion.commit()

        print("Los datos se insertaron correctamente.")

except Exception as error:
    sesion.rollback()
    print("Ocurrió un error:", error)

finally:
    sesion.close()
