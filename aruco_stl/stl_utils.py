# aruco_stl/stl_utils.py

import numpy as np
from stl import mesh

def marker_to_stl(marker_image, output_file, thickness=1.0):
    """
    Convert a 2D marker image (with black parts extruded) to a 3D STL file.
    :param marker_image: Binary marker image.
    :param output_file: Path to save the STL file.
    :param thickness: Thickness of the marker in 3D.
    """
    rows, cols = marker_image.shape
    vertices = []
    faces = []

    # Create vertices for the black regions (0) of the marker
    for y in range(rows):
        for x in range(cols):
            if marker_image[y, x] == 0:  # Only consider black regions (0)
                z0 = 0
                z1 = thickness
                vertices.extend([
                    [x, y, z0],
                    [x + 1, y, z0],
                    [x, y + 1, z0],
                    [x + 1, y + 1, z0],
                    [x, y, z1],
                    [x + 1, y, z1],
                    [x, y + 1, z1],
                    [x + 1, y + 1, z1],
                ])

                base_index = len(vertices) - 8

                # Faces of the cube (12 triangles per block)
                faces.extend([
                    [base_index, base_index + 1, base_index + 2],
                    [base_index + 1, base_index + 3, base_index + 2],
                    [base_index + 4, base_index + 5, base_index + 6],
                    [base_index + 5, base_index + 7, base_index + 6],
                    [base_index, base_index + 1, base_index + 4],
                    [base_index + 1, base_index + 5, base_index + 4],
                    [base_index + 2, base_index + 3, base_index + 6],
                    [base_index + 3, base_index + 7, base_index + 6],
                    [base_index, base_index + 2, base_index + 4],
                    [base_index + 2, base_index + 6, base_index + 4],
                    [base_index + 1, base_index + 3, base_index + 5],
                    [base_index + 3, base_index + 7, base_index + 5],
                ])

    # Convert vertices and faces to numpy arrays
    vertices = np.array(vertices)
    faces = np.array(faces)

    # Create the mesh
    marker_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, face in enumerate(faces):
        for j in range(3):
            marker_mesh.vectors[i][j] = vertices[face[j], :]

    # Write to STL file
    marker_mesh.save(output_file)
    print(f"STL file saved as: {output_file}")
