import pandas as pd 
import numpy as np 
import datetime as dt 
from individuo import Individual
import genetic_algorithm as ga 
from population import Population
import matplotlib.pyplot as plt
import analisys as an

#Hiperparametros
POP_TAM = 20
GENERATIONS_TAM = 150
TORNAMENT_SIZE = 2
TORNAMENT_RATE = 0.75
CROSS_OVER_RATE = 0.60
MUTATION_RATE = 0.05
TEST_SIZE = 30 


#faz entrada de dados e adiciona cabeçalho 
header = ['origin', 'destination', 'departure', 'arrival', 'cost']
data = pd.read_csv('flights.txt')
data = pd.DataFrame(data.values, columns=header)

#converte para minutos os horarios de chegada e de saída 
data['departure'] = data['departure'].apply(lambda minutes: int(minutes.split(':')[0]) * 60 + int(minutes.split(':')[1]))
data['arrival'] = data['arrival'].apply(lambda minutes: int(minutes.split(':')[0]) * 60 + int(minutes.split(':')[1]))

#organiza os dados por origem e destino
data_fligths = [ 
            data[data['origin']=='LIS'],
            data[data['origin']=='MAD'],
            data[data['origin']=='CDG'],
            data[data['origin']=='DUB'],
            data[data['origin']=='BRU'],
            data[data['origin']=='LHR'],
            data[data['destination']=='LIS'],
            data[data['destination']=='MAD'],
            data[data['destination']=='CDG'],
            data[data['destination']=='DUB'],
            data[data['destination']=='BRU'],
            data[data['destination']=='LHR'],
            ]


population = []
generations = [] 

for individual in range(POP_TAM): 
    
    
    genototype = pd.concat([flight.sample() for flight in data_fligths])
    #print(Individual(genototype).fitness)
    population.append(Individual(genototype))


populations =  Population(individuals=population, pop_tam=POP_TAM)
 
for x in  range(TEST_SIZE):
    elit , elit_for_generations,worst_for_generations, average_for_generations ,generations = ga.genetic_algorithm(data_fligths, populations, generations, POP_TAM, GENERATIONS_TAM, TORNAMENT_SIZE, TORNAMENT_RATE, CROSS_OVER_RATE, MUTATION_RATE)
    print(f"Geração {x}")
    print(elit.fitness)
    print(elit_for_generations)


    plt.plot(average_for_generations, label='Average')
    plt.plot(worst_for_generations, label='Worst')
    plt.plot(elit_for_generations, label='Elit')
    plt.legend()
    plt.show()


   









