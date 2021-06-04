
import pickle

class Detergentes:

    def __init__(self,tipo,marca):
        self.tipo = tipo
        self.marca = marca

    def __str__(self):
        return "{} {}".format(self.tipo,self.marca)


class ListaDetergentes:

    miListadetergentes = []

    def __init__(self):
        
        valoresagregados = open("detergentesbd","ab+")
        valoresagregados.seek(0)
        try:
            self.miListadetergentes = pickle.load(valoresagregados)
            print("Se han cargado {} registros".format(len(self.miListadetergentes)))
        except:
            print("El archivo esta vacio")
        finally:
            valoresagregados.close()
            del (valoresagregados)


    def agregarDetergentes(self,objdetergentes):
        
        self.miListadetergentes.append(objdetergentes)
        self.guardarInformacion()

    def guardarInformacion(self):
        valoresagregados = open("detergentesbd","wb")
        pickle.dump(self.miListadetergentes,valoresagregados)
        valoresagregados.close()
        del (valoresagregados)

    def visualizarDetergentesAgregados(self):
       for elementos in self.miListadetergentes:
           print(elementos)
       


lista = ListaDetergentes()

d1 = Detergentes("cloro","blancox")
lista.agregarDetergentes(d1)
lista.visualizarDetergentesAgregados()
