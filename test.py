import os

filename = "ruta/al/archivo.txt"
root, extension = os.path.splitext(filename)
print(root)  # Output: ruta/al/archivo
print(extension)  # Output: .txt