class Estadisticas():
    def init (self,dict:list)->None:
        self.temporadas= dict.get("temporadas")
        self.puntos_totales = dict.get("puntos_totales")
        self.promedio_puntos_por_partido = dict.get("promedio_puntos_por_partido")
        self.rebotes_totales = dict.get("rebotes_totales")
        self.promedio_rebotes_por_partido = dict.get("promedio_rebotes_por_partido")
        self.asistencias_totales = dict.get("asistencias_totales")
        self.promedio_asistencias_por_partido = dict.get("promedio_asistencias_por_partido")
        self.robos_totales = dict.get("robos_totales ")
        self.bloqueos_totales = dict.get("bloqueos_totales")
        self.porcentaje_tiros_de_campo = dict.get("porcentaje_tiros_de_campo")
        self.porcentaje_tiros_libres = dict.get("porcentaje_tiros_libres")
        self.porcentaje_tiros_triples = dict.get("porcentaje_tiros_triples")