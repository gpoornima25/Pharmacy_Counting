
# coding: utf-8

# In[2]:

import csv
import os
import sys
infile = sys.argv[1]
outfile = sys.argv[2]
reader = csv.reader(open(infile, 'r'), delimiter=',')
next(reader, None) #skip header row
records = []

#loading data
for row in reader:
    records.append(row)

    
# loading variables in an array
n=len(records)
prescription_data = [[0, '', '', 0] for j in range(n)]
for i in range(n):
    #ID
    prescription_data[i][0] = records[i][0] 
    #prescriber full name = prescriber_last_name+prescriber_first_name
    prescription_data[i][1] = records[i][1] + ' ' + records[i][2]
    #drug_name
    prescription_data[i][2] = records[i][3]
    #drug_cost
    prescription_data[i][3] = records[i][4]
    
#finding unique drug names and sorting them 
Dict = {}
for Data in prescription_data:
       Dict.setdefault(Data[2], []).append(Data)
drug_names= list(Dict.keys())
drug_names.sort()

num_drugs=len(drug_names)

num_prescriber=[0]*(num_drugs)
total_cost=[0]*(num_drugs)

for j in range(num_drugs):
    num=len(Dict[drug_names[j]])
    prescriber_names=[0]*(num)
    
    for i in range(num):

        # finding total drug cost
        (Dict[drug_names[j]])[i][3]=float((Dict[drug_names[j]])[i][3])
        total_cost[j] += (Dict[drug_names[j]])[i][3]

        # finding unique unumber of prescribers
        prescriber_names[i]=(Dict[drug_names[j]])[i][1]
    names_sorted=list(set(prescriber_names))
    num_prescriber[j]=len(names_sorted)

# top_cost_drug array and sorting
top_cost_drug = [['', 0, 0] for j in range(num_drugs)]

for j in range(num_drugs):
    #drug_name
    top_cost_drug[j][0] = drug_names[j]
    #num_prescriber
    top_cost_drug[j][1] = num_prescriber[j]
    #total_cost
    top_cost_drug[j][2] = int(total_cost[j])

#sorting based on top cost
top_cost_drug.sort(key=lambda row: row[2], reverse=True)

# adding labels
header = ["drug_name", "num_prescriber", "total_cost"]
top_cost_drug.insert(0,header)

#writing to text file
with open(outfile, "w") as output:
    csv_writer = csv.writer(output)
    csv_writer.writerows(top_cost_drug)

