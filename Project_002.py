import matplotlib.pyplot as plt
import numpy as np
import json 
import csv 
import pandas as pd

us_population = []
with open('/Users/stephanie/Desktop/CSCI040/us_population.json') as f:  
    text = f.read()
us_population = json.loads(text)
us_population = us_population[1]
years = []
value= []
for us_pop in us_population:
    value.append(us_pop['value'])
    years.append(us_pop['date'])
us_fv = value[::-1]
us_fy = years[::-1]


china_population = []
with open('/Users/stephanie/Desktop/CSCI040/china_population.json') as f:   
    text = f.read()
china_population = json.loads(text)
china_population = china_population[1]
c_years = []
c_value= []
for china_pop in china_population:
    c_value.append(china_pop['value'])
    c_years.append(china_pop['date'])
c_fv = c_value[::-1]
c_fy = c_years[::-1]


plt.plot(us_fy, us_fv, label = 'United States Population')
plt.plot(c_fy, c_fv, label = 'China Population')

plt.xticks(rotation = 90, fontsize = 5.2)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title ('United States Population vs. China Population')
plt.legend()
plt.show()


# pie chart 

with open('/Users/stephanie/Desktop/CSCI040/NCHS_-_Leading_Causes_of_Death__United_States.csv') as f:  
    spreadsheet=list(csv.reader(f))

unintentional_injuries = 0
alzheimers_disease = 0
stroke = 0
clrd = 0
diabetes = 0
heart_disease = 0
influenza_and_pneumonia = 0
suicide = 0
cancer = 0
kidney_disease = 0



for row in spreadsheet:
    if row[0] == '2017':
        if row[3]== 'United States':
            if row[2] == "Unintentional injuries":
                unintentional_injuries = row[4]
            if row[2] == "Alzheimer's disease":
                alzheimers_disease = row[4]
            if row[2] == "Stroke":
                stroke = row[4]
            if row[2] == "CLRD":
                clrd = row[4]     
            if row[2] == "Diabetes":
                diabetes = row[4]     
            if row[2] == "Heart disease":
                heart_disease = row[4]     
            if row[2] == "Influenza and pneumonia":
                influenza_and_pneumonia = row[4] 
            if row[2] == "Suicide":
                suicide = row[4] 
            if row[2] == "Cancer":
                cancer = row[4] 
            if row[2] == "Kidney disease":
                kidney_disease = row[4]

cause_data = ["Unintentional injuries","Alzheimer's disease","Stroke","CLRD","Diabetes","Heart disease","Influenza and pneumonia","Suicide","Cancer","Kidney disease"]
incident_data = [unintentional_injuries, alzheimers_disease, stroke, clrd, diabetes, heart_disease, influenza_and_pneumonia, suicide, cancer, kidney_disease] 
plt.pie(incident_data, labels=cause_data)
plt.title("Leading Causes of Death in the United States in 2017")
plt.show()
