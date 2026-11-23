import pandas as pd
from dataclasses import dataclass

@dataclass
class Nodo:   


    # edges = pd.read_csv("dataframes/edges.csv")

    def __init__(self, IATA):

        self.edges = pd.read_csv("dataframes/edges.csv") # FIXME: atributo de clase (atributo que comporten todos los objetos) para evitar tener que cargar el dataframe varias veces (muy costoso)

        self.IATA = IATA
        self.destinos = self.get_destinos() # lista de objetos destino -> diccionario con claves como nombres de los aeropuertos y valores que son el coste: (codigo_aeropuerto_destino, distancia haversine)
        
        self.heuristica = self.get_heuristica() # distancia Harvesine directa desde el aeropuerto de inicio al aeropuerto de destino
        self.coste = self.obtener_coste() # distincia Haversine del aeropuerto actual al aeropuerto de escala 
        self.coste_total = self.obtener_coste_total() #

        self.padre = self.obtener_padre() # debería ser de una clase padre?


    def get_destinos(self)->pd.Series:
        return self.edges.loc([self.edges["origin"] == self.IATA], "destination")


    def get_heuristica(self):
        pass


    def obtener_coste(self):
        pass

    def obtener_coste_total(self):
        return self.coste + self.padre.coste + self.heuristica


    def obtener_padre(self):
        pass

    
    def __lt__(self, other):
        pass

    def __hash__(self):
        pass


