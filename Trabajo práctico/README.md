# Trabajo práctico

Proyecto de diseño e implementación de un filtro pasabanda a partir de una función de transferencia dada.

Los scripts grafican y comparan diagramas de Bode y respuestas del circuito a diferentes señales de entrada en tres etapas del proyecto:
1. **Circuito teórico**: diseñado en base a la función de transferencia.
2. **Circuito normalizado**: diseñado a partir del circuito teórico, con valores de componentes comerciales.
3. **Circuito implementado**: circuito efectivamente implementado a partir del circuito normalizado, medido en laboratorio.

Dependiendo de la etapa, los datos que se muestran en los gráficos están generados a partir de:
- Cálculos analíticos
- Simulaciones numéricas hechas con SciPy
- Simulaciones circuitales hechas con LTspice
- Mediciones hechas en laboratorio
