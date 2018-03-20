# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:58:13 2017

@author: User
"""

import random
import os
import xlrd
from enum import Enum



#curdir = os.getcwd()
#print(curdir)
#curdir = os.chdir('D:\\Toan\\1. NCU Master Degree\\Semester 4\\writing thesis')
#book = xlrd.open_workbook(os.path.join(os.getcwd(), "data", "FJS_exampleData.xlsx"))
#sheet1 = book.sheet_by_index(0)

'''
reading and clean the raw data from excel file
'''
#reading machines name
#machines = []
#col = 2
#while True:
#    try:
#        cellVal = sheet1.cell_value(0,col)
#        machines.append(cellVal)
#        col +=1
#    except IndexError:
#        break
#print(machines)
#['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8']

#reading operations name.
#operations = []
#row = 1
#while True:
#    try: 
#        cellVal = sheet1.cell_value(row, 1)
#        operations.append(cellVal)
#        row += 1
#    except IndexError:
#        break
#print(operations)
#['O11', 'O12', 'O13', 'O21', 'O22', 'O23', 'O24', 'O31', 'O32', 'O33',
#'O41', 'O42', 'O43', 'O51', 'O52', 'O53', 'O54', 'O61', 'O62', 'O63',
#'O71', 'O72', 'O73', 'O81', 'O82', 'O83', 'O84']

#reading list of jobs
#Note: given you know the range of operations
#jobs = []
#for i in range(len(operations)):
#    cellVal = sheet1.cell_value(i+1, 0)
#    if cellVal != '':
#        jobs.append(cellVal)
#print(jobs)
#['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8']

#reading the processing Time.
#processingTime = {}
#row = 1
#col = 2
#for operation in operations:
#    col = 2
#    for machine in machines:
#        cellVal = sheet1.cell_value(row, col)
#        processingTime[operation, machine] = cellVal
#        col += 1
#    row += 1
#print(processingTime) processingTime{('operation', 'machine'): time}

#machineDict = {
#                'O11': ['M1', 'M2', 'M3', 'M4'],
#                'O12': ['M1', 'M2', 'M3', 'M4'],
#                'O13': ['M1', 'M2', 'M3', 'M4'],
#                'O21': ['M1', 'M2', 'M3', 'M4'],
#                'O22': ['M1', 'M2', 'M3', 'M4'],
#                'O23': ['M1', 'M2', 'M3', 'M4'],
#                'O31': ['M1', 'M2', 'M3', 'M4'],
#                'O32': ['M1', 'M2', 'M3', 'M4']}

#print(machineDict) machineDict{'operation': [list of machines]}
'''
develop generate function for machine selction genes
and sequence decicion genes.
'''


def generate_operationSequence(operations):
    '''
    operations is a list.
    only take the job index of operation in operation list
    return a coding vector for operation Sequence.
    '''
    tempList = []
    for o in operations:
        tempList.append(o[:-1]) #create jobs list
    operationSequence = []
    i = 0
    while i < len(operations) :
        element = random.choice(tempList)
        operationSequence.append(element)
        tempList.remove(element)
        i += 1
    return operationSequence
#encodeSequence = generate_operationSequence(operations)
#print(encodeSequence)

'''
develop decoding function for sequence decision genes.
'''

def decode_operationSequence(encodeSequence):
    '''
    encodeSequence is a encoding list for operation sequence.
    return a list of operation sequence.
    '''
    jobDict = {}
    for j in set(encodeSequence): #a set of job
        jobDict[j] = 0 #create a adictionary ob job
    decodeSequence = []
    for i in encodeSequence: #loop through the encodeSequence
        jobDict[i] += 1
        decodeSequence.append(i + str(jobDict[i]))
    return decodeSequence
#sequenceGenes = decode_operationSequence(encodeSequence)
#print(sequenceGenes)

#print(operations)
#print(machineDict)
def generate_machineSelection(sequenceDecision, machineDict):
    '''
    operations is a list.
    machineDict{'operation': [list of machines]}
    return a coding vector for machine selection.
    '''
    machineSelection = []
    for o in sequenceDecision:
        machine = random.choice(machineDict[o]) #
        machineSelection.append(machine)
    return machineSelection
#encodeMachineSelection = generate_machineSelection(operations, machineDict)
#print(encodeMachineSelection)


#print(operations)
#'TAB211': job TA, product B2, job 1 of that compination, processing 1
'''
develop crossover, mutate function for
sequence decision genes, machine selection genes
''' 
#v1 = [3, 2, 1, 2, 3, 2, 1, 1, 3]
#v2 = [3, 1, 2, 3, 3, 1, 2, 1, 2]
#index = 5
#partial1 = v1[index:]
#partial2 = v2[index:]
#print(partial1, partial2)
#print(set(partial1))
#print(set(partial2))
#alist1 = list(set(partial1))
#alist2 = list(set(partial2))
#set(set(partial1)+set(partial2))

def find_exceedMissingGenes(partial1, partial2):
    '''
    partial1 and partial2 are lists of genes and
    have the same length. 
    return a list of dictionaries storing exceed and
    missing genes information of partial 2 compare to partail1.
    Note: dict2 store exceed information, dict1 store missing information
    '''
    genesSet1 = list(set(partial1))
    geneDict1 = {}
    for gene in genesSet1:
        geneDict1[gene] = 0
    genesSet2 = list(set(partial2))
    geneDict2 = {}
    for gene in genesSet2:
        geneDict2[gene] = 0
    temp1 = partial1[:]
    temp2 = partial2[:]
    #find exceed genes, partial2 compare to partial1.
    for p in partial2:
        if p in temp1:
            temp1.remove(p)
        else:
            geneDict2[p] += 1
    #find missing genes, partial 2 compare to partial1.
    for p in partial1:
        if p in temp2:
            temp2.remove(p)
        else:
            geneDict1[p] += 1
    #genDict2: exceed information, geneDict1: missing information
    return [geneDict2, geneDict1]
#print(partial1, partial2)
#exceedMissingGenes = find_exceedMissingGenes(partial1, partial2)
#print(partial1, partial2)
#print(exceedMissingGenes)

def fix_genes(partial1, partial2, find_exceedMissingGenes):
    '''
    partial1 is a tail split from sequence genes 1, a list.
    partial2 is a tail split from sequence genes 2, a list.
    after find exceed and missing genes do prepare.
    remove exceed and add missing genes to tail 2.
    Note: 
    '''
    exceedMissingGenes = find_exceedMissingGenes(partial1, partial2)
    newGenes = partial2[:]
    #remove exceed genes
    for k in exceedMissingGenes[0]:
        temp = exceedMissingGenes[0][k]
        if temp != 0:
            for i in range(temp):
                newGenes.remove(k)
    #adding missing genes
    for k in exceedMissingGenes[1]:
        temp = exceedMissingGenes[1][k]
        if temp != 0:
            for i in range(temp):
                newGenes.append(k)
    return newGenes
    
#print(partial1, partial2)
#prepairedGenes = fix_genes(partial1, partial2, find_exceedMissingGenes)
#print(prepairedGenes)
#print(partial1, partial2)


'''
develop crossover and mutate for encode sequence decision
'''   
def crossover_encodeSequence(v1, v2,find_exceedMissingGenes ,fix_genes):
    '''
    v1 is parent encodeSequence genes, it is a list.
    v2 is also parent encodeSequence genes, is a list.
    v1, v2 are in the same length.
    pick a mid point, split v1 and v2 into two part
    front and end. fixed end and recombine the genes.
    '''
    index = round(len(v1)/2)
    front1 = v1[:index]
    front2 = v2[:index]
    end2 = v2[index:]
    #fix end2, produce offSpring1
    end1 = v1[index:]
    end2 = v2[index:]
    fixedEnd2 = fix_genes(end1, end2, find_exceedMissingGenes)
    offSpring1 = front1 + fixedEnd2
    #fix end1, produce offSpring2
    end1 = v1[index:]
    end2 = v2[index:]
    fixedEnd1 = fix_genes(end2, end1, find_exceedMissingGenes)
    offSpring2 = front2 + fixedEnd1
    return [offSpring1, offSpring2]

#print(v1)
#print(v2)
#offSpring1, offSpring2 = crossover_encodeSequence(v1, v2, find_exceedMissingGenes, fix_genes)
#print(v1, v2)
#print(offSpring1, offSpring2)

 
    
#random.sample(range(len(v1)), 2)
def mutate_encodeSequence(genes):
    '''
    genes is a list of encode sequence decision.
    random choose two posistion and do swap
    return new genes
    Note: you dont want to change genes material
    '''
    newGenes = genes[:]
    indexes = random.sample(range(len(newGenes)), 2)
    index1, index2 = indexes[0], indexes[1]
    temp = newGenes[index2]
    newGenes[index2] = newGenes[index1]
    newGenes[index1] = temp
    return newGenes

#print(v1)
#newGenes = mutate_encodeSequence(v1)
#print(newGenes)
#print(v1)


'''
develope crossover, mutate for encode machine selection. 
'''
#machineSelection1 = generate_machineSelection(operations, machineDict)
#machineSelection2 = generate_machineSelection(operations, machineDict)
#print(machineSelection1)
#print(machineSelection2)

def crossover_encodeMachineSelection(genes1, genes2):
    '''
    genes is a encode list for machine Selection decision.
    pick mid point and do cross over.
    return newGenes1 and newGenes2
    '''
    index = round(len(genes1)/2)
    front1 = genes1[:index]
    end1 = genes1[index:]
    front2 = genes2[:index]
    end2 = genes2[index:]
    newGenes1 = front1 + end2
    newGenes2 = front2 + end1
    return [newGenes1, newGenes2]

#print(machineSelection1)
#print(machineSelection2)
#newMachineSelection = \
#crossover_encodeMachineSelection(machineSelection1, machineSelection2)
#print(newMachineSelection)
#
#
#print(machineDict)
#print(list(machineDict['O11']).remove('M1'))
#print(machineDict['O11'])
#print(machineDict)
#
#alist = [1, 2, 3, 4, 5]
#print(list(alist.remove(5)))

def mutate_encodeMachineSelection(genes,operations, machineDict):
    '''
    genes is a list encode for machine selection.
    operations is a list of ordered operations from global environment
    pick a random point and choose machine from 
    machineDict
    return new genes
    Note: you dont want to change genes, and machineDict.
    '''
    newGenes = genes[:]
    index = random.randint(0, len(newGenes)-1)
    currentMachine = newGenes[index]
    operation = operations[index]
    machineList = machineDict[operation][:]
    machineList.remove(currentMachine)
    newMachine = random.choice(machineList)
    newGenes[index] = newMachine
    return newGenes
    
#print(machineSelection1)
#newGenes1 = mutate_encodeMachineSelection(machineSelection1, operations, machineDict)
#print(newGenes1)
#print(machineSelection1)
#print(machineDict)
#    
    
'''
develop decoding chromosome function or translate
sequence genes and machine selection genes to
readable plan.
'''

#encodeSequence = generate_operationSequence(operations)
#sequenceDecision = decode_operationSequence(encodeSequence)
#print(sequenceDecision)
#machineSelection = generate_machineSelection(operations, machineDict)
#print(operationSequence)
#print(sequenceDecision)
#print(machineSelection)
#print(processingTime)
#for i in sequenceDecision:
#    print(type(i[1]))



def get_scheduleResult(sequenceGenes, machineSelectionGenes,
                       operations, processingTime, decode_operationSequence):
    '''
    sequenceGenes is a list of encode genes for operation Sequence.
    machineSelectionGenes is a list of encode genes for machine selection.
    operations is a list of ordered operations of jobs.
    processingTime is a dict with key is (operation, machine) from global environment. 
    decode_operationSequence is a function to translate sequenceGenes
    return a readable scheduling plan.
    '''    
    #Note: sequenceDecision is readable sequence decision
    sequenceDecision = decode_operationSequence(sequenceGenes)
    jobTime = {} #to keep track of job time
    machineTime = {} #to keep track of machineTime
    schedulingResult = {} #store the result
    #create key for jobTime and machineTime dictionary.
    #Note: if you dont create dict with key you can not
    #call it later or keyError.
    for machine in set(machineSelectionGenes):
        machineTime[machine] = 0 #
    for job in set(sequenceGenes):
        jobTime[job] = 0
    for i in range(len(sequenceDecision)):
        #note: each element in operation is unique.
        machineIndex = operations.index(sequenceDecision[i])
        machine = machineSelectionGenes[machineIndex]
        operation = sequenceDecision[i]
        processTime = processingTime[operation,machine]
        machineTime[machine] += processTime
        jobTime[sequenceDecision[i][:-1]] += processTime
        completionTime = max(machineTime[machine], jobTime[sequenceDecision[i][:-1]])
        startingTime = completionTime - processTime
        #update jobTime and machineTime
        machineTime[machine] = completionTime
        jobTime[sequenceDecision[i][:-1]] = completionTime
        schedulingResult[operation, machine] = (startingTime, completionTime)
    return schedulingResult
    
#schedulingResult = get_scheduleResult(operationSequence, machineSelection,
#                                      operations, processingTime, decode_operationSequence)
#print(schedulingResult)

############################################################################
#we want to fix the get_scheduele Reuslt function
###########################################################################
#print(operations)
#randomdly generate operation sequence
#encodeSequence = generate_operationSequence(operations)
#print(encodeSequence)
#decode the operation encodeSequence
#sequenceDecision = decode_operationSequence(encodeSequence)
#sequenceDecision[0]
##machine selection
#machineSelection = generate_machineSelection(operations, machineDict)
#machineSelection[0]
#print(processingTime)

#def get_scheduleResult(sequenceGenes, machineSelectionGenes,
#                       processingTime, decode_operationSequence):
#    sequenceDecision = decode_operationSequence(sequenceGenes)
#    jobTime = {}
#    machineTime = {}
#    schedulingResult = {}
#    for machine in set(machineSelectionGenes):
#        machineTime[machine] = 0
#    for job in set(sequenceGenes):
#        jobTime[job] = 0
#    for i in range(len(sequenceDecision)):
#        machine = machineSelectionGenes[i] #get machine
#        operation = sequenceDecision[i] #get operation
#        processingTime = processingTime[operation, machine] #get operation time of that operation
#        machineTime[machine] += processingTime # current machine Time
#        jobTime[operation[:-1]] += processingTime # current job time.
#        completionTime = max(machineTime[machine], jobTime[operation[:-1]])
#        startingTime = completionTime - processingTime
#        #update jobTime and machineTime
#        machineTime[machine] = completionTime
#        jobTime[operation[:-1]] = completionTime
#        schedulingResult[operation, machine] = (startingTime, completionTime)
#        return schedulingResult

def get_longestTime(schedulingResult):
    '''
    schedulingResult is a dictionary with
    key is (operation, machine)
    return the completion time of the last operation
    '''
    completionTime = []
    for i in schedulingResult:
        completionTime.append(schedulingResult[i][1])
    return max(completionTime)
    
    
#print(schedulingResult)
#get_longestTime(schedulingResult)
#machineSelectionGenes = generate_machineSelection(operations, machineDict)

def get_maxWorkload(schedulingResult, machineSelectionGenes, processingTime):
    '''
    schedulingResult is a dictionary with
    key is (operation, machine).
    machines is a list of ordered machines in global environment
    workload of each machine is total
    processing time of each machine.
    return the max workload value.
    given ProcessingTime in the global environment.
    '''
    #create key for machineTracker
    machineTracker = {}
    for machine in set(machineSelectionGenes):
        machineTracker[machine] = 0
    for i in schedulingResult:
        processTime = processingTime[i]
        machineTracker[i[1]] += processTime
    return max(machineTracker.values())
#print(processingTime)
#print(schedulingResult)    
#get_maxWorkload(schedulingResult, machineSelectionGenes, processingTime)




#compute total workload of all machine.
def get_totalWorkload(schedulingResult,machineSelectionGenes, processingTime):
    '''
    schedulingResult is a dictionary with key
    is (operation, machine)
    return total processing time of all machine
    given processingTime in the global environment
    '''
    #create key for machineTracker
    machineTracker = {}
    for machine in set(machineSelectionGenes):
        machineTracker[machine] = 0
    for i in schedulingResult:
        processTime = processingTime[i]
        machineTracker[str(i[1])] += processTime
    return sum(machineTracker.values())

#print(schedulingResult)
#get_totalWorkload(schedulingResult,machines, processingTime)


'''
building complete GA with class and method.
'''

def get_fitness(genes,operations, processingTime, decode_operationSequence):
    '''
    genes is a list of list.
    genes[0] is encode sequence genes
    genes[1] is encode machine selection genes
    Note: call other functions and data from
    the global environment.
    return fitness class
    '''
    sequenceGenes = genes[0]
    machineSelectionGenes = genes[1]
    schedulingResult = get_scheduleResult(sequenceGenes, machineSelectionGenes,operations,
                                          processingTime, decode_operationSequence)
    longestTime = get_longestTime(schedulingResult)
    maxWorkload = get_maxWorkload(schedulingResult, machineSelectionGenes, processingTime)
    totalWorkload = get_totalWorkload(schedulingResult,machineSelectionGenes, processingTime)
    return Fitness(longestTime, maxWorkload, totalWorkload)

    
#sequenceGenes = generate_operationSequence(operations)
#machineSelectionGenes = generate_machineSelection(operations, machineDict)
#print(sequenceGenes)
#print(machineSelectionGenes)
#genes1 = [sequenceGenes, machineSelectionGenes]
#print(genes1)
#fitness1 = get_fitness(genes1,jobs, operations, processingTime, decode_operationSequence)
#print(fitness1)

def generate_parent(machineDict, operations, processingTime, decode_operationSequence, get_fitness):
    '''
    operations is a list of unique operations.
    machineDict is a dict with key is operation, value is
    list of machines can process corresponding operations
    get_fitnees is a function to get_fitness of parent.
    return a parent individual or chromosome class
    Note: other datas and functions is from the global environment.
    '''
    sequenceGenes = generate_operationSequence(operations)
    machineSelectionGenes = generate_machineSelection(operations, machineDict)
    genes = [sequenceGenes, machineSelectionGenes]
    fitness = get_fitness(genes,operations, processingTime, decode_operationSequence)
    return Chromosome(genes, fitness, Strategies.Create)
 
#parent1 = generate_parent(machineDict, operations, processingTime, decode_operationSequence, get_fitness)
#print(parent1.Genes)
#print(parent1.Fitness)



def mutate(parent, machineDict, operations, processingTime, decode_operationSequence):
    '''
    parent is a chromosome instant.
    return newChild is also a chromosome instant.
    Note: other datas and function is from the global environment.
    '''
    sequenceGenes = parent.Genes[0][:]
    machineSelectionGenes = parent.Genes[1][:]
    child_sequenceGenes =  mutate_encodeSequence(sequenceGenes)
    child_machineSelectionGenes = mutate_encodeMachineSelection(machineSelectionGenes,operations, machineDict)
    newGenes = [child_sequenceGenes, child_machineSelectionGenes]
    fitness = get_fitness(newGenes,operations, processingTime, decode_operationSequence)
    return Chromosome(newGenes, fitness, Strategies.Mutate)



#print(parent1.Genes)
#child1 = mutate(parent1, machineDict, operations, processingTime, decode_operationSequence)
#print(parent1.Genes, parent1.Fitness)
#print(child1.Genes, child1.Fitness) 

def cross_over(parent1, parent2, operations, processingTime,
               decode_operationSequence, find_exceedMissingGenes, fix_genes):
    '''
    parent1, parent2 are chromosome instants.
    '''
    sequenceGenes1 = parent1.Genes[0][:]
    machineSelectionGenes1 = parent1.Genes[1][:]
    sequenceGenes2 = parent2.Genes[0][:]
    machineSelectionGenes2 =parent2.Genes[1][:]
    childSequenceGenes1, childSequenceGenes2 = \
    crossover_encodeSequence(sequenceGenes1, sequenceGenes2,find_exceedMissingGenes ,fix_genes)
    childMachineSelectionGenes1, childMachineSelectionGenes2 = \
    crossover_encodeMachineSelection(machineSelectionGenes1, machineSelectionGenes2)
    childGenes1 = [childSequenceGenes1, childMachineSelectionGenes1]
    childGenes2 = [childSequenceGenes2, childMachineSelectionGenes2]
    childFitness1 = get_fitness(childGenes1,operations, processingTime, decode_operationSequence)
    childFitness2 = get_fitness(childGenes2,operations, processingTime, decode_operationSequence)
    child1 = Chromosome(childGenes1, childFitness1, Strategies.Crossover)
    child2 = Chromosome(childGenes2, childFitness2, Strategies.Crossover)
    return [child1, child2]

#parent1 = generate_parent(machineDict,operations, processingTime, decode_operationSequence, get_fitness)
#parent2 = generate_parent(machineDict,operations, processingTime, decode_operationSequence, get_fitness)
#child1, child2 = cross_over(parent1, parent2, operations,
#                            processingTime, decode_operationSequence, find_exceedMissingGenes, fix_genes)
#print(parent1.Genes, parent1.Fitness)
#print(parent2.Genes, parent2.Fitness)
#print(child1.Genes, child1.Fitness)
#print(child2.Genes, child2.Fitness)
 
    
'''
develop class for GA.
'''    




#create a generator of individual.
def get_improve(machineDict, operations, processingTime, decode_operationSequence,
                           find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over):
    '''
    the goal: yield better individual each iteration.
    '''
    bestParent1 = generate_parent(machineDict, operations, processingTime, decode_operationSequence, get_fitness)
    bestParent2 = generate_parent(machineDict, operations, processingTime, decode_operationSequence, get_fitness)
    while True:
        probability = random.random()
        if probability > 0.3 :
            child1, child2 = cross_over(bestParent1, bestParent2, operations, processingTime,
                                        decode_operationSequence, find_exceedMissingGenes, fix_genes)
        else:
            child1 = mutate(bestParent1, machineDict, operations, processingTime, decode_operationSequence)
            child2 = mutate(bestParent2, machineDict, operations, processingTime, decode_operationSequence)
        #find bestParent1 and bestParent2.
        if child1.Fitness > child2.Fitness:
            if (child1.Fitness > bestParent1.Fitness) and (child1.Fitness > bestParent2.Fitness):
                if (bestParent1.Fitness > bestParent2.Fitness):
                    bestParent1, bestParent2 = child1, bestParent1
                else:
                    bestParent1, bestParent2 = bestParent2, child1
        else:
            if (child2.Fitness > bestParent1.Fitness) and (child2.Fitness > bestParent2.Fitness):
                if (bestParent1.Fitness > bestParent2.Fitness):
                    bestParent1, bestParent2 = child2, bestParent1
                else:
                    bestParent1, bestParent2 = bestParent2, child2
        yield [bestParent1, bestParent2]


def generate_population(n, machineDict, operations, processingTime, decode_operationSequence, get_fitness):
    '''
    n is int, the number of individual in the population.
    return a list of n individuals.
    '''
    pop = []
    for i in range(n):
        tempParent = generate_parent(machineDict, operations, processingTime, decode_operationSequence, get_fitness)
        pop.append(tempParent)
    return pop
#test for generate_population    
#parent1 = generate_parent(machineDict, operations, processingTime, decode_operationSequence, get_fitness)
#print(parent1.Genes)
#print(parent1.Fitness)
#population = generate_population(10, machineDict, operations, processingTime, decode_operationSequence, get_fitness)
#print(population[1].Genes)
#print(population[1].Fitness)
    
#create a generator version2 each iteration create a population.
def get_improve2(n, machineDict, operations, processingTime, decode_operationSequence,
                           find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over, generate_population):
    '''
    n is the number of individuals in the population.
    given the probability of crossover and mutate.
    return a population of individuals each interation.
    '''
    #generate_population is a function define outside.
    pop = generate_population(n, machineDict, operations, processingTime, decode_operationSequence, get_fitness)
    #doing evolution.
    while True:
        newPop = []
        #random choose two sub population for mutation.
        pop1 = random.sample(pop, int(n/3))
        pop2 = random.sample(pop, int(n/3))
        #just do the cross over.
        for i in range(int(1/3)):
            parent1 = pop1[i]
            parent2 = pop2[i]
            #set the probability for cross_over.
            if random.random() > 0.3:
                child1, child2 = cross_over(parent1, parent2, operations, processingTime,
                                        decode_operationSequence, find_exceedMissingGenes, fix_genes)
                #seleciton processing.
                if child1.Fitness > parent1.Fitness and child2.Fitness > parent2.Fitness:
                    newPop.extend([child1, child2])
                elif child1.Fitness > parent1.Fitness and parent2.Fitness > child2.Fitness:
                    newPop.extend([child1, parent2])
                elif parent1.Fitness > child1.Fitness and child2.Fitness > parent2.Fitness:
                    newPop.extend([parent1, child2])
                else: newPop.extend([parent1, parent2])
                
            else:
                newPop.extend([parent1, parent2])
        #just do mutation.
        pop3 = random.sample(pop, int(n/3))
        for i in range(int(n/3)):
            parent3 = pop3[i]
            #set the propability for mutation.
            if random.random() > 0.7:
                child3 =  mutate(parent3, machineDict, operations, processingTime, decode_operationSequence)
                #selection processing
                if child3.Fitness > parent3.Fitness:
                    newPop.append(child3)
                else:
                    newPop.append(parent3)
            else:
                newPop.append(parent3)
        pop = newPop[:]
        yield newPop
    
#test get_improve2().
#count = 0
#for improvement in get_improve2(10, machineDict, operations, processingTime, decode_operationSequence,
#                           find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over, generate_population):
#    newPop = improvement
#    print(newPop[0].Genes)
#    print(newPop[1].Fitness)
#    count += 1
#    if count == 2:
#        break
    
def find_bestIndividual(population):
    '''
    given a population the goal is to find the best individual.
    newPop is a list of chromosome.
    return the best dividual.
    dont change population.
    '''
    popFitness = [] #the first priority.
    for i in range(len(population)):
        popFitness.append(population[i].Fitness.LongestTime)
    bestIndividualIndex = popFitness.index(min(popFitness))
    bestIndividual = population[bestIndividualIndex]
    return bestIndividual
    
def find_bestIndividual2(population):
    '''
    given a population of individuals
    using sorted function of alist to sort list of objects.
    return the best Indiviudal 
    '''
    bestIndividual = sorted(population, reverse=True)[0]
    return bestIndividual
#test find_bestIndividual().
#population = generate_population(10, machineDict, operations, processingTime, decode_operationSequence, get_fitness)
#bestIndividual = find_bestIndividual(population)
#print('best Individual Genes: ', bestIndividual.Genes)
#print('best Individual Fitness: ', bestIndividual.Fitness)
#randomIndividual = population[random.randint(0, len(population)-1)]
#print('random Individual Genes:', randomIndividual.Genes)
#print('random Individual Fitness: ', randomIndividual.Fitness)
    

    
def get_result2(n, machineDict, operations, processingTime, decode_operationSequence,
               find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over,
               generate_population,get_improve2, find_bestIndividual):
    '''
    each interation return an improving population.
    in each population choose the best idividual
    compare to the last once, get the improving only.
    '''
    bestIndividuals = []
    count = 0
    #note: get_improve2 is generator defined outsiide
    for improvement in get_improve2(n, machineDict, operations, processingTime, decode_operationSequence,
                           find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over, generate_population):
        newPop = improvement[:]
        #find_bestIndividual is a function defined outside.
        bestIndividual = find_bestIndividual2(newPop)
#        print(bestIndividual.Genes) #testing
        #for the first iteration, if not index error.
        if count == 0:
            bestIndividuals.append(bestIndividual)
        elif bestIndividual.Fitness > bestIndividuals[len(bestIndividuals)-1].Fitness:
            bestIndividuals.append(bestIndividual)
        currentBestIndividual = bestIndividuals[len(bestIndividuals)-1]
        print('current best individual fitness: ', currentBestIndividual.Fitness)
#        print('current best individual genes: ', currentBestIndividual.Genes)        
        count += 1
        print(count)
        if count > 2000: #setting iteration of evolution process.
            return bestIndividuals
            break
        
#test get_result2().
#bestIndividuals = get_result2(10, machineDict, operations, processingTime, decode_operationSequence,
#               find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over,
#               generate_population,get_improve2, find_bestIndividual)
  
      

def get_result(machineDict, operations, processingTime, decode_operationSequence,
               find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over):
    count = 0
    fitnessList = [] #to store fitness information through generation.
    for improvement in get_improve(machineDict, operations, processingTime, decode_operationSequence,
                           find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over):
        bestParent1 = improvement[0]
        bestParent2 = improvement[1]
        fitnessList.append(bestParent2.Fitness.LongestTime)
        print('best parent1 genes: ', bestParent1.Genes)
        print('best parent1 fitness: ', bestParent1.Fitness)
        print('best parent2 genes: ', bestParent2.Genes)
        print('best parent2 fitness: ', bestParent2.Fitness)
        count += 1
        print(count)
        if count >5000:  #set the iteration of evolution process.
#            return [bestParent1, bestParent2]
            return fitnessList
            break
        
#get_result(machineDict, operations, processingTime, decode_operationSequence,
#           find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over)
#        
        

        
            
                        
class Chromosome:
    def __init__(self, genes, fitness, strategy):
        self.Genes = genes
        self.Fitness = fitness
        self.Strategy = strategy
        self.Age = 0
    def __lt__(self, other):
        return self.Fitness < other.Fitness


class Strategies(Enum):
    Create = 0,
    Mutate = 1,
    Crossover = 2
    
    
class Fitness:
    def __init__(self, longestTime, maxWorkload, totalWorkload):
        self.LongestTime = longestTime
        self.MaxWorkload = maxWorkload
        self.TotalWorkload = totalWorkload

#    def __gt__(self, other):
#        if self.LongestTime < other.LongestTime:
#            return True
#        elif self.LongestTime == other.LongestTime:
#            if self.MaxWorkload < other.MaxWorkload:
#                return True
#            elif self.MaxWorkload == other.MaxWorkload:
#                if self.TotalWorkload < other.TotalWorkload:
#                    return True
#                else:
#                    return False
#        else:
#            return False
 
    def __lt__(self, other):
        if self.LongestTime > other.LongestTime:
            return True
        elif self.LongestTime == other.LongestTime:
            if self.MaxWorkload > other.MaxWorkload:
                return True
            elif self.MaxWorkload == other.MaxWorkload:
                if self.TotalWorkload > other.TotalWorkload:
                    return True
            

    def __str__(self):
        return "Time to process all jobs: {0: 0.2f}, maximum workload: {1: 0.2f}, total workload: {2: 0.2f}".format(self.LongestTime, self.MaxWorkload, self.TotalWorkload)
                
               
                
#machineTracker = {}
#for machine in machines:
#    machineTracker[machine] = 0
#print(machineTracker)
#machineTracker['M1']
#best1 = 4
#best2 = 6
#best = 2
#
#best1, best2 = best, best1
#print(best1, best2)
#--------------------------------------------------------------
#alist = [1, 2, 3, 4]
##print(sorted(alist, reverse=True)[0])
##print(alist)
#alist.sort(reverse=True)
#print(alist[0])

