import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

# ---------------- Parameters ----------------
grid_size = 3
theta = 0.35  # Resonance threshold
weights = np.array([1.0, 2.0, 0.4])  # (Linear, Cyclic, Subjective)
origin = (0, 0, 0)
target = (2, 2, 2)
max_attempts = 20

# ---------------- Resonant Graph Builder ----------------
def generate_lattice_and_graph():
    lattice = {}
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):
                v = np.random.randn(3)
                v /= np.linalg.norm(v)
                lattice[(x, y, z)] = v

    G = nx.Graph()
    G.add_nodes_from(lattice.keys())

    def edge_weight(a, b):
        delta = np.array(a) - np.array(b)
        return np.sqrt(np.sum(weights * delta**2))

    for t1 in lattice:
        for t2 in lattice:
            if t1 != t2 and sum(abs(np.array(t1) - np.array(t2))) == 1:
                psi1, psi2 = lattice[t1], lattice[t2]
                if np.dot(psi1, psi2)**2 > theta:
                    G.add_edge(t1, t2, weight=edge_weight(t1, t2))
    return G, lattice

# ---------------- Retry Loop ----------------
for attempt in range(max_attempts):
    G, lattice = generate_lattice_and_graph()
    if origin in G and target in G and nx.has_path(G, origin, target):
        path = nx.dijkstra_path(G, origin, target)
        break
else:
    raise RuntimeError(f"No resonant path found between {origin} and {target} after {max_attempts} attempts.")

# ---------------- Save Path ----------------
np.savetxt("minimal_path_nodes.csv", np.array(path), fmt="%d", delimiter=",")

# ---------------- Plotting ----------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')

# Light lattice grid
for i in range(grid_size):
    for j in range(grid_size):
        for k in range(grid_size):
            ax.plot([i, i], [j, j], [0, grid_size - 1], color="gray", alpha=0.08)
            ax.plot([i, i], [0, grid_size - 1], [k, k], color="gray", alpha=0.08)
            ax.plot([0, grid_size - 1], [i, i], [k, k], color="gray", alpha=0.08)

# Resonant path
x, y, z = zip(*path)
ax.plot(x, y, z, marker='o', color='blue', linewidth=2, label='Resonant path')

# Node annotations
for i, (xi, yi, zi) in enumerate(path):
    ax.text(xi + 0.05, yi + 0.05, zi + 0.05, str(i), fontsize=9, color='navy', weight='bold')

# Start/Target
ax.scatter(*origin, color='green', s=100, label='Start')
ax.scatter(*target, color='red', s=100, label='Target')

# Camera view
ax.view_init(elev=22, azim=135)

# Axis ticks
ax.set_xlim(0, grid_size - 1)
ax.set_ylim(0, grid_size - 1)
ax.set_zlim(0, grid_size - 1)
ax.set_xticks([0, 1, 2])
ax.set_yticks([0, 1, 2])
ax.set_zticks([0, 1, 2])

# ---------------- ✅ PROFESSIONAL AXIS LABELS ----------------
ax.set_xlabel("Linear time", labelpad=14, fontsize=11, fontweight='bold', color='black')
ax.set_ylabel("Cyclic time", labelpad=14, fontsize=11, fontweight='bold', color='teal')
ax.set_zlabel("Subjective time", labelpad=14, fontsize=11, fontweight='bold', color='orange')

# Title and legend
ax.set_title("Minimal Resonant Path in Time Lattice", pad=20)
ax.legend(loc='upper left')
plt.tight_layout()

# Export
plt.savefig("../figures/fig_minpath_with_labels.png", dpi=300)
plt.show()