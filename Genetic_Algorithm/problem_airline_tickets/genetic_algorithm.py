import pandas as pd
import numpy as np
from individuo import Individual
from population import Population
import copy

def tournament(population: Population, tournament_size: int, tournament_rate: float):
    winners = []
    for _ in range(len(population.individuals)):
        knights = np.random.randint(0, len(population.individuals),tournament_size)
        fair = [population.individuals[i] for i in knights]

        
        strongerst_knight = min(fair, key=lambda knight: knight.fitness)
        weakest_knight = max(fair, key=lambda knight: knight.fitness)

        winner_knight = strongerst_knight if np.random.rand() < tournament_rate else weakest_knight                                      
        winners.append(winner_knight)
    
    return Population(winners, population.pop_tam)

def crossover(population: Population, crossover_rate: float):
    tinder = np.array(range(population.pop_tam))
    np.random.shuffle(tinder)
    childrens = []
    while len(tinder) > 1:
        if np.random.rand() < crossover_rate:
            a = tinder[0]
            b = tinder[1]
            tinder = np.delete(tinder, [0,1])
            arraival_a_genes = population.individuals[a].flights[:6]
            departure_a_genes = population.individuals[a].flights[6:]
            arraival_b_genes = population.individuals[b].flights[:6]
            departure_b_genes = population.individuals[b].flights[6:]
            
            crossing_point = np.random.randint(1, len(arraival_a_genes)-1)
            
            arraival_son = pd.concat([arraival_a_genes[:crossing_point], arraival_b_genes[crossing_point:]])
            arraival_daugehter = pd.concat([arraival_b_genes[:crossing_point], arraival_a_genes[crossing_point:]])
           

            crossing_point = np.random.randint(1, len(arraival_a_genes)-1)
            
            departure_son = pd.concat([departure_a_genes[:crossing_point], departure_b_genes[crossing_point:]])
            departure_daugehter = pd.concat([departure_b_genes[:crossing_point], departure_a_genes[crossing_point:]])


            son = Individual(pd.concat([arraival_son, departure_son]))
            daugehter = Individual(pd.concat([arraival_daugehter, departure_daugehter]))
            childrens.append(son)
            childrens.append(daugehter)
        else:
            childrens.append(population.individuals[tinder[0]])
            childrens.append(population.individuals[tinder[1]])
            tinder = np.delete(tinder, [0,1])

    return Population(childrens, population.pop_tam)

def mutation(population:Population, mutation_rate: float,data_flights: list):
    
    for individual in population.individuals:
        mutation_genes = np.random.rand(12) < mutation_rate
        mutation_genes_index = np.where(mutation_genes)[0]
        

        new_mutation = [data_flights[gene].sample()for gene in mutation_genes_index]
        if new_mutation: 
            individual.flights.iloc[mutation_genes_index] = pd.concat(new_mutation, ignore_index=True)

    return population
    

def elitism(population:Population,elit: Individual):
    if elit.fitness < population.best_individual().fitness:
        murdered = population.worst_individual_index()
        population.individuals[murdered[0]] = copy.deepcopy(elit)
    else: 
        elit = copy.deepcopy(population.best_individual())
    return population, elit


def genetic_algorithm(data_fligths: list,populations: Population,generations: list, POPULATION_TAM: int, GENERATIONS_TAM: int, TORNAMENT_SIZE: int, TORNAMENT_RATE: float,
                       CROSS_OVER_RATE: float, MUTATION_RATE: float):
    
    
    elit = copy.deepcopy(populations.best_individual())
    worst_for_generations = []
    average_for_generations = []
    elit_for_generations = []


    #algorithm interation 
    for years in range(GENERATIONS_TAM):
        
        generations.append(populations)

        elit_for_generations.append(elit.fitness.copy())
        worst_for_generations.append(populations.worst_individual().fitness)
        average_for_generations.append(populations.average_fitness())
    
        new_generation = tournament(populations, TORNAMENT_SIZE, TORNAMENT_RATE)
        
        new_generation = crossover(new_generation, CROSS_OVER_RATE)
        
        new_generation = mutation(new_generation, MUTATION_RATE, data_fligths)
        
        populations,elit = elitism(new_generation,elit)

    return elit, elit_for_generations, worst_for_generations, average_for_generations,generations
    