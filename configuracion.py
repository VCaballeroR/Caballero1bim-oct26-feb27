
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de la base de datos SQLite
URL_BASE_DATOS = "sqlite:///clinicas_veterinarias.db"

# Crear la conexión con la base de datos
engine = create_engine(URL_BASE_DATOS, echo=False)

# Crear la clase base para las entidades
Base = declarative_base()

# Crear la sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
