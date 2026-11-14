
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from configuracion import Base, engine


# ENTIDAD 1: CLINICA
class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(150), nullable=False)

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica"
    )


# ENTIDAD 2: CONSULTORIO
class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_numero = Column(String(50), nullable=False)
    especialidad = Column(String(100), nullable=False)

    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship(
        "Clinica",
        back_populates="consultorios"
    )

    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio"
    )


# ENTIDAD 3: VETERINARIO
class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False)
    licencia_profesional = Column(String(50), unique=True, nullable=False)

    consultorio_id = Column(
        Integer,
        ForeignKey("consultorios.id"),
        nullable=False
    )

    consultorio = relationship(
        "Consultorio",
        back_populates="veterinarios"
    )

    historias_clinicas = relationship(
        "HistoriaClinica",
        back_populates="veterinario"
    )


# ENTIDAD 4: HISTORIA CLINICA
class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(300), nullable=False)
    tratamiento = Column(String(300), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)

    veterinario_id = Column(
        Integer,
        ForeignKey("veterinarios.id"),
        nullable=False
    )

    veterinario = relationship(
        "Veterinario",
        back_populates="historias_clinicas"
    )


# CREAR LAS TABLAS EN LA BASE DE DATOS
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Las tablas se crearon correctamente.")