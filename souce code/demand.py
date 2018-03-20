# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:35:09 2017

@author: Bui Xuan Toan
"""
import os
#os.chdir('D:\Toan\1. NCU Master Degree\Semester 4\writing thesis')
#print(os.getcwd())
 
#Products code.
'''
Products table: is a dictionary with key is production code.
value is a list [name, volume, demand (ml),type, fermentation time].
'''
##Note this is the data for approximate the real data
productTable = {'B1': ['333 premium (bottle)', 330, 0, 'Premium lager', 28],
                'B2': ['333 (can)', 330, 300*10**3*10**3, 'lager', 21],
                'B3': ['saigon lager (bottle)', 450, 1250*10**3*10**3, 'lager', 21],
                'B4': ['saigon lager (can)', 330, 1000*10**3*10**3, 'lager', 21],
                'B5': ['saigon export (bottle)', 355, 100*10**3*10**3, 'lager', 28],
                'B6': ['saigon special (bottle)', 330, 0, 'lager', 28],
                'B7': ['saigon special (can)', 330, 300*10**3*10**3, 'lager', 28]}
                       
#Note: this is the data for 10 time smaller
#productTable = {'B1': ['333 premium (bottle)', 330, 0, 'Premium lager', 28],
#                'B2': ['333 (can)', 330, 30*10**3*10**3, 'lager', 21],
#                'B3': ['saigon lager (bottle)', 450, 125*10**3*10**3, 'lager', 21],
#                'B4': ['saigon lager (can)', 330, 100*10**3*10**3, 'lager', 21],
#                'B5': ['saigon export (bottle)', 355, 10*10**3*10**3, 'lager', 28],
#                'B6': ['saigon special (bottle)', 330, 0, 'lager', 28],
#                'B7': ['saigon special (can)', 330, 30*10**3*10**3, 'lager', 28]}

'''
machine coding:
machine is a dictionary with key is machine coding,
value is capacity.
TA: tank with capcacity of 500 BBL (change to ml).
TB: tank with capacity of 1000 BBL (change to ml).
FC: can filling line, 30000 can/h.
FB: bottle filling line, 35000 bottle/h
Note: the measure for volume is ml.
'''
machine = {'TA1': 500*117*1000,
           'TA2': 500*117*1000,
           'TA3': 500*117*1000,
           'TA4': 500*117*1000,
           'TA5': 500*117*1000,
           'TB1': 1000*117*1000,
           'TB2': 1000*117*1000,
           'TB3': 1000*117*1000,
           'TB4': 1000*117*1000,
           'TB5': 1000*117*1000,
           'TB6': 1000*117*1000,
           'TB7': 1000*117*1000,
           'TB8': 1000*117*1000,
           'FC1': 30000,
           'FC2': 30000,
           'FB1': 35000,
           'FB2': 35000}
           


fillingMachineType = ['FC', 'FB']
fillingMachines = ['FC1', 'FC2', 'FB1', 'FB2']
fillingMachineDict = {'FC': ['FC1', 'FC2'], 'FB': ['FB1', 'FB2']}
tankType = ['TA', 'TB']
tankList = ['TA1', 'TA2', 'TA3', 'TA4', 'TA5','TB1', 'TB2', 'TB3', 'TB4', 'TB5', 'TB6', 'TB7', 'TB8']
tanksDict = {'TA': ['TA1', 'TA2', 'TA3', 'TA4', 'TA5'], 'TB': ['TB1', 'TB2', 'TB3', 'TB4', 'TB5', 'TB6', 'TB7', 'TB8']}
productFillingLineDict = {'B1': ['FB1', 'FB2'], 'B2': ['FC1', 'FC2'], 'B3': ['FB1', 'FB2'],
                          'B4': ['FC1', 'FC2'], 'B5': ['FB1', 'FB2'], 'B6': ['FB1', 'FB2'], 'B7': ['FC1', 'FC2']}
fillingLineCapacity = {'FC': 30000, 'FB': 35000} #bottle/hour.



'''
we want to get productVolume{'product': volume}
'''
def get_productVolume(productTable):
    '''
    return the bottle volume (ml) of each product
    '''
    productVolume = {}
    for p in productTable.keys():
        productVolume[p] = productTable[p][1]
    return productVolume

productVolume = get_productVolume(productTable)
#print(productVolume)
           
'''
demand table.
use product table at an input. user just need to change the demand,
or production quantity that they want to produce in a period of time.
out put: dictionary withy key is product code and demand. 
'''
def find_production(productTable):
    '''
    productTable is a product Table as define in previous code.
    out put is demand{'product': demand}.
    '''
    demand = {}
    for key in productTable.keys():
        if productTable[key][2] != 0:
            demand[key] = productTable[key][2]
    return demand
    
demand = find_production(productTable)
#print(demand)


'''
find set of products want to produce.
'''
def get_product(demand):
    '''
    input: demand{'product': demand}
    output: list of sorted products will be produced
    '''
    product = sorted(list(demand.keys()))
    return product
    
products = get_product(demand)
#print(products)



'''
we want to solve linear programing model to find optimization job.
First we want to find the input data for the model.
'''

'''
find fermention time for products.
'''
def get_fermentationTime(productTable, products):
    '''
    output: fermentationTime{'product': time}
    '''
    fermentationTime = {}
    for p in products:
        fermentationTime[p] = productTable[p][4]
    return fermentationTime
    
fermentationTime = get_fermentationTime(productTable, products)
#print(fermentationTime)


####################################################
#Model1
'''
find type of tanks and their capacity.
in this case: TA: 500 BBL, TB: 1000 BBL
'''
def get_tankCapacity(machine):
    '''
    output: tankCapacity{'tank': capacity}
    '''
    tankCapacity = {}
    count = 0
    for t in machine.keys():
        if t[0] == 'T':
            count += 1
            if count == 1:
                tankCapacity[t[:2]] = machine[t]
                temp = t[:2]
            elif t[:2] != temp:
                tankCapacity[t[:2]] = machine[t]
                temp = t[:2]
    return tankCapacity

tankCapacity = get_tankCapacity(machine) #tank type
#print(tankCapacity)

def get_tanks(tankCapacity):
    '''
    output a list of tanks
    '''
    tanks = sorted(list(tankCapacity.keys()))
    return tanks

tankType = get_tanks(tankCapacity) #tank type
#print(tanks)

##########################################################
##Model2
#'''
#get_tanks() for model 2.
#'''
#def get_tanks2(machine):
#    '''
#    machine is a dict('machine': capacity)
#    return a list of tanks
#    '''
#    tanks = []
#    for k in machine.keys():
#        if k[0] == 'T':
#            tanks.append(k)
#    tanks.sort()
#    return tanks
#    
#tanks = get_tanks2(machine)
#print(tanks)
#
#'''
#get_TankCapacity2 for the model2
#'''
#def get_tankCapacity2(tanks, machine):
#    tankCapacity = {}
#    for t in tanks:
#        tankCapacity[t] = machine[t]
#    return tankCapacity
#    
#tankCapacity = get_tankCapacity2(tanks, machine)
#print(tankCapacity)
        
    
    
        


'''
Second: we definde decision variable, constraint and objective function.
in order to solve the model you need:
products: a list of products.
tanks: a list of type of tanks.
demand{'product': demand}
fermentationTime{'product': fermentationTime}
tankCapacity{'tank': capacity}
Note: model 1 we just consider the type of tanks
model 2 we consider specified tanks
'''
#print(products)
#print(tanks) #type of tanks
#print(demand)
#print(fermentationTime)
#print(tankCapacity)

#add de

from gurobipy import *

m = Model("fermentation")

#add decision variable.
#the number of time use you tank type t for product p.
numTank = m.addVars(tankType, products,vtype=GRB.INTEGER, name = 'numTank')
print(numTank)

#add objective function.
#objective fuction 1.
m.setObjective(quicksum(numTank[t,p]*fermentationTime[p] for t in tankType for p in products))

#add constraints.
#demand constraints.
m.addConstrs(((quicksum(numTank[t,p]*tankCapacity[t] for t in tankType) >= demand[p]) for p in products), '_')

#tank balance constraint.
#model1
m.addConstrs((quicksum(numTank[t,p] for t in tankType if t == 'TA') - quicksum(numTank[t,p] for t in tankType if t == 'TB') >= 0 for p in products), '_')
#model2
#m.addConstrs((quicksum(numTank[t,p] for t in tanks if t[:2] == 'TA') - quicksum(numTank[t,p] for t in tanks if t[:2] == 'TB') >= 0 for p in products), '_')
    

#define print function.
def printSolution():
    if m.status == GRB.Status.OPTIMAL:
        print('\nCost: %g' % m.objVal)
        print('\nNumber of time using tank: ')
        numTankx = m.getAttr('x', numTank)
        for t in tanks:
            for p in products:
                print('tank:{0}, product: {1}: {2}'.format(t, p, numTankx[t,p]))
                
m.optimize()
#printSolution()



'''
Now we want to create the input data for flexible job shop scheduling problem.
you need:
machines
jobs
operation.
processingTime

'''
#bestIndividuals = get_result2(100, machineDict, operations, processingTime, decode_operationSequence,
#               find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over,
#               generate_population,get_improve2, find_bestIndividual)

#print(machineDict)

'''
The first important task is to find machineDict{'operation': [machines]}
'''



#get the solution form gurubi solver.
def get_result():
    '''
    return the result in sorted order
    '''
    if m.status == GRB.Status.OPTIMAL:
        numTankx = m.getAttr('x', numTank)
    return numTankx

numTankx = get_result()
#print(numTankx)

'''
Now you want to create a job list which code like the flowing:
tankTypeProduct (TAB3i), i is the number of job in that criteria.
'''
def create_jobList(numTankx):
    #return a sorted jobList.
    sortedJob = sorted(numTankx.keys())
    jobList = []
    for k in sortedJob:
        for i in range(int(numTankx[k])): #number of job for each coding
            jobList.append(k[0]+k[1]+str(i+1))
    return jobList
    
jobList = create_jobList(numTankx)
#print(jobList)


'''
Now you want to create operation list.
'''
def create_operationList(jobList):
    '''
    return sorted operationList with cod TAB211: tank (TB), product(B2), job(1), operation(1)
    '''
    operationList = []
    for j in jobList:
        for i in range(2): #each job have 2 operation.
            operationList.append(j + str((i+1)))
    return operationList
    
operations = create_operationList(jobList)
#print(operations)
#print(len(operations))

'''
Now you have operationList, let find machineDict{'operation': [machineSet]}
'''
#print(tanksDict)
#print(productFillingLineDict)
def get_machineDict(operations, tanksDict, productFillingLineDict):
    #operationList coding you know tank type and product type.
    #tankDict{'tankType': [list of tanks]}
    #return machineDict{'operation': [machineSet]}
    machineDict = {}
    for o in operations:
        if o[-1] == '1':
            machineDict[o] = tanksDict[o[:2]] #get tanks
        else:
            machineDict[o] = productFillingLineDict[o[2:4]] #get fillingLine
    return machineDict
    
machineDict = get_machineDict(operations, tanksDict, productFillingLineDict)
#print(machineDict)
#print(len(machineDict))

'''
Now you want to get processingTime{('operation', 'machine'): time} .
'''
def compute_fillingTime(demand, bottleType, capacity):
    '''
    demand is in ml.
    bottleType in ml.
    capacity, bottle/hour
    return time in hour.
    '''
    bottle = int(demand/bottleType)
    hour = int(bottle/capacity)
    date = round(hour/24,2)
    return date
#print(machine)    
def get_processingTime(machineDict, productTable, machine):
    '''
    machineDict{'operation': [machineSet]}
    machine{'machine': capacity}
    return processingTime{('operation', machine): time}
    '''
    processingTime = {}
    for o in machineDict.keys(): #operations
        for m in machineDict[o]: #machine set for that operations
            if o[-1] == str(1): #fermentation. Note testing wrong! str not int.
                processingTime[o, m] = productTable[o[2:4]][-1] #fermentation Time of product
            else : #filling operation o[-1] == 2.
                processingTime[o, m] = compute_fillingTime(productTable[o[2:4]][2], productTable[o[2:4]][1], machine[m])
    return processingTime
    
processingTime = get_processingTime(machineDict, productTable, machine)
#print(processingTime)


#create df from dictionary and write to an excel file.
#note: if you can not create a df form a dict using list of tuple.
import pandas as pd
processingTimeList = [] #list of tuple
for key in processingTime.keys():
    processingTimeList.append((key, processingTime[key]))
print(processingTimeList)

processingTimeData = pd.DataFrame(processingTimeList, columns = ['Operation', 'Processing Time'])
processingTimeData.to_excel('ProcessingTimeData1.xlsx', index = False)


    
    
                
            
'''
Now we want to solve the shop job scheduling problem.
'''    
import os
import xlrd
from enum import Enum
from GA_engine2 import *
from drawingFunction import *

#print(operations)
#print(processingTime)
#draw_lineGraph(index, fitnessList, 'learning curve2')
#bestIndividuals is as lit of betIndividual through the evolution process. 
bestIndividuals = get_result2(200, machineDict, operations, processingTime, decode_operationSequence,
               find_exceedMissingGenes, fix_genes, get_fitness, mutate, cross_over,
               generate_population,get_improve2, find_bestIndividual) #100 is population.
bestIndividual = bestIndividuals[-1]
#get gene of bestIndividual
print('sequence decision')
print(bestIndividual.Genes[0][:])
print('machine selection decision')
print(bestIndividual.Genes[1][:])
#write the genes presentation in excel file.
sequenceDecision = bestIndividual.Genes[0][:]
machineSelectionDecision = bestIndividual.Genes[1][:]
genePresentation = list(zip(sequenceDecision, machineSelectionDecision))
print(genePresentation)
geneData = pd.DataFrame(genePresentation, columns = ['Job', 'Machine'])
geneData.to_excel('genePresentation.xlsx', index = False)

#print operations and machines selection decision.
machineSelectionPresentation = list(zip(operations, machineSelectionDecision))
print(machineSelectionPresentation)
machineSelectionData = pd.DataFrame(machineSelectionPresentation, columns = ['Operation', 'Machine'])
machineSelectionData.to_excel('machineSelectionData.xlsx', index = False)




#note sequence genes first, machine selection genes later
bestSchedule = get_scheduleResult(bestIndividual.Genes[0], bestIndividual.Genes[1],
                       operations, processingTime, decode_operationSequence)
#print(bestSchedule)


'''
Now you want to use draw function to draw learning curve and grant chart
'''
#drawing learning curve for egine2.
index = []
fitness = []
for i in range(len(bestIndividuals)):
    index.append(i)
    fitness.append(bestIndividuals[i].Fitness.LongestTime)   
draw_lineGraph(index, fitness, 'learning curve populated egine')


#draw grant chart.
schedule = get_scheduleResult(bestIndividual.Genes[0], bestIndividual.Genes[1],
                       operations, processingTime, decode_operationSequence)
print(schedule)
draw_grantChart(schedule,'grant chart example', create_inputData,
                find_sortedJobSet, create_colorCode, create_jobColorDict)




    

            







    

#'''
#from the demand find number of job for each product.
#jobDemand is a dictionary with value is product code.
#value is demand and correspondent number of job.
#'''
#
#def compute_productJob(demand):
#    '''
#    input: demand {'productCode': volume}
#    output: jobDemand {'productCdoe': [volume, numJob]}
#    '''
#    jobDemand = {}
#    for key in demand.keys():
#        jobDemand[key] = [demand[key], round(demand[key]/(500*117*1000))]
#    return jobDemand
#    
#jobDemand = compute_productJob(demand)
#print(jobDemand)
#
#'''
#find the number of job from demand.
#'''
#def compute_totNumJob(jobDemand):
#    '''
#    input: jobDemand {'productCode' [volume, numJob]}
#    output: int total number of job.
#    '''
#    totJob = 0
#    for key in jobDemand.keys():
#        totJob += jobDemand[key][1]
#    return totJob
#    
#totalJob = compute_totNumJob(jobDemand)
#print(totalJob)
#
#def create_stringCode(number):
#    code = ['{0:03}'.format(i) for i in range(number)]
#    return code  
#
#code = create_stringCode(5)
#print(code)
#    
#
#'''
#create job coding with as fellow:
#JB101 or JB212. j-productCoding-jobCoding.
#'''
#def create_jobCoding(jobDemand):
#    '''
#    input jobDemand {'productCode': [volume, numJob]}
#    '''
#    jobCode = []
#    for key in sorted(list(jobDemand.keys())):
#        tempCode = ['J{0}{1:02}'.format(key,i) for i in range(jobDemand[key][1])]
#        jobCode.extend(tempCode)
#    return jobCode
#    
#jobCode = create_jobCoding(jobDemand)
#print(jobCode)
#
#
#
#
#tempList = ['J{0}{1:02}'.format('b2',i) for i in range(5)]
#print(tempList)
#
#print(sorted(list(jobDemand.keys())))
#
#print(keys)
#
#            
#'''
#find the number of job.
#
#'''
#
#for i in range(100):
#    print('{0:03}'.format(i))
#    
#
#    
#'''
#define job.
#each job is define as 500 BBL (the smallest tanks capacity).
#coding for job as follow:
#JProductCodeJobNumber (JB1001)
#job coding is 001 or 111
#'''


    
    
        
    
           
           


