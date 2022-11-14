import pandas as pd
import numpy as np
import random
import string

#Reads in the list of names (stored as a Data Frame)
namesDF = pd.read_csv("randomnames.csv")

#Sets a random seed for predictible random results
random.seed(0)

#Creates a list of names from the imported Data Frame
names = namesDF['Name']

#Assigning an empty list to be filled with ID numbers
idno_list = []

#Creates a random arrangement of strings and integers 6 characters long for each name in the list, and appends to the empty list
for name in names:
    idno = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    idno_list.append(idno)
    
#Creates a dictionary pairing the name list to the newly created ID list
dic = {names[i]: idno_list[i] for i in range(len(idno_list))}

#Adds the IDs to the initial dataframe in a column entitled "ID" by dictionary pairing (name:ID)
namesDF['ID'] = namesDF['Name'].map(dic)

#Sets the name column as the index
namesDF = namesDF.set_index('Name')

#prints the resulting Data Frame
print(namesDF)

#Exports the data frame as an xlsx file to your working directory
namesDF.to_excel("name.xlsx")
