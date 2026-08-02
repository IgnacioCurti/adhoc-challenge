from typing import Iterable
from .persona import Persona


class RegistroPersonas:
    def __init__(self, registros: list[tuple[str, str, str, int]]):
        self.personas = {}

        for registro in registros:
            if registro[0] in self.personas:
                raise ValueError(f"DNI duplicado. DNI: {registro[0]}")
            else:
                self.personas[registro[0]] = Persona(*registro)


    def formatear_registros(self):
        registros_formateados = []
        for dni in self.personas:
            registros_formateados.append({
                dni: (
                    self.personas[dni].nombre,
                    self.personas[dni].apellido,
                    self.personas[dni].edad
                )
            })
        return registros_formateados


    def obtener_extremos_de_edad(self) -> tuple[Persona, Persona] | None :
        if not self.personas:
            raise ValueError("No hay personas registradas.")
        mayor_edad = max(self.personas.values(), key=lambda x:x.edad)
        menor_edad = min(self.personas.values(), key=lambda x:x.edad)
        return mayor_edad, menor_edad


    @staticmethod
    def calcular_promedio_edad(personas: Iterable[Persona]) -> float | None:
        if not personas:
            return None
        return sum(persona.edad for persona in personas) / len(personas)


    def obtener_promedio_de_edad(self):
        return self.calcular_promedio_edad(self.personas.values())


    def segmentar_poblacion(self, umbral = 25):
        mayores = [persona for persona in self.personas.values() if persona.edad >= umbral]
        menores = [persona for persona in self.personas.values() if persona.edad < umbral]
        return {
            "mayores": {
                "personas": mayores,
                "cantidad": len(mayores),
                "promedio": self.calcular_promedio_edad(mayores)
            },
            "menores" : {
                "personas": menores,
                "cantidad": len(menores),
                "promedio": self.calcular_promedio_edad(menores)
            }
        }

    def obtener_edad_de_persona_por_dni(self, dni: str) -> int | None:
        persona = self.personas.get(dni)
        return persona.edad if persona else None
