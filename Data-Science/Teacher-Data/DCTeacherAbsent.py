import csv
import pandas as pd
from collections import defaultdict

#Reading data from the Teacher data filecsv file
data = pd.read_csv('Teacher-Data-Absenteeism-DC.csv')

print "This is a summary of DC School District data of Teacher Absenteeism"
print ("\n")
print "DC School District Data Summary"
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
#find the overall DC school district sum 
district_sum = data['FTE_ABSENT'].sum()

#find the overall DC school district average
district_mean = data['FTE_ABSENT'].mean()
#find the overall DC School district lowest absence
district_min = data['FTE_ABSENT'].min()

#find the overall DC School district highest absence
district_max = data['FTE_ABSENT'].max()

#find the overall DC School district sum grouped by School District
district_group = data.groupby('LEA_NAME').sum()

#find th overall DC School district average grouped by School District
district_groupmean = data.groupby('LEA_NAME').mean()

print "The overall DC School District sum of absences are: " , district_sum
print " The overall DC School District average of absences are: ", district_mean 
print " The lowest absence for the overall DC School district is: ", district_min
print " The highest absence for the overall DC School district is: ", district_max
print district_group
print district_groupmean
