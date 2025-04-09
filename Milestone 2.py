import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
df = pd.read_csv('E:\QCR\milestone2.csv')
Headingnames=list(df.head(0))

Allvalues = df.values
Alllists = {}
i=0
for heading in Headingnames:
    Alllists[heading]= Allvalues[:,i]
    i+=1
    #print(Alllists)
Headingnames.pop(0)
def totalavginflation(countrydata):
    sum = 0
    for j in range(len(countrydata)):
        sum = sum + countrydata[j]
        avg = sum / len(countrydata)
    return avg
totalaverage=[]
for country in Headingnames:
    x = Alllists[country]
    totalaverage.append(totalavginflation(x))
#print(totalaverage)
def sorting_list(totalavg):
    sorted_list=[]
    sorted_indices = []
    for M in range(len(totalavg)):
        chota = totalavg[0]
        index = 0
        for N in range(len(totalavg)):
            if totalavg[N] < chota:
                chota = totalavg[N]
                index = N
        sorted_list.append(chota)
        totalavg[index]=1000
        sorted_indices.append(index)
    return sorted_list,sorted_indices
sorted_list,sorted_indices=sorting_list(totalaverage)
rank =0
for i in range(len(sorted_indices)):
    rank += 1
    print ("sasta country",rank ,"goes to ",Headingnames[sorted_indices[i]],"with average inflation ",sorted_list[i])
#colors=["Green","Orange","Red","Violet","Blue","Yellow","Purple"]
for Z in range(len(Headingnames)):

    plt.plot(Alllists['Year'],Alllists[Headingnames[Z]], label=Headingnames[Z])
plt.xlabel('Years')
plt.ylabel('Average inflation')
plt.title('Inflation Average over the year')
plt.legend(loc="best")

plt.show()