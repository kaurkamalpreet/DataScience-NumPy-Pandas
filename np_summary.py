import numpy as np
data = np.load('monthdata.npz')
# print(data.files)
totals = data['totals']
counts = data['counts']


# lowest total precipitation over the year
print("Row with lowest total precipitation:")
print(np.argmin(np.sum(totals, axis=1)))

# average precipitation of these locations for each month
print("Average precipitation in each month:")
print(np.sum(totals, axis=0)/np.sum(counts, axis=0))

# average precipitation for each city
print("Average precipitation in each city:")
print(np.sum(totals, axis=1)/np.sum(counts, axis=1))

# total precipitation for each quarter in each city
print("Quarterly precipitation totals:")
numofcities = totals.shape[0]
totals_reshaped = np.reshape(totals,((4*numofcities),3))
quarterlysum = np.sum(totals_reshaped, axis=1)
a = int((quarterlysum.size)/4)

print(np.reshape(quarterlysum, (a, 4)))
