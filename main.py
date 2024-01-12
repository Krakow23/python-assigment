import numpy as np

data = np.loadtxt(fname='NewProject.txt', delimiter=';', skiprows=1)
print (data[0,3])
print (data[1,3])

print (data[0,3]+data[1,3])
sum=0
for i in range (0,3):
    print (data[i,3])
    sum=sum + data[i,3]
print (sum)

data = np.array([
    [1, 0, 20.30, 110.10],
    [2, 201.45, 0, 450.56],
    [3, 56.50, 105, 256.50],
    [4, 0, 157.80, 53.20],
    [5, 0, 20.30, 101.20],
    [6, 0, 0, 248.30],
    [7, 55.90, 125, 72.10],
    [8, 0, 152.20, 46.90]
])

week = data[:, 0]  # Extract the 'Week' column
clothes = data[:, 1]  # Extract the 'Clothes' column
bills = data[:, 2]  # Extract the 'Bills' column
food = data[:, 3]  # Extract the 'Food' column

total_week = np.sum(week)
total_clothes = np.sum(clothes)
total_bills = np.sum(bills)
total_food = np.sum(food)

print("Total week: ", total_week)
print("Total clothes: ", total_clothes)
print("Total bills: ", total_bills)
print("Total food: ", total_food)

import matplotlib.pyplot as plt
date=data[0:,0]
amount=data[0:,3]
plt.plot(date,amount)
plt.ylabel("Amount")
plt.xlabel("Week")

plt.show ()