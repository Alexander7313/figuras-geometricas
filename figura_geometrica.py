''' Programa para hallar el area de figuras geometricas'''
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):  # pylint: disable=too-few-public-methods
    """Clase abstracta que define la interfaz para calcular áreas."""

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""



class Rectangulo(FiguraGeometrica):
    """Clase que representa la figura geométrica rectángulo."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def __str__(self):
        return f"Rectángulo(base={self.base}, altura={self.altura})"


class Triangulo(FiguraGeometrica):
    """Clase que representa la figura geométrica triángulo."""

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2

    def __str__(self):
        return f"Triángulo(base={self.base}, altura={self.altura})"


class Circulo(FiguraGeometrica):
    """Clase que representa la figura geométrica círculo."""

    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return self.pi * (self.radio ** 2)

    def __str__(self):
        return f"Círculo(radio={self.radio})"

# Variables globales
BASE_RECTANGULO =10
ALTURA_RECTANGULO=5
BASE_TRIANGULO=7
ALTURA_TRIANGULO =4
RADIO_CIRCULO =3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO,ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO,ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
