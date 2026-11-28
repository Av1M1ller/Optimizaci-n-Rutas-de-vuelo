import pandas as pd
from dataclasses import dataclass


@dataclass
class Nodo:   


    # edges = pd.read_csv("dataframes/edges.csv")

    def __init__(self, IATA):

        # self.edges = pd.read_csv("dataframes/edges.csv") # FIXME: atributo de clase (atributo que comporten todos los objetos) para evitar tener que cargar el dataframe varias veces (muy costoso)

        self.IATA = IATA
        self.destinos = self.get_destinos() # lista ponderada pdSeries (una "lista") lista de objetos destino -> diccionario con claves como nombres de los aeropuertos y valores que son el coste: (codigo_aeropuerto_destino, distancia haversine)
        
        self.coste_total = self.obtener_coste_total() 
        self.padre = self.obtener_padre() # debería ser de una clase padre?


    def get_destinos(self)-> pd.Series:
        return self.edges.loc[[self.edges["origin"] == self.IATA], "destination"] #TODO: cambiar lista de strs [IATA, IATA, IATA] por lista de nodos

    def obtener_coste_total(self) -> int:
        return self._get_heuristica() + self._get_coste()


    def _get_heuristica(self, IATA_destino): # distancia Harvesine directa desde el aeropuerto de inicio al aeropuerto de destino
        return self.edges.loc[(self.edges["origin"] == self.IATA) & (self.edges["destination"] == IATA_destino) , "haversine_km"].iloc(0)

    def _get_coste(self): # distincia Haversine del aeropuerto actual al aeropuerto de escala 
        # padre = self.obtener_padre()
        # resultado = 0
        # while padre is not None:
        #     resultado += padre.


    def obtener_padre(self):
        pass

    
    def __lt__(self, other):
        pass

    def __hash__(self):
        pass


