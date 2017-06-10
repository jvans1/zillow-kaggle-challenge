import csv
import numpy as np
train_properties = {}


with open('train_2016.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        train_properties[row['parcelid']] = row

test_data = []
train_data = []
total = 0
with open('properties_2016.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total += 1
        if row["parcelid"] in train_properties:
            row["logerror"] = train_properties[row["parcelid"]]["logerror"]
            row["transactiondate"] = train_properties[row["parcelid"]]["transactiondate"]
            train_data.insert(len(train_data), row)
        else:
            test_data.insert(len(test_data), row)


with open('test_data.csv', 'w') as td:
    writer = csv.DictWriter(td, fieldnames=test_data[0].keys())
    writer.writeheader()
    for row in test_data:
        writer.writerow(row)

train_data = np.array(train_data)
np.random.shuffle(train_data)
print("===========")
print(len(train_data))
print("===========")
validation_set, training_set = np.split(train_data, [12000])
validation_sample =  np.random.choice(validation_set, size=1200, replace=False)
print(len(training_set))
training_sample =  np.random.choice(training_set, size=8000, replace=False)

def write_data(filename, data):
    with open(filename, 'w') as td:
        writer = csv.DictWriter(td, fieldnames=train_data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

write_data("sample/training_data.csv", training_sample)
write_data("sample/validation_data.csv", validation_sample)
write_data("data/validation_data.csv", validation_set)
write_data("data/training_data.csv", training_set)

