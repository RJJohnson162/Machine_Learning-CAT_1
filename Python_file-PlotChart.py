import matplotlib.pyplot as plt

from Python_file import train_data

# Plot sensor trends for a single engine
engine_id = 1
engine_data = train_data[train_data['id'] == engine_id]

plt.figure(figsize=(12, 6))
for sensor in ['s1', 's2', 's3', 's4']:
    plt.plot(engine_data['cycle'], engine_data[sensor], label=sensor)
plt.xlabel('Cycle')
plt.ylabel('Sensor Value')
plt.title(f'Sensor Trends for Engine {engine_id}')
plt.legend()
plt.show()