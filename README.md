# Estrategias para reducir las pérdidas por fraude en las reclamaciones de siniestro en una empresa de seguros vehiculares

## Introducción
Este documento presenta una serie de recomendaciones basadas en un análisis de datos sobre reclamaciones de siniestros y fraudes en una empresa de seguros vehiculares. El objetivo es proporcionar estrategias efectivas para reducir las pérdidas por fraude y proteger los activos de la empresa. Estas recomendaciones se basan en los insights obtenidos del análisis de datos y se centran en áreas clave identificadas durante el proceso.

## Insights del análisis de datos
Durante el análisis de los registros de denuncia de siniestros, se obtuvieron los siguientes insights:

`Insight 1`: La mayoría de los fraudes registrados se producen en zonas urbanas y son realizados por personas independientes. Además, se observó que los fraudes están asociados principalmente al tipo de seguro "All Perils".

`Insight 2`: Se identificó un patrón en los registros de no_fraudes con edades de 0, donde los seguros tenían un costo de 300 y 400. Por otro lado, todos los registros de fraudes con edades de 0 mostraban costos de seguro de 400.

`Insight 3`: Se descubrió que la marca de vehículo más frecuentemente asociada a fraudes y registros de edades de 0 es Honda. Además, se observó que los fraudes siempre eran cometidos por una persona masculina y externa a la compañía.

`Insight 4`: La distribución de las edades de los denunciantes mostró variabilidad en general, pero se destacó una particularidad en las edades de 0, que anteriormente se pensaban como posibles outliers. Se recomienda examinar minuciosamente los registros que reporten estas edades, ya que podrían estar relacionados con fraudes según los insights anteriores.

`Insight 5`: La mayoría de los seguros con fraudes tienen un costo de 400 en la variable "Deductible". Cerca del 90% de los fraudes se asociaron a seguros con ese costo. Esto indica que los seguros con este valor de deducible son más fáciles o más atractivos para cometer fraudes.

`Insight 6`: Se observó una disminución en la cantidad de fraudes a lo largo de los años. Esto puede ser resultado de la implementación exitosa de nuevos mecanismos o tecnologías para reducir la ocurrencia de fraudes. Se recomienda seguir invirtiendo en tecnología y personal calificado para mantener esta tendencia positiva.

`Insight 7`: El tipo de seguro "All Perils" fue el menos denunciado en la categoría de no fraudes, mientras que fue el más denunciado en los registros con fraudes. Esto respalda la idea de que este tipo de seguro es más apetecible para cometer fraudes debido a su cobertura integral y mayor beneficio económico para los defraudadores.

## Recomendaciones para reducir las pérdidas por fraude
`Mejorar la detección de fraudes en zonas urbanas:` Implementar sistemas y tecnologías de detección de fraudes más sofisticados en áreas urbanas para identificar comportamientos fraudulentos y prevenir pérdidas.

`Reforzar la revisión de reclamaciones con edades de 0:` Realizar una revisión minuciosa de todas las reclamaciones con edades de 0 para identificar posibles casos de fraude. Aplicar verificaciones adicionales y utilizar técnicas de detección de fraude específicas para estos casos.

`Implementar controles y validaciones más estrictos en seguros "All Perils":` Establecer controles rigurosos al procesar y aprobar reclamaciones bajo este tipo de póliza. Realizar una revisión detallada de la documentación, validar múltiples fuentes y utilizar análisis de comportamiento para detectar posibles fraudes.

`Fortalecer los mecanismos de seguridad y prevención de fraudes:` Invertir en tecnología y recursos humanos especializados para mejorar continuamente los mecanismos de seguridad y prevención de fraudes. Implementar sistemas de monitoreo en tiempo real, colaborar con agencias especializadas en detección de fraudes y proporcionar capacitación constante al personal para identificar señales de posibles fraudes.

`Fomentar la concientización y denuncia interna:` Promover una cultura de ética y honestidad en la empresa, donde los empleados se sientan seguros al denunciar posibles casos de fraude. Establecer canales de comunicación confidenciales y programas de concientización sobre la importancia de prevenir y combatir el fraude.

`Mantenerse actualizado sobre nuevas técnicas de fraude:` Estar al tanto de las nuevas técnicas y tendencias de fraude en la industria de seguros. Participar en conferencias, seminarios y capacitaciones relacionadas con la detección de fraude para obtener información actualizada y adaptar las estrategias de prevención y detección.

Estas recomendaciones se basan en los insights obtenidos del análisis de datos y tienen como objetivo ayudar a la empresa de seguros vehiculares a reducir las pérdidas por fraude en las reclamaciones de siniestro. Al implementar estas estrategias, la empresa puede fortalecer sus mecanismos de detección, prevenir casos de fraude y proteger sus activos.

## Conclusiones
La detección y prevención del fraude en reclamaciones de siniestro es crucial para garantizar la sostenibilidad y el éxito de una empresa de seguros vehiculares. Mediante el análisis de datos, se pueden obtener insights valiosos que orienten la toma de decisiones y la implementación de estrategias efectivas. Al aplicar las recomendaciones presentadas en este informe, la empresa estará mejor preparada para enfrentar el desafío del fraude, proteger sus recursos y brindar un servicio confiable a sus clientes.

## Nota
En la carpeta notebooks se encuentra un cuaderno de jupyter en el cual está el análisis y un modelo de `Machine Learning` que ayudara a la detección de fraudes.
