
class Estadisticas():
    def __init__(self, datos_estadisticos : dict) -> None:

        self.temporadas = datos_estadisticos.get("temporadas")
        self.puntos_totales = datos_estadisticos.get("puntos_totales")
        self.promedio_puntos_por_partido = datos_estadisticos.get("promedio_puntos_por_partido")
        self.rebotes_totales = datos_estadisticos.get("rebotes_totales")
        self.promedio_rebotes_por_partido = datos_estadisticos.get("promedio_rebotes_por_partido")
        self.asistencias_totales = datos_estadisticos.get("asistencias_totales")
        self.promedio_asistencias_por_partido = datos_estadisticos.get("promedio_asistencias_por_partido")
        self.robos_totales = datos_estadisticos.get("robos_totales")
        self.bloqueos_totales = datos_estadisticos.get("bloqueos_totales")
        self.porcentaje_tiros_de_campo = datos_estadisticos.get("porcentaje_tiros_de_campo")
        self.porcentaje_tiros_libres = datos_estadisticos.get("porcentaje_tiros_libres")
        self.porcentaje_tiros_triples = datos_estadisticos.get("porcentaje_tiros_triples")
        self.atributos_estadisticos = list(datos_estadisticos.keys())
        self.datos_estadisticos = list(datos_estadisticos.values())

    @property
    def get_temporadas(self):
        return self.temporadas
    
    @property
    def get_puntos_totales(self):
        return self.puntos_totales
    
    @property
    def get_promedio_puntos_por_partido(self):
        return self.promedio_puntos_por_partido
    
    @property
    def get_rebotes_totales(self):
        return self.rebotes_totales
    
    @property
    def get_promedio_rebotes_por_partido(self):
        return self.promedio_rebotes_por_partido
    
    @property
    def get_asistencias_totales(self):
        return self.asistencias_totales
    
    @property
    def get_promedio_asistencias_por_partido(self):
        return self.promedio_asistencias_por_partido
    
    @property
    def get_robos_totales(self):
        return self.robos_totales
    
    @property
    def get_bloqueos_totales(self):
        return self.bloqueos_totales
    
    @property
    def get_porcentaje_tiros_de_campo(self):
        return self.porcentaje_tiros_de_campo
    
    @property
    def get_porcentaje_tiros_libres(self):
        return self.porcentaje_tiros_libres
    
    @property
    def get_porcentaje_tiros_triples(self):
        return self.porcentaje_tiros_triples
    
    @property
    def get_atributos_estadisticos(self):
        return self.atributos_estadisticos
    
    @property
    def get_datos_estadisticos(self):
        return self.datos_estadisticos