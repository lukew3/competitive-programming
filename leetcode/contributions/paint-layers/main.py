"""
One possible solution is to start at the left side of the wall and simulate painting layers with your brush until the leftmost target value is met. If the value cannot be met, return false. After the right side of the brush reaches the right edge of the wall, check if the layers underneath the brush are correct.
"""
from collections import deque

def solution(layers, k):
    # Return true if brush is of size 1
    if k == 1: return True
    # If brush is bigger than the wall, return True if wall is already correct, False if not
    if k > len(layers): return sum(layers) == 0

    # Use a queue to store history of layers painted
    layers_history = deque([0 for i in range(k-1)])
    # Store the number of values painted on the column under the left edge of the brush
    left_layers = 0

    # Move the brush left until it's right edge hits the right edge of the wall
    for i in range(len(layers)-k):
        # Return False if you have painted more layers than you are targeting
        if layers[i] < left_layers: return False
        # Number of layers to paint in this round is target - current layers on left
        next_layer = layers[i] - left_layers
        # Add the number of layers added this round to the queue
        layers_history.append(next_layer)
        # Add the layers added this round to the layers on the leftmost column
        left_layers += next_layer
        # If you pass a previously painted column, remove the layers added to that column only from the left_layers
        left_layers -= layers_history.popleft()
    
    # Check layers underneath brush
    for j in range(k-1):
        # If left layer is not equal to layers painted on left, return false
        if layers[-k+j] != left_layers:
            return False
        # If still items in layers_history, remove the next column from left_layers
        left_layers -= layers_history.popleft()

    if layers[-1] != left_layers: return False

    # Return true if you made it through all previous checks
    return True


# Test
import sys
n = int(input())
for _ in range(n):
    layers = [int(i) for i in input().split()]
    k = int(input())
    print(solution(layers, k))

