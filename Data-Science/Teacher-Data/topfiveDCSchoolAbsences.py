import csv

#Top 5 overall absences within the DC School District

print "Below are the top five overall absences in the DC School district"
print "These are a combination of elementary school, middle school, and high school"
print "The following are: Miner ES, Ballou SHS, Woodrow Wilson HS, Oyster-Adams Bilingual Elementary School, and Columbia Heights Elementary School"
print ("\n")
print("Top Five Higest DC School District Absences")
print("----------------------------------------------------------")
with open('Teacher-Data-Absenteeism-DC.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if float(row['FTE_ABSENT']) >= 29:
            print row
           #print str(row['LEA_NAME'])
           #print float(row['FTE_ABSENT'])
