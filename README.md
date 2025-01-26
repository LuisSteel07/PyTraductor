# PyTraductor
El proyecto PyTraductor ofrece la funcionalidad de poder traducir archivos de subtítulos .srt a otros idiomas sin 
complicaciones y de manera rápida.

# Características y Funciones
En la funcionalidad del código, creamos la clase **TranslateActivity**, que solamente abarca un subtítulo del archivo 
.srt, en donde en el mismo guardaremos el **número de secuencia**, **el tempo**, **el texto** que se mostrará y 
**una instancia de Thread** para realizar la acción de traducción en segundo plano, donde el resultado de la misma lo 
guardará en otra propiedad llamada **translate_text**.

En la clase podemos encontrar el único método llamado **translate(dest: str)** el cual recive únicamente el idioma 
destino a que se va a traducir el archivo.

## Funciones elementales para el funcionamiento del programa

- **create_activities(path: str, dest: str)**: Nos permitirá crear una lista de instancias de la clase 
**TranslateActivity**, a partir de una lectura que se da en el archivo .srt objetivo. Para eso precisamos de utilizar 
el path para ubicar el archivo y el destino de idioma.

- **save_translate(path: str, dest: str, list_activities: list[TranslateActivity])**: Nos permitirá guardar los 
resultados de la traducción realizada en la actividad en segundo plano. En donde este escribirá un nuevo archivo
con determinada ubicación y recorrerá la lista de actividades creada por **create?activities()** extrayendo de ella:
el numero de secuencia, el tempo y principalmente el texto ya traducido.

En la misma función main() creada para la inicialización del programa se agrega la función **translate_file()** la cual
nos permite directamente crear la lista de actividades a partir del archivo .srt e ir empezando las actividades en 
segundo plano, lo que claro, son muchísimas, por lo cual cada 20 inicializaciones se tendrá un tiempo de espera de 10s.
Mientras de vaya terminando cada actividad se calculá el porciento de traducción y al final se mostrará el tiempo
transcurrido para realizar la traducción completamente en segundos.
 
# Enlace de descarga del programa


# Licencia
MIT