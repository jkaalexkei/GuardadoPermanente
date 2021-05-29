#GUARDAR INFORMACION PERMANENTE EN FICHEROS EXTERNOS

#SE USARA PARA GUARDAR INFORMACION DE DIFERENTES PROGRAMAS
import pickle#importamos la biblioteca pickle

class Persona: #Creamos la clase persona

    def __init__(self,nombre,genero,edad):#creamos un constructor que recibe por parametros 3 arg
        self.nombre=nombre#asignamos el valor a cada variable
        self.genero = genero
        self.edad = edad
        print("Nombre de la persona", self.nombre)#imprimimos el nombre de la persona
    
    def __str__(self):#este metodo convierte en una cadena de texto la informacion de un objeto
        return "{} {} {}".format(self.nombre,self.genero,self.edad)#esta linea le da un formato al texto


class  ListaPersona:#esta clase se usa para agregar personas a una lista

    persona=[]#lista para ir almacenando las personas

     # ab+ --> significa agregar informacion binaria
    
    def __init__(self):
        listadepersonas = open("ficheroexterno","ab+")
        listadepersonas.seek(0)

        try:
            self.persona = pickle.load(listadepersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.persona)))
            
        except:
            print("El fichero esta vacio")

        finally:
            listadepersonas.close()
            del (listadepersonas)


    def agregarPersona(self,persona):#metodo para agregar persona
        self.persona.append(persona)#agregamos personas a la lista mediante el metodo append()
        self.guardarPersonasenFicheroExterno()
    
    def mostrarPersona(self):#metodo para mostrar la lista de personas agregadas
        for p in self.persona:#este bucle recorre las personas agregadas al objeto listPersona
            print(p)
    
    def guardarPersonasenFicheroExterno(self):
        # wb --> escribir informacion binaria
        Listadepersona=open("ficheroexterno","wb")
        pickle.dump(self.persona,Listadepersona)
        Listadepersona.close()
        del (Listadepersona)
    
    def mostrainfoficheroexterno(self):
        print("la informacion del fichero es la siguiente: ")
        for p in self.persona:
            print(p)
        


miListapersona = ListaPersona()

#Aqui creamos los objetos de tipo persona y los agregamos a la lista mediante el objeto miListapersona

persona = Persona("Pedro","Masculino",15)
miListapersona.agregarPersona(persona)
miListapersona.mostrainfoficheroexterno()




