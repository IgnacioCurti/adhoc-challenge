from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:
    dni: str
    nombre: str
    apellido: str
    edad: int

    def __post_init__(self):
        if self.edad < 0:
            raise ValueError("La edad no puede ser negativa")
