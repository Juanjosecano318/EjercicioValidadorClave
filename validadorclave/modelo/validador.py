# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def _init_(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        """Método abstracto que debe ser implementado por las subclases para verificar la validez de la clave"""
        pass

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada


    def _contiene_mayuscula(self, clave: str) -> bool:
        for c in clave:
            if c.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for c in clave:
            if c.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for c in clave:
            if c.isdigit():
                return True
        return False




