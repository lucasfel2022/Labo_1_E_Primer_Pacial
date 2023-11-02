from estadisticas import Estadisticas

class Jugador():
    def __init__(self, jugador : dict) -> None:
        self.nombre = jugador.get("nombre")
        self.logros = jugador.get("logros")
        self.posicion = jugador.get("posicion")
        self.estadisticas = Estadisticas(jugador.get("estadisticas"))
        
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def logros(self):
        return self._logros

    @logros.setter
    def logros(self, nuevos_logros):
        self._logros = nuevos_logros

    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, nueva_posicion):
        self._posicion = nueva_posicion

    @property
    def estadisticas(self):
        return self._estadisticas

    @estadisticas.setter
    def estadisticas(self, nuevas_estadisticas):
        self._estadisticas = nuevas_estadisticas
 
    

