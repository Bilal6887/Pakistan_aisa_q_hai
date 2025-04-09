import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('milestone2.csv')
columnNames = list(df.head(0))
myData = df.values
myDataDict = {}
i = 0
for column in columnNames:
    myDataDict[column] = myData[:,i]
    i += 1

plt.plot(myDataDict['Year'],myDataDict['Pakistan'],'green', label="Pakistan")
plt.plot(myDataDict['Year'],myDataDict['India'],'red', label="India")
plt.plot(myDataDict['Year'],myDataDict['China'],'blue', label="China")

plt.title('Avg. Inflation')
plt.legend(loc="best")
plt.show()
# Use myDataDict appropriately to compute the average inflation per country and then output their ranked order through print.
# Use as many helper functions from your milestone 1, as required!
# Can you use a different kind of plot (other than a line plot) to show your answer to the 'susta' question?