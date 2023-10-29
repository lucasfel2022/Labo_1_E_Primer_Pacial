import Estadisticas

class Jugador():
    def __init__(self,dict:list) -> None:
        self.nombre = dict.get("nombre")
        self.logros = dict.get("logros")
        self.posicion = dict.get("posicion")
        self.estadisticas = Estadisticas(Jugador.get("estadisticas"))