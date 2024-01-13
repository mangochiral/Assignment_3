import numpy as np
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
titan_test = pd.read_csv('tit_test.csv')
titan_train = pd.read_csv('tit_train.csv')
# Provides summary of the CSV files
print(titan_test.describe())
print(titan_train.describe())

# Concates both the CSV files and provides summary of the merged CSV file
titan_merge = pd.concat([titan_train,titan_test], ignore_index=True)
print(titan_merge.describe())

# Removes any row having Nan data for in the column Age
Age_merge= titan_merge.dropna(subset=['Age'])
# Distribution of Age VS survival rate
sns.histplot(data= Age_merge, x= 'Age')
plt.title("Age Distribution of Passengers in Titanic")
plt.xlabel('Passengers Age')
plt.ylabel('Passengers Distribution')
plt.show()
print("There were more Passenger of the Age group 20-30 then rest.")


# Removes any row having Nan data for in the column Age and Survived
Age_survive_merge = titan_merge.dropna(subset=['Age', 'Survived'])
# Distribution plot for age vs survival rate
sns.histplot(data= Age_survive_merge, x= 'Age', hue= 'Survived')
plt.title("Age VS Survival rate Distribution")
plt.xlabel('Passengers Age')
plt.ylabel('Passengers Survival Distribution')
plt.show()
print("The Survival among infants were significantly high.")

# Removes any row having Nan data for in the column Sex and Survived
survive_gender_merge = titan_merge.dropna(subset=['Sex','Survived'])

survival_rate = survive_gender_merge['Survived'].value_counts(normalize=True)
survival_rate.plot.bar(x='Survived', y='proportion', color = 'skyblue', rot=0)
plt.title("Survival rate")
plt.xlabel('Survivors Type')
plt.xticks([0,1],['Dead', 'Alive'])
plt.ylabel('Ratio')
plt.show()
print("The Death rate was high is the titanic accident and less the 40% change of survival.")


male_survive = survive_gender_merge.loc[survive_gender_merge['Sex'] == 'male']['Survived'].value_counts()
female_survive = survive_gender_merge.loc[survive_gender_merge['Sex'] == 'female']['Survived'].value_counts()
sur_rate = [male_survive[0.0], male_survive[1.0], female_survive[0.0], female_survive[1.0]]
passenger = 0
for i in sur_rate:
    passenger = passenger + i
y = [i/passenger for i in sur_rate]
y1 = y[:2]
y2 = y[2:]
x1 = ['Male Dead', 'Male Alive']
x2 = [ 'Female Dead', 'Female Alive']
plt.bar(x1,y1,color = "red", label = 'Male')
plt.bar(x2,y2,color = "orange", label = 'Female')
plt.title("Survival rate VS Gender")
plt.xlabel("Passenger Gender")
plt.ylabel("Ratio")
plt.legend()
plt.show()

print("The Death among male passengers were more than female passengers")

# Removes any row having Nan data for in the column Pclass and Survived
passenger_merge = titan_merge.dropna(subset=['Pclass', 'Sex', 'Survived'])
sns.barplot(data=passenger_merge, x= 'Pclass', y= 'Survived', hue= 'Sex')
plt.xticks([0,1,2],['First Class','Second Class','Third class'])
plt.title("Survival rate VS Gender VS Class of Passenger")
plt.xlabel('Passengers Type')
plt.ylabel('Ratio')
plt.show()

print("Being rich as its merits, because the survival rate among first passengers were higher")
