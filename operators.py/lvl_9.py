#. Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

# Coordinates
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope formula: (y2 - y1) / (x2 - x1)
slope = (y2 - y1) / (x2 - x1)

# Euclidean distance formula
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Output
print("Slope:", slope)
print("Euclidean distance:", distance)


