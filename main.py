import argparse
from models.registroPersona import RegistroPersonas
from data import data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u" , "--umbral", type=int, default=25, help="Umbral de edad para segmentación (default: 25)")
    parser.add_argument("-d" , "--dni", type=str, default=None, help="DNI de la persona a consultar")
    args = parser.parse_args()

    registro_personas = RegistroPersonas(data)
    print(f"\nFormateo de registros:")
    print(registro_personas.formatear_registros())

    print(f"\nExtremos de edad:")
    mayor, menor = registro_personas.obtener_extremos_de_edad()
    print(f"MAYOR: DNI: {mayor.dni}. Nombre completo: {mayor.nombre} {mayor.apellido}. Edad: {mayor.edad}")
    print(f"MENOR: DNI: {menor.dni}. Nombre completo: {menor.nombre} {menor.apellido}. Edad: {menor.edad}")

    print(f"\nPromedio de edad:")
    print(registro_personas.obtener_promedio_de_edad())

    print(f"\nSegmentación de registros:")
    poblaciones = registro_personas.segmentar_poblacion(args.umbral)
    print(f"\nMayores de {args.umbral}:")
    print (poblaciones["mayores"]["personas"])
    print(f"\nMetricas de mayores de {args.umbral}:")
    print (f"Tamaño del grupo: {poblaciones["mayores"]["cantidad"]}. Promedio de edad del grupo: {poblaciones["mayores"]["promedio"]}")
    print(f"\nMenores de {args.umbral}:")
    print (poblaciones["menores"]["personas"])
    print(f"\nMetricas de menores de {args.umbral}:")
    print (f"Tamaño del grupo: {poblaciones["menores"]["cantidad"]}. Promedio de edad del grupo: {poblaciones["menores"]["promedio"]}")

    print(f"\nEdad de Persona específica:")
    if args.dni:
        edad = registro_personas.obtener_edad_de_persona_por_dni(args.dni)
        if edad is not None:
            print(f"Edad de persona con DNI {args.dni}: {edad}")
        else:
            print(f"DNI {args.dni} no encontrado")
    else:
        print("No se especificó DNI.")    


if __name__ == "__main__":
    main()
