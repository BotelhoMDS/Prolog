import pandas as pd
import numpy as np 
import datetime as dt
from dataclasses import dataclass


@dataclass
class Individual:
    flights: pd.DataFrame
    

    @property
    def fitness (self):
        flights = self.flights 
        arrival = flights[flights['destination'] == 'FCO']
        departure = flights[flights['origin'] == 'FCO']
        
        max_arrival = arrival['arrival'].max()
        min_departure = departure['departure'].min()

        arrival_waiting = np.sum(max_arrival - arrival['arrival'])
        departure_waiting = np.sum(departure['departure'] - min_departure)

        cost = np.sum(flights['cost'])

        return arrival_waiting + departure_waiting + cost
    



