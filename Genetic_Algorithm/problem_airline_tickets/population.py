import numpy as np
import pandas as pd
from dataclasses import dataclass
from individuo import Individual

@dataclass
class Population: 
    individuals: list
    pop_tam : int

    def best_individual(self):
        return min(self.individuals, key=lambda individual: individual.fitness)
    def best_individual_index(self):
        return np.where(min(self.individuals, key=lambda individual: individual.fitness))[0]
    def worst_individual(self):
        return max(self.individuals, key=lambda individual: individual.fitness)
    def worst_individual_index(self):
        return np.where(max(self.individuals, key=lambda individual: individual.fitness))[0]
    def average_fitness(self):
        return np.mean([individual.fitness for individual in self.individuals])