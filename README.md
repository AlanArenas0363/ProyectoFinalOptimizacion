# Proyecto Final de Análisis de Algoritmos
## Proyecto hecho por: Alan Arenas y Jose Equihua (Programación Loka)
### Tema: Optimización

## ¿De que trata el proyecto?
Este proyecto trata de resolver el problema de enrutamiento de vehículo (VRP), esto utilizando la programación optimizada en el lenguaje Python.

#### ¿Que es el VRP?
El enrutamiento de vehículos o VRP (Vehicle Routing Problem) es un problema típicamente planteado para la optimización de las rutas de transporte y vehículos
asociados a ellas. Para su planteamiento y búsqueda de soluciones óptimas se recurre en investigación operativa a modelos matemáticos como Branch and
Bound o programación dinámica entre otros más.

#### ¿Como lo haremos?
En el lenguaje Python, haremos un programa con interfaz, en la parte de la interfaz podría empezar el enrutamiento utilizando coordenadas iniciales y de destino,
(Se pueden utilizar otras más maneras). Despues preguntaría que sería más eficiente para el usuario (Tiempo, distancia, costo) entre otras cosas más que posiblemente
agregaríamos.

Para esto podríamos utilizar dos librerías principales:
  - tkinter / customtkinter (Usaremos la segunda).
  - numpy
  - heapq
  - y otras librerías que podríamos agregar más adelante

## Changelog:
### Actualización 13/Mayo/2024
  - Se agregó la base del Frontend (Capturas: https://imgur.com/a/wVB8Qot ).
  - Se agregó las posibles librerías que se usarán en Backend.

### Actualización 14/Mayo/2024
  - Se agregó este README.md para lectura/contexto/changelog del proyecto.
  - Se agregó imagenes ilustrativa del Frontend (v0.0.1).

### Actualización 15/Mayo/2024
  - Se actualizó el Frontend y que llevaría posiblemente (Captura: https://imgur.com/a/4IpaDNQ):
      * Se eliminó el botón de créditos
      * Se agregó nuevas entradas de texto
      * Se agregó 2 textboxes (1 de resultados y 1 de ayuda al usuario)
  - Se actualizó el Backend, que cosas preguntaría y comentarios de lo que llevaría.
      * Se agregó una nueva librería en el Backend y se especifica cual es en el README.md
  - Se cambió el número de versión del programa Frontend (De v0.0.1 pasa a v0.2, esto por el corto tiempo que recibirá actualizaciones el programa)
  - Se agregó imagenes ilustrativa del Frontend (v0.2).

### Actualización 18/Mayo/2024
  - Se introduce una clase (versión de prueba) para los grafos en el Backend
  - Se agregaron los significados que tendrán los comentarios dinámicos en el código (Instalar BetterComments en VisualStudioCode para ver los cambios)
  - Se renombró la librería heapd para completar el código más rápido (Para desarrolladores)
