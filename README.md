## MAYRA MICHELLE MORAN MEDINA
## TECNOLOGIAS DE LA INFORMACION
## SEGUNDO SEMESTRE
## mm.moranm@uea.edu.ec

# Sistema Avanzado de Gestión de Inventario

Este proyecto corresponde al desarrollo de un Sistema Avanzado de Gestión de Inventario
implementado en Python, aplicando los principios de la Programación Orientada a Objetos (POO)
y el uso eficiente de colecciones para la administración de datos.

El sistema permite gestionar productos de una tienda mediante una interfaz interactiva
en consola, incluyendo almacenamiento persistente en archivos.

El sistema utiliza distintas colecciones para optimizar la gestión del inventario:

- **Diccionario:**  
  Se utiliza como estructura principal para almacenar los productos,
  donde la clave es el ID del producto y el valor es el objeto Producto.
  Esto permite búsquedas rápidas y eficientes.

- **Lista:**  
  Se emplea en la búsqueda de productos por nombre.

- **Tuplas:**  
  Se utilizan internamente para el manejo estructurado de datos.

El inventario se guarda en un archivo llamado: inventario.json

## Dato Importante
Aunque GitHub organiza los archivos en orden alfabético,
el archivo que debe ejecutarse es:
**main.py**
Los archivos `producto.py` e `inventario.py` contienen las clases utilizadas por el sistema.
