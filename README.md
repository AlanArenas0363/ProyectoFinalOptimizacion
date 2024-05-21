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

#### ¿Que es el Dijkstra?
Es un método utilizado para encontrar el camino más corto desde un nodo de inicio a todos los demás nodos en un grafo con pesos no negativos. Funciona manteniendo una
lista de los nodos cuyas distancias más cortas desde el nodo de inicio ya se han determinado y actualizando estas distancias a medida que explora los nodos adyacentes. 

Para esto podríamos utilizar dos librerías principales:
  - tkinter / customtkinter (Usaremos la segunda).
  - numpy
  - heapq
  - tkinterDnD (Librería de apoyo)

#### Instalación de las librerías:
Para poder instalar correctamente las librerías, debe de ingresar estos comandos al CMD o Terminal de su sistema operativo:
```
    pip install numpy
    pip install customtkinter
    pip install tkinterDnD
```
Una vez instalada, reinicie el IDE que está usando y vuelvalo a ejecutar.

## ¿Como podríamos mejorar este proyecto?
Ya que hemos terminado el proyecto, aún nos podríamos hacer la pregunta de como se podría mejorar aún más este pequelo programa. Esto con el fin de no perder práctica
en el ámbito de la programación, así que se hizo esta pequeña lista de lo que podríamos hacer y una breve explicación del por qué podríamos hacer este cambio.
  - Datos personalizados en velocidad:
      Esto sería importante poderlo arreglar, ya que el programa en sí te propone la velocidad constante de 60km/hr. Entonces, sería mejor poderle dar la posibilidad de que el
      usuario cambie ese valor, sin tener que modificar el valor desde el archivo fuente.
    
  - Capacidad de leer archivos ajenos (.cvs):
      Esta parte sería interesante, tener un pequeño menú en la cual pueda cargar cualquier archivo con esta extensión y así acomodar los datos de manera automática sin tener que
      escribirlos cada vez que se necesite.
    
  - Archivo ejecutable:
      Esto sería interesante también, ya que puede ser algo tedioso tener que instalar una librería solamente para utilizar el programa pocas veces, así que para ahorrarnos tiempo, sería
      mejor que sería un ejecutable, para así nada más correr el archivo y poderlo utilizar sin problemas. 

## Cronograma:

![l0fL2uP](https://github.com/AlanArenas0363/ProyectoFinalOptimizacion/assets/159272184/10d601ad-1e0a-4170-b8cb-7d3806874389)

Link: https://imgur.com/a/nLNSz80

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

### Actualización 20/Mayo/2024 (COMMIT 1)
  - Se completó la parte del Backend. (Ver 'backend.py')

### Actualización 20/Mayo/2024 (COMMIT 2)
  - Se subió el codigo principal en la cual es la fusión del Frontend y Backend (v0.5). Se puede modificar luego, para agregar otro metodo de resolver el problema
    final (Ver 'main.py') (Capturas: https://imgur.com/a/6s5TinG)
      * Se modificó el ingreso de texto en el apartado de 'Metodo optimo' a números (Esto es una version de prueba, puede cambiar a futuras actualizaciones)
  - Se agregó como se puede instalar las librerías necesarias en el README.md (Este documento)
  - Se agregó la definición del método Dijkstra en el README.md (Este documento)

### Actualización 21/Mayo/2024
  - Bugfixes menores al código principal (v0.6):
      * Se arregló el bug que se amontonaba el resultado si cambiabas las coordenadas y/o cambiabas el metodo optimo a resolver sin tener que reiniciar el
        código (Capturas: https://imgur.com/a/HJxRnuL)
      * Se eliminó el feedback cuando apretabas el botón de Calcular (Este botón funciona correctamente)
      * Se ocultó los resultados del problema ubicados en la terminal (Si desea reactivarlos, quite el '#' antes de su print correspondiente)
  - Implementado un nuevo botón:
      * Se agregó un nuevo botón, en la cual borra todos los valores/texto que se encuentran en los recuadros de:
          - X Inicial, Y Inicial, X Final, Y Final, Método Optimo y Resultado
  - Se agregó el apartado de '¿Como podríamos mejorar este proyecto?' en el README.md (Este documento)
  - Se agregó una librería que se utilizó en el programa final en el README.md (Este documento)
