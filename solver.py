import numpy as np

print("================================")
print("   Python MNA Circuit Solver")
print("================================")
print()

# Get components from user
netlist = []
num_components = int(input("How many components do you have? "))

for i in range(num_components):
    print(f"\nComponent {i+1}:")
    comp_type = input("Type (R for resistor, V for voltage source): ").upper()
    name = input("Name (e.g. R1, V1): ")
    n1 = int(input("Node + : "))
    n2 = int(input("Node - : "))
    value = float(input("Value (ohms for R, volts for V): "))
    netlist.append((comp_type, name, n1, n2, value))

# Step 1: find all nodes
nodes = set()
for component in netlist:
    nodes.add(component[2])
    nodes.add(component[3])
nodes.discard(0)
nodes = sorted(nodes)
n = len(nodes)

# Step 2: find voltage sources
voltage_sources = []
for component in netlist:
    if component[0] == 'V':
        voltage_sources.append(component)
m = len(voltage_sources)

# Step 3: build empty matrix and vector
size = n + m
G = np.zeros((size, size))
b = np.zeros(size)

# Step 4: helper function
def node_index(node):
    if node == 0:
        return -1
    return nodes.index(node)

# Step 5: stamp resistors
for component in netlist:
    if component[0] == 'R':
        name, n1, n2, value = component[1], component[2], component[3], component[4]
        g = 1.0 / value
        i = node_index(n1)
        j = node_index(n2)
        if i >= 0:
            G[i][i] += g
        if j >= 0:
            G[j][j] += g
        if i >= 0 and j >= 0:
            G[i][j] -= g
            G[j][i] -= g

# Step 6: stamp voltage sources
for idx, component in enumerate(voltage_sources):
    name, n1, n2, value = component[1], component[2], component[3], component[4]
    i = node_index(n1)
    j = node_index(n2)
    row = n + idx
    if i >= 0:
        G[row][i] = 1
        G[i][row] = 1
    if j >= 0:
        G[row][j] = -1
        G[j][row] = -1
    b[row] = value

# Step 7: solve
x = np.linalg.solve(G, b)

# Step 8: print clean results
print()
print("================================")
print("         Results")
print("================================")
for i, node in enumerate(nodes):
    print(f"V(node {node}) = {x[i]:.4f} V")
for idx, component in enumerate(voltage_sources):
    print(f"Current through {component[1]} = {x[n+idx]:.6f} A")
print("================================")

input("\nPress Enter to close...")
