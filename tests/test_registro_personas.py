import pytest
from models.registroPersona import RegistroPersonas


@pytest.fixture
def registros_base():
    return [
        ("20456132", "Martín", "Rodriguez", 40),
        ("30522552", "Ana", "González", 31),
        ("40404040", "Marcos", "Diaz", 17),
    ]


def test_dni_duplicado_lanza_error(registros_base):
    duplicado = registros_base + [("40404040", "Otro", "Nombre", 20)]
    with pytest.raises(ValueError):
        RegistroPersonas(duplicado)


def test_obtener_extremos_de_edad(registros_base):
    registro = RegistroPersonas(registros_base)
    mayor, menor = registro.obtener_extremos_de_edad()
    assert mayor.dni == "20456132"
    assert menor.dni == "40404040"


def test_promedio_de_edad(registros_base):
    registro = RegistroPersonas(registros_base)
    assert registro.obtener_promedio_de_edad() == pytest.approx((40 + 31 + 17) / 3)


def test_segmentar_poblacion_con_umbral_default(registros_base):
    registro = RegistroPersonas(registros_base)
    resultado = registro.segmentar_poblacion()
    assert resultado["mayores"]["cantidad"] == 2
    assert resultado["menores"]["cantidad"] == 1


def test_segmentar_poblacion_con_umbral_custom(registros_base):
    registro = RegistroPersonas(registros_base)
    resultado = registro.segmentar_poblacion(umbral=30)
    assert resultado["mayores"]["cantidad"] == 2
    assert resultado["menores"]["cantidad"] == 1


def test_obtener_edad_por_dni_existente(registros_base):
    registro = RegistroPersonas(registros_base)
    assert registro.obtener_edad_de_persona_por_dni("30522552") == 31


def test_obtener_edad_por_dni_inexistente(registros_base):
    registro = RegistroPersonas(registros_base)
    assert registro.obtener_edad_de_persona_por_dni("11111111") is None
