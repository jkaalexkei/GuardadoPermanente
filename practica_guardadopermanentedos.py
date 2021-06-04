import pickle


class Detergente:

    def __init__(self,nombre,tipo,marca):
        self.tipo = tipo
        self.marca = marca
        self.nombre = nombre

        print("Se creo un articulo con el nombre de: ",self.nombre)
    
    def __str__(self):
        return "{}, {}, {}".format(self.nombre,self.tipo,self.marca)

class ListadeDetergentes:

    listadetergentes = []

    def __init__(self):
        listadodedetergentes = open("archivodetergenteb","ab+")
        listadodedetergentes.seek(0)
        try:
            
            self.listadetergentes = pickle.load(listadodedetergentes)
            print("Se cargo {} registro".format(len(self.listadetergentes)))
        except:
            print("El archivo no se ha creado")
        finally:
            listadodedetergentes.close()
            del(listadodedetergentes)

    def guardarInformacion(self):
        listadodedetergentes = open("archivodetergenteb","wb")
        pickle.dump(self.listadetergentes,listadodedetergentes)
        listadodedetergentes.close()
        del(listadodedetergentes)

    def agregarDetergentes(self,objdetergentes):
        self.listadetergentes.append(objdetergentes)
        self.guardarInformacion()
    

    def mostrarDetergentesAgregados(self):
        
        for elementos in self.listadetergentes:
            print(elementos)


lista = ListadeDetergentes()
d1 = Detergente("suavizante","frescoaroma","suavitel")
lista.agregarDetergentes(d1)
lista.mostrarDetergentesAgregados()


