from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
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

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = {'@', '_', '#', '$', '%'}
        return any(char in especiales for char in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise ValueError("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise ValueError("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise ValueError("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise ValueError("La clave debe contener al menos un caracter especial (@, _, #, $, %)")

        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = sum(1 for char in clave if char.isupper())
        total_letras = len(clave)
        return mayusculas >= 2 and mayusculas < total_letras


    def es_valida(self, clave: str) -> bool:
       if not self._validar_longitud(clave):
           raise ValueError("ReglaValidacionCalisto: La clave debe tener una longitud de más de 6 caracteres.")
       if not self._contiene_numero(clave):
           raise ValueError("ReglaValidacionCalisto: La clave debe contener al menos un número.")
       if not self.contiene_calisto(clave):
           raise ValueError("ReglaValidacionCalisto: La palabra calisto debe estar escrita con al menos dos letras en mayúscula.")
       return True









