import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt  # Para los colormaps

# ----------------------------
# 1️⃣ Definir nodos (x, y, z)
# ----------------------------
nodos = np.array([
    [0, 0, 0],    # Nodo 1
    [1, 0, 0],    # Nodo 2
    [1, 1, 0],    # Nodo 3
    [0, 1, 0]     # Nodo 4
])

# Reacciones en nodos (True si hay empotramiento / reacción)
reacciones = [True, False, False, True]

# ----------------------------
# 2️⃣ Definir barras y esfuerzos
# ----------------------------
barras = [
    (0, 1),  # Barra 1
    (1, 2),  # Barra 2
    (2, 3),  # Barra 3
    (3, 0)   # Barra 4
]


# Valores de esfuerzo ficticios
esfuerzos = [50, 120, 80, 100]

# ----------------------------
# 3️⃣ Colormap
# ----------------------------
cmap = plt.get_cmap("coolwarm")  # De azul (bajo) a rojo (alto)

# ----------------------------
# 4️⃣ Crear plotter
# ----------------------------
plotter = pv.Plotter()
plotter.background_color = "white"

# ----------------------------
# 5️⃣ Dibujar nodos
# ----------------------------
for i, nodo in enumerate(nodos):
    color = "green" if reacciones[i] else "red"
    plotter.add_mesh(pv.Sphere(radius=0.05, center=nodo), color=color, name=f"nodo{i+1}")

# ----------------------------
# 6️⃣ Dibujar barras con color según esfuerzo
# ----------------------------
for i, (start_idx, end_idx) in enumerate(barras):
    start = nodos[start_idx]
    end = nodos[end_idx]
    
    linea = pv.Line(start, end)
    
    # Normalizar esfuerzo a 0-1 y convertir a RGB
    color_rgb = cmap(esfuerzos[i] / max(esfuerzos))[:3]
    
    plotter.add_mesh(linea, color=color_rgb, line_width=5)

# ----------------------------
# 7️⃣ Dibujar flechas de reacción
# ----------------------------
for i, has_reaction in enumerate(reacciones):
    if has_reaction:
        plotter.add_mesh(pv.Arrow(start=nodos[i], direction=[0, 0, 1], scale=0.2), color="blue")

# ----------------------------
# 8️⃣ Mostrar grid y ventana 3D
# ----------------------------
plotter.show_grid()
plotter.show()
