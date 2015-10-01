import csv 
import matplotlib.pyplot as plt

#This depicts a pie chart of the top highest five school absences with the DC School District

fig = plt.figure()
fig.suptitle('Top Five DC Schools Highest Absences', fontsize=16)

values = [29, 31, 41, 46, 53.5] 
labels = ['Miner ES', 'Oyster Adams Bilingual EC', 'Columbia Heights EC', 'Ballou SHS', 'Woodrow Wilson HS'] 
def my_autopct(pct):
    total=sum(values)
    val=int(pct*total/100.0)
    return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)

plt.pie(values, labels=labels, autopct=my_autopct)
plt.show()
