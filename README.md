# VERIFICADOR DE CLAVES AUTOMÁTICO
El Script de manera automática incluye la detección de:
863 palabras de uso común (en español e ingles)
383 patrones de escritura débiles (en español e ingles)
245 palabras de contraseñas de diccionario (en español e ingles, las más usadas hasta el año 2023)
232 palabras con complejidad semantica débiles (en español e ingles)


![02](https://github.com/marcoscunioli/verificador_de_claves/assets/158846893/cf7bb235-1e1b-4585-b64d-a6ea43df272e)


Este script en Python tiene como objetivo verificar la fortaleza de una contraseña proporcionada por el usuario.
El proceso de verificación se realiza mediante varias funciones que evalúan diferentes aspectos de la contraseña. Vamos a analizar detalladamente cada función:

1. Función evitar_palabras_comunes(contraseña):
   - Objetivo: Evitar el uso de palabras comunes en la contraseña.
   - Método: Compara la contraseña con una lista de palabras comunes en varios idiomas.
   - Devolución: Retorna `True` si la contraseña no contiene palabras comunes, y `False` en caso contrario.

2. Función detectar_patrones(contraseña):
   - Objetivo: Detectar patrones débiles en la contraseña.
   - Método: Compara la contraseña con una lista de patrones de contraseñas débiles.
   - Devolución: Retorna `True` si la contraseña no contiene patrones débiles, y `False` en caso contrario.

3. Función comprobar_contra_diccionario(contraseña):
   - Objetivo: Verificar si la contraseña está en una lista de contraseñas comúnmente utilizadas.
   - Método: Compara la contraseña con una lista de contraseñas comunes.
   - Devolución: Retorna `True` si la contraseña no está en la lista, y `False` en caso contrario.

4. Función calcular_entropia(contraseña):
   - Objetivo: Calcular la entropía de la contraseña.
   - Método: Utiliza la fórmula de entropía para medir la complejidad de la contraseña.
   - Devolución: Retorna el valor de entropía.

5. Función calificar_entropia(entropia):
   - Objetivo: Clasificar la entropía en términos de fortaleza de la contraseña.
   - Método: Compara la entropía con umbrales predefinidos.
   - Devolución: Retorna una categoría de fortaleza ("Débil", "Moderada" o "Fuerte").

6. Función analizar_complejidad_gramatical(contraseña):
   - Objetivo: Verificar la complejidad gramatical de la contraseña.
   - Método: Comprueba si la contraseña incluye al menos una letra minúscula, una letra mayúscula y un número.
   - Devolución: Retorna un mensaje de sugerencia y la categoría de fortaleza ("Baja" si no cumple con los requisitos).

7. Función analizar_complejidad_semantica(contraseña):
   - Objetivo: Analizar la complejidad semántica de la contraseña.
   - Método: Busca palabras débiles en la contraseña.
   - Devolución: Retorna un mensaje de sugerencia y la categoría de fortaleza ("Baja" si se encuentran palabras débiles).

8. Función verificar_contraseña(contraseña):
   - Objetivo: Realizar la verificación completa de la contraseña combinando las funciones anteriores.
   - Devolución: Retorna un mensaje indicando si la contraseña es segura y las sugerencias para mejorarla si es necesario.
     
El script proporciona una herramienta completa para evaluar la fortaleza de una contraseña, teniendo en cuenta la longitud,
la entropía, la presencia de palabras comunes, patrones débiles y contraseñas conocidas.
