import csps
import time

"""
class Crucigrama(csps.ProblemaCSP):
    def __init__(self, pos_ini):

        self.X = #
        self.D = # TODO: definir el dominio de cada variable
        self.N = # TODO: definir el conjunto de vecinos de cada variable
        

    def restriccion_binaria(self, xi, vi, xj, vj):
        # TODO: definir la función de restricción binaria entre las variables xi y xj
        pass
    
def prueba_crucigrama(verticales, horizontales, consistencia=1):
    pos_ini = {
        "verticales": verticales,
        "horizontales": horizontales
    }
    programa = Crucigrama(pos_ini)
    t0 = time.time()
    asig =csps.asignacion_completa(problema, consistencia=consistencia)
    t_lapso=time.time() - t0

    print(asig)
    print("Backtracking con consistencia {}: {} segundos".format(consistencia, t_lapso))

if __name__ == "__main__":
    
    prueba_crucigrama(...) # TODO: definir los crucigramas a probar

   """"      
