# Importamos la libreria para poder manipular imagenes
import imageio

# Importamos las imagenes de ejemplo al proyecto
archivos = ['bersek-1.png', 'bersek-2.png']

# Creamos una lista donde guardaremos las imagenes
imagenes = []

# Bucle para recorrer las imagenes agregadas
for archivo in archivos:
    imagenes.append(imageio.v2.imread(archivo))

# Guardamos el .gif con una duracion de 0.5 milisegundos
imageio.mimsave('mi_gif_generado.gif', imagenes, duration=0.5)
