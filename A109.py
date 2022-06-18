import statistics
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].to_list()

hmean = statistics.mean(data)
hmedian = statistics.median(data)
hmode = statistics.mode(data)
hsd = statistics.stdev(data)
print(hmean)
print(hmedian)
print(hmode)
print(hsd)

h1start,h1end = hmean-hsd,hmean+hsd
h2start,h2end = hmean-(2*hsd),hmean+(2*hsd)
h3start,h3end = hmean-(3*hsd),hmean+(3*hsd)

hlist1 = [result for result in data if result > h1start and result < h1end]
hlist2 = [result for result in data if result > h2start and result < h2end]
hlist3 = [result for result in data if result > h3start and result < h3end]

hp1 = len(hlist1)*100/len(data)
hp2 = len(hlist2)*100/len(data)
hp3 = len(hlist3)*100/len(data)

print("percentage of score within 1 sd - ",hp1)
print("percentage of score within 2 sd - ",hp2)
print("percentage of score within 3 sd - ",hp3)

