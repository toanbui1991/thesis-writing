# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 00:28:15 2017

@author: User
"""
import random 
from datetime import datetime  #to dealing with date format and date data type
from datetime import timedelta  # to dealing with time dealta.

#setting the drawing tool, plottly.
import plotly 
plotly.tools.set_credentials_file(username='toanbui1991', api_key='2fG5m417Upv2albUpc5Y')
#package for drawing line.
import plotly.plotly as py
from plotly.graph_objs import *
#package for drawing grant chart.
import plotly.plotly as py
import plotly.figure_factory as ff

'''
develop function to drawing line graph.
'''

#trace0 = Scatter(
#    x=[1, 2, 3, 4],
#    y=[10, 15, 13, 17]
#)
#trace1 = Scatter(
#    x=[1, 2, 3, 4],
#    y=[16, 5, 11, 9]
#)
##note the data step is a must.
#data = Data([trace0])
#py.plot(data, filename = 'one line example')

def draw_lineGraph(x, y, filename):
    '''
    x is a list for coordinate x.
    y is a list for coordinate y.
    filename is a string
    return single line plot in plotly cloude.    
    '''
    line = Scatter(x = x[:], y = y[:])
    data = Data([line])
    py.plot(data, filename = filename)
    
#experiment with draw_lineGraph.
#x = [1, 2, 3, 4]
#y = [10, 15, 13, 17]
#
#draw_lineGraph(x, y, 'one line example 2')

    
'''
develop the drawing grant chart function.
'''
    
    
#bestSchedule1 = {('O73', 'M4'): (13.0, 16.0), ('O33', 'M1'): (15.0, 16.0), ('O81', 'M1'): (0.0, 2.0), ('O12', 'M3'): (9.0, 14.0), ('O71', 'M5'): (0.0, 7.0), ('O52', 'M4'): (5.0, 9.0), ('O62', 'M7'): (4.0, 10.0), ('O54', 'M6'): (11.0, 16.0), ('O41', 'M8'): (0.0, 4.0), ('O23', 'M6'): (5.0, 9.0), ('O83', 'M1'): (6.0, 15.0), ('O53', 'M6'): (9.0, 11.0), ('O82', 'M2'): (2.0, 6.0), ('O61', 'M3'): (3.0, 4.0), ('O72', 'M8'): (7.0, 12.0), ('O51', 'M1'): (2.0, 5.0), ('O42', 'M7'): (10.0, 16.0), ('O21', 'M3'): (0.0, 3.0), ('O32', 'M4'): (9.0, 13.0), ('O84', 'M5'): (15.0, 16.0), ('O63', 'M2'): (10.0, 15.0), ('O11', 'M2'): (6.0, 9.0), ('O13', 'M6'): (16.0, 18.0), ('O22', 'M4'): (3.0, 5.0), ('O43', 'M3'): (16.0, 18.0), ('O24', 'M5'): (9.0, 13.0), ('O31', 'M7'): (0.0, 2.0)}
#print(bestSchedule1)

'''
create the input data for the plotting function.
the data is a list of dictionary like this.
df = [
    dict(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00', Resource='Sleep'),
    dict(Task='Breakfast', Start='2016-01-01 7:00:00', Finish='2016-01-01 7:30:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 9:00:00', Finish='2016-01-01 11:25:00', Resource='Brain'),
    dict(Task='Break', Start='2016-01-01 11:30:00', Finish='2016-01-01 12:00:00', Resource='Rest'),
    dict(Task='Lunch', Start='2016-01-01 12:00:00', Finish='2016-01-01 13:00:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 13:00:00', Finish='2016-01-01 17:00:00', Resource='Brain'),
    dict(Task='Exercise', Start='2016-01-01 17:30:00', Finish='2016-01-01 18:30:00', Resource='Cardio'), 
    dict(Task='Post Workout Rest', Start='2016-01-01 18:30:00', Finish='2016-01-01 19:00:00', Resource='Rest'),
    dict(Task='Dinner', Start='2016-01-01 19:00:00', Finish='2016-01-01 20:00:00', Resource='Food'),
    dict(Task='Evening Sleep', Start='2016-01-01 21:00:00', Finish='2016-01-01 23:59:00', Resource='Sleep')
]
'''

def compute_date(timeDelta):
    '''
    timeDealta is a decimal number.
    return the date after to day.
    '''
    today = datetime.now()
    timeDelta = timedelta(days = timeDelta)
    return today + timeDelta
    



##create date time string
#import datetime
#d = datetime.datetime(2010, 7, 4, 12, 15, 58)
#'{:%Y-%m-%d %H:%M:%S}'.format(d)
##'2010-07-04 12:15:58' 
#create data and time string in format of plotly.
#def create_timeStr(year, month, date, hour, minute, second):
#    '''
#    return dateTime string.
#    '''
#    time = datetime.datetime(year, month, date, hour, minute, second)
#    return '{:%Y-%m-%d %H:%M:%S}'.format(time)
    
#print(create_timeStr(2017, 4, 25, 15, 0  , 0))

#create input data for grant chart plotly function.
#Since grant chart plotly function need specifict input data.
def create_inputData(schedule, compute_date):
    '''
    schedule is a dictionary with key is (operation, machine).
    value is (start, finish) and will be like this.
    {('O73', 'M4'): (13.0, 16.0), ('O33', 'M1'): (15.0, 16.0)}.
    return a list of dictionary like this.
    df = [
    dict(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00', Resource='Sleep'),
    dict(Task='Breakfast', Start='2016-01-01 7:00:00', Finish='2016-01-01 7:30:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 9:00:00', Finish='2016-01-01 11:25:00', Resource='Brain')
    ]
    '''
    df = []
    for key, value in sorted(schedule.items()):
        tempDict = {}
        tempDict['Task'] = key[1]
        tempDict['Job'] = key[0][:-1]
        tempDict['Start'] = compute_date(value[0])
        tempDict['Finish'] = compute_date(value[1])
        df.append(tempDict)
    return df
#inputData = create_inputData(schedule, compute_date)
#print(inputData)

#create color dictionary for operation.


#find the set of uinique operation from schedule.
#bestSchedule1.keys()
#def find_sortedOperationSet(schedule):
#    '''
#    input is schedule, output is a sorted set of operations.
#    '''
#    operationList = []
#    for key in schedule.keys():
#        operationList.append(key[0])
#    sortedOperationSet = sorted((set(operationList)))
#    return sortedOperationSet
#    
#sortedOperationSet = find_sortedOperationSet(bestSchedule1)
#print(sortedOperationSet)

def find_sortedJobSet(schedule):
    jobsList = []
    for key in schedule.keys():
        jobsList.append(key[0][:-1])
    sortedJobsSet = sorted(jobsList)
    return sortedJobsSet
    
#sortedJobsSet = find_sortedJobSet(schedule)
#print(sortedJobsSet)
        

#create color dictionary.
def create_colorCode():
    input1 = random.randint(0, 250)
    input2 = random.randint(0, 250)
    input3 = random.randint(0, 250)
    return 'rgb({0}, {1}, {2})'.format(input1, input2, input3)
    
#colorCode1 = create_colorCode()
#print(colorCode1)
#create color dictionary for operation.


    
#operationColorDict = create_operationColorDict(sortedOperationSet, create_colorCode)
#print(operationColorDict)
def create_jobColorDict(sortedJobsSet, create_colorCode):
    jobColorDict = {}
    for j in sortedJobsSet:
        jobColorDict[j] = create_colorCode()
    return jobColorDict
    
#jobColorDict = create_jobColorDict(sortedJobsSet, create_colorCode)
#print(jobColorDict)

#create grawing grant chart function.

def draw_grantChart(schedule,filename, create_inputData, find_sortedOperationSet,
                    create_colorCode, create_jobColorDict):
    '''
    schedule is a dictionary.
    filename is a string of the grant chart name.
    '''
    inputData = create_inputData(schedule, compute_date)
    sortedJobSet = find_sortedJobSet(schedule)
    jobColorDict = create_jobColorDict(sortedJobSet, create_colorCode)
    fig = ff.create_gantt(inputData, colors=jobColorDict, index_col='Job',
                          show_colorbar=True, group_tasks=True)
    py.iplot(fig, filename = filename, world_readable=True)
    
#draw_grantChart(schedule,'grant chart example', create_inputData,
#                find_sortedJobSet, create_colorCode, create_jobColorDict)
    

 



#----------------------------------------------------------------------------



 

 