import sys
import platform

print(f"Python version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Machine: {platform.machine()}")

# Simulation d'un mini script ML
data = [1, 2, 3, 4, 5]
mean = sum(data) / len(data)
print(f"Moyenne des données: {mean}")
