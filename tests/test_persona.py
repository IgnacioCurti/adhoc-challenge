import pytest
from models.persona import Persona


def test_crea_persona_valida():
    p = Persona("41942661", "Ignacio", "Curti", 26)
    assert p.dni == "41942661"
    assert p.edad == 26


def test_persona_es_inmutable():
    p = Persona("44123456", "Martín", "Rodríguez", 24)
    with pytest.raises(Exception):  
        p.edad = 30


def test_edad_negativa():
    with pytest.raises(ValueError):
        Persona("11111111", "Pedro", "Paez", -1)
