#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 03:34:06 2021

@author: daliashaker

Ammar Abou Hamze
Lesrene Browne
Final Project
Nov 30 2021
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
def find_data(filename):
    """
   

    Parameters
    ----------
    filename : string
        is a file that contains the data from 4 leagues 

    Returns
    -------
    data : list
        is a list of all lines relating to the 2019-2020 season

    """
    # opens file, reads lines, and seperates by any commas
    with open(filename, "r") as infile:
       lines = csv.reader(infile, delimiter = ",")
       # creates a data list that will contain all lines relating to 2019-2020
       data = []
       # checks every line for 2019 or 2019/20 and removes anomalies and adds
       # info to the list
       for row in lines:
           row[2] = row[2].replace(u'\xa0', u' ')
           if row[1] == "2019/20" or row[1] == "2019":
               data.append(row)
               
       return data

def league(data):
    """
   

    Parameters
    ----------
    data : list
       is a list of all lines relating to the 2019-2020 season 

    Returns
    -------
    premier_league, la_liga, bundesliga, mls : lists
        these lists contain the lines from the data list 
        pertaining to their respective leagues

    """
    # makes a list for each league
    premier_league = []
    la_liga = []
    bundesliga = []
    mls = []
    
    # adds lines from data list to respective league  
    for row in data:
        if row[0] == "Premier League":
            premier_league.append(row)
        elif row[0] == "La Liga":
            la_liga.append(row)
        elif row[0] == "Bundesliga":
            bundesliga.append(row)
        elif row[0] == "Major League Soccer":
            mls.append(row)
    # these return the data sorted by leagues
    return premier_league, la_liga, bundesliga, mls  

def league_dict(names):
    """
    

    Parameters
    ----------
    data : list
       is a list of all lines relating to the 2019-2020 season  

    Returns
    -------
    pl, ll, bl, ml : dictionaries
        these dictionaries contain the league positions as keys and total 
        points as values from the data list pertaining to their respective 
        leagues


    """
    # makes a dictionary for each league
    premier_league = {}
    la_liga = {}
    bundesliga = {}
    mls = {}
    
    # changes league position & points to integers from data list and adds them 
    # to respective leagues 
    for row in names:
        league_position = int(row[2])
        if row[0] == "Premier League":
            premier_league[league_position] = int(row[11])
        elif row[0] == "La Liga":
            la_liga[league_position] = int(row[11])
        elif row[0] == "Bundesliga":
            bundesliga[league_position] = int(row[11])
        elif row[0] == "Major League Soccer":
            mls[league_position] = int(row[11])
        
        # sorts the dictionaries so the positions will be in ascending order
        pl = dict(sorted(premier_league.items(), key=lambda x: x[1], reverse = True))
        ll = dict(sorted(la_liga.items(), key=lambda x: x[1], reverse = True))
        bl = dict(sorted(bundesliga.items(), key=lambda x: x[1], reverse = True))
        ml = dict(sorted(mls.items(), key=lambda x: x[1], reverse = True))
        
            
            
            
    # these return the data sorted by leagues
    return pl, ll, bl, ml 

def avg(league):
    """
    

    Parameters
    ----------
    league : list
        the list containg the lines for one league

    Returns
    -------
    average : float
        the mean of the total points of all the teams in the league
        put together

    """
    
    # makes a list for the total points from each team, adds points to list
    points = []
    for row in league:
        points.append(row[-1])
    # sorts the points list
    points.sort()
    
    # removes any anomalies
    for x in points:
        if x == "":
            points.remove("")
    
    # changes the list to an array with integer elements
    a = np.array(points).astype(int)
    # finds the mean
    average = sum(a)/len(a)
    
    return average

             

def get_var(league):
    """
   

    Parameters
    ----------
    league : list
        the list containg the lines for one league

    Returns
    -------
    stdv : float
        the standard deviation for total points in a league

    """
    # makes a list for the total points from each team, adds points to list
    points = []
    for row in league:
        points.append(row[-1])
    # sorts the points list
    points.sort(reverse = True)
   
   # removes any anomalies
    for x in points:
        if x == "":
            points.remove("")
    
    # changes the list to an array with float elements
    a = np.array(points).astype(float)
    # finds variance, uses variance to find standard deviation, rounds stdv
    var = np.var(a)
    stdv = (var)**(0.5)
    stdv = round(stdv,3)
   
     
    return stdv

def get_avg_diff(league): 
    """
   
    Parameters
    ----------
    league : list
        the list containg the lines for one league
    Returns
    -------
    difference : float
        the average difference in points between each position
https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
https://stackoverflow.com/questions/47040728/get-average-difference-between-all-numbers-in-a-list-python
    """
    # makes a list for the total points from each team, adds points to list
    points = []
    for row in league:
        points.append(row[-1])
    # sorts the points list
    points.sort()
    
    # changes the list to an array with integer elements
    a = np.array(points).astype(int)
    
    # finds the difference between wach position
    b = [j-i for i, j in zip(a[:-1], a[1:])]
    # finds the average of those differences and rounds it
    length = len(b)
    total = sum(b)
    difference = total/length
    difference = round(difference, 3)
    
    return difference
    
    




