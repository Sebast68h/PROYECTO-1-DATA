# Revisión de calidad de los datos

Por una nueva indicacion que se nos dio, el analisis filtra unicamente personas de 18 años o mas. De 235350 registros iniciales quedan 172025. Estos registros corresponden a todo el pais, por lo que los resultados no describen exclusivamente a Bogota.

No encontramos personas duplicadas usando DIRECTORIO, SECUENCIA_P y ORDEN. Las siete variables de bienestar revisadas no tienen valores nulos.

En P1896 encontramos 21681 respuestas con código 99 (12,6 % de los adultos). Este codigo significa que no recibe ingresos y no es una puntuacion de satisfaccion. Lo conservamos como informacion de la persona, pero lo excluimos al calcular promedios y correlaciones de satisfaccion con los ingresos.