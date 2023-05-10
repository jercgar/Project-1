#Project 1 - Dataset

#setting up the imports
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style



#VDS = Valorant Data Set
VDS = pd.DataFrame(pd.read_csv('Book1.csv'))
print(VDS)

#obtaining the win AVG from a separate sheet
Win = pd.read_excel("WinAVG.xlsx")
x = list(Win['Guns'])
y = list(Win['AVG Win'])

#creating the scatter plot
plt.figure(figsize=(20,20))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="red")
plt.title("Valorant Gun Win AVG")
plt.show()
		
#Obtaining the pick AVG from a separate sheet
Pick = pd.read_excel("PickAVG.xlsx")
x = list(Pick['Guns'])
y = list(Pick['AVG Pick'])

#creating the scatter plot
plt.figure(figsize=(20,20))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="red")
plt.title("Valorant Gun Pick AVG")
plt.show()
