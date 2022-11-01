import numpy as np
import matplotlib.pyplot as plt

meteors = np.loadtxt("meteors.csv", delimiter=',',
                   skiprows=1, dtype="int")

# mass,year,reclat,reclong

# heaviest
print(max(meteors[:,0]))

# lightest
print(min(meteors[:,0]))

# average weight
print(np.mean(meteors[:,0]))

# percent of meteors > 1000g
over1000 = np.count_nonzero(meteors[:,0] > 1000)
print(over1000/len(meteors[:,0]))

# percent in northern hemisphere
# Note: negative latitudes represent the southern hemisphere,
# and negative longitudes represent the western hemisphere

northern = np.count_nonzero(meteors[:,2]<0)
print(northern/len(meteors[:,2]))


# number of meteors per year
years, counts = np.unique(meteors[:,1], return_counts=True)
print(years, counts)

# plot meteors per year
plt.plot(years,counts)
plt.title("Meteors per year")
plt.show()

# plot histogram of mass
print(meteors[:,0])
plt.hist(meteors[:,0], range=(0,1000), bins=10)
plt.show()

# plot lat/long
plt.plot(meteors[:,3], meteors[:,2], "*")
plt.title("Meteor strikes by location")
plt.show()
