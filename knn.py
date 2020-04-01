#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: katherinemichalski
Reads data quality files and 
"""

# Python3 program to find groups of unknown 
# Points using K nearest neighbour algorithm. 

import math
import csv

def getData(file='winequality-white.csv'):
    def convert(value):
        try:
            return(int(value))
        except:
            try:
                return(float(value))
            except:
                return(value)
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            for key in row.keys():
                row[key] = convert(row[key])
            data.append(row)
            #print(len(data))
    print("Read {} records.".format(len(data)))
    return(data)



def classifyAPoint(points,p,k=3): 
	''' 
	This function finds the classification of p using 
	k nearest neighbor algorithm. It assumes only two 
	groups and returns 0 if p belongs to group 0, else 
	1 (belongs to group 1). 

	Parameters - 
		points: Dictionary of training points having two keys - 0 and 1 
				Each key have a list of training data points belong to that 

		p : A tuple, test data point of the form (x,y) 

		k : number of nearest neighbour to consider, default is 3 
	'''

	distance=[] 
	for group in points: 
		for feature in points[group]: 

			#calculate the euclidean distance of p from training points 
			euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2) 

			# Add a tuple of form (distance,group) in the distance list 
			distance.append((euclidean_distance,group)) 

	# sort the distance list in ascending order 
	# and select first k distances 
	distance = sorted(distance)[:k] 

	freq1 = 0 #frequency of group 0 
	freq2 = 0 #frequency og group 1 

	for d in distance: 
		if d[1] == 0: 
			freq1 += 1
		elif d[1] == 1: 
			freq2 += 1

	return 0 if freq1>freq2 else 1

# driver function 
def main(): 

	# Dictionary of training points having two keys - 0 and 1 
	# key 0 have points belong to class 0 
	# key 1 have points belong to class 1 

	points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)], 
			1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]} 

	# testing point p(x,y) 
	p = (5,5) 

	# Number of neighbours 
	k = 3

	print("The value classified to unknown point is: {}".
		format(classifyAPoint(points,p,k))) 

if __name__ == '__main__': 
	main() 
	
