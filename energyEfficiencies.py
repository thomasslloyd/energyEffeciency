# battery effeciency calc of testla model s 85kw/h
import matplotlib.pyplot as plt
import numpy as np

# https://forum.abetterrouteplanner.com/blogs/entry/13-model-3-consumption-and-charging/
# https://forum.abetterrouteplanner.com/blogs/entry/10-tesla-model-x-consumption-vs-speed/
# https://forum.abetterrouteplanner.com/blogs/entry/9-tesla-model-s-consumption-vs-speed/

# INSTANTIATION
mass = 2250
speed = np.array([10, 15, 20, 25, 30, 35, 40, 45]) # in km/h
speedms = speed*(1/3.6) # in m/s
print("speeds in m/s: ", speedms)

# CALCS
delta_d = np.zeros([speed.shape[0]])
for n in range(0, speed.shape[0]):
    delta_d[n] = 1000
print("distances covered for example: ", delta_d)

# BATTERY CONSUMPTION
battery_consumption = np.array([225, 190, 180, 180, 185, 200, 220, 225]) # in watt hours
timefor1000 = delta_d/speed
print("time to cover distance: ", timefor1000)

timefor1000hours = timefor1000/(60*60)
print("time to cover distance in hours: ", timefor1000hours)

# energy in: energy given by battery over distance
energyin = battery_consumption/timefor1000hours

# energy out: mechanical work done
energyout = (.5)*mass*(speedms**2)

# x = np.linspace(0, 2, 100)

plt.plot(speedms, battery_consumption, label='Model S 85kw')
plt.xlabel('speed')
plt.ylabel('battery_consumption')
plt.title("battery consumption vs speed")
plt.legend()
plt.show()

plt.plot(speed, (energyin/energyout), label='Model S 85kw effeciencies')
plt.xlabel('speed')
plt.ylabel('effeciency')
plt.title("battery consumption vs speed")
plt.legend()


plt.show()