def main():
    filename = find_data("/Users/lesrene/Desktop/Datasets/all-leaguetables.csv")
    premier_league_points, la_liga_points, bundesliga_points, mls_points  = league(filename)
    
    premier_league_var = get_var(premier_league_points)
    la_liga_var = get_var (la_liga_points)
    bundesliga_var = get_var(bundesliga_points)
    mls_var = get_var(mls_points)
    
    premier_league_avg = get_avg_diff(premier_league_points)
    la_liga_avg = get_avg_diff(la_liga_points)
    bundesliga_avg = get_avg_diff(bundesliga_points)
    mls_avg = get_avg_diff(mls_points)
    
    

    plap = avg(premier_league_points)
    llp = avg(la_liga_points)
    bdlp = avg(bundesliga_points)
    mlsp = avg(mls_points)
    
    
    


    avgp_dic = {'PL':plap, 'La Liga':llp, 'Bundesliga':bdlp, 'MLS':mlsp}
    var_dic = {'PL':premier_league_var, 'La Liga':la_liga_var, 'Bundesliga':bundesliga_var, 'MLS':mls_var}
    avg_dic = {'PL':premier_league_avg, 'La Liga':la_liga_avg, 'Bundesliga':bundesliga_avg, 'MLS':mls_avg}
    print("The premier league variation is", premier_league_var)
    print(premier_league_avg)
    print(var_dic)
    print(avg_dic)
    
    leagues = list(var_dic.keys())
    variation = list(var_dic.values())
    
    
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(leagues, variation, color ='maroon',
            width = 0.4)
    
    
    plt.xlabel("Leagues")
    plt.ylabel("Variation of Final Points")
    plt.title("The Variation of Final Points in Diffrent Leagues")
    plt.show()
    
    leagues = list(avg_dic.keys())
    average = list(avg_dic.values())
      
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(leagues, average, color ='blue',
            width = 0.4)
    plt.xlabel("Leagues")
    plt.ylabel("Average of the Diffrence between each Position")
    plt.title(" Average of the Diffrence between each Position in Diffrent Leagues")
    plt.show()
    

    leagues = list(avgp_dic.keys())
    average = list(avgp_dic.values())
      
    fig = plt.figure(figsize = (10, 5))
     
    # creating the bar plot
    plt.bar(leagues, average, color ='red',
            width = 0.4)
     
    plt.xlabel("Leagues")
    plt.ylabel("Average of Points")
    plt.title(" Average of Point in Diffrent Leagues")
    plt.show()
    #https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
    #print(premier_league_points)
    
    premier_league, laliga, bundesliga, mls = league_dict(filename)
    
    #print (premier_league)
    

    
    
    plt.plot(list(premier_league.keys()), list(premier_league.values()), marker='o', color='#003366', label='PL')
    plt.axhline(y=plap, color='#6684a3', linestyle='--')
    plt.axhline(y=plap + 17.33, color='#6684a3', linestyle='--')
    plt.axhline(y=plap - 17.33, color='#6684a3', linestyle='--')
    plt.xlabel('Positions')
    plt.ylabel('Total Points')
# title of a plot
    plt.title('League Position vs Points Comparison')
# explanation(symbol) for a graph
    plt.legend()
# This will pop up the graph
    plt.show()
    

   
    plt.plot(list(bundesliga.keys()), list(bundesliga.values()), marker='o', color='#be4038', label='Bundesliga')
    plt.axhline(y=bdlp, color='#d88c87', linestyle='--')
    plt.axhline(y=bdlp + 15.7 , color='#d88c87', linestyle='--')
    plt.axhline(y=bdlp - 15.7 , color='#d88c87', linestyle='--')
    plt.xlabel('Positions')
    plt.ylabel('Total Points')
# title of a plot
    plt.title('League Position vs Points Comparison')
# explanation(symbol) for a graph
    plt.legend()
# This will pop up the graph
    plt.show()
    

   
    plt.plot(list(laliga.keys()), list(laliga.values()), marker='o', color='purple', label='La Liga')
    plt.axhline(y=llp, color='darkviolet', linestyle='--')
    plt.axhline(y=llp + 15.72 , color='darkviolet', linestyle='--')
    plt.axhline(y=llp - 15.72 , color='darkviolet', linestyle='--')
    plt.xlabel('Positions')
    plt.ylabel('Total Points')
# title of a plot
    plt.title('League Position vs Points Comparison')
# explanation(symbol) for a graph
    plt.legend()
# This will pop up the graph
    plt.show()
    

   
    plt.plot(list(mls.keys()), list(mls.values()), marker='o', color='green', label='MLS')
    plt.axhline(y=mlsp, color='palegreen', linestyle='--')
    plt.axhline(y=mlsp + 10 , color='palegreen', linestyle='--')
    plt.axhline(y=mlsp - 10 , color='palegreen', linestyle='--')
   
    plt.xlabel('Positions')
    plt.ylabel('Total Points')
# title of a plot
    plt.title('League Position vs Points Comparison')
# explanation(symbol) for a graph
    plt.legend()
# This will pop up the graph
    plt.show()
    
    #print(plap, bdlp, mlsp, llp)
    

main()
