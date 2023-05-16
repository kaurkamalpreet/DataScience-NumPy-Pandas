import pandas as pd

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])

# print(totals)
# print(counts)

# lowest total precipitation over the year
print("City with lowest total precipitation:")
print(totals.sum(axis='columns').idxmin())


# average precipitation of these locations for each month
print("Average precipitation in each month:")
print(totals.sum()/counts.sum())

# average precipitation for each city
print("Average precipitation in each city:")
print(totals.sum(axis='columns')/counts.sum(axis='columns'))


