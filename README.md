# Proyecto Urban Grocers 

# API Testing - Creación de Kits

## Descripción

Este proyecto contiene pruebas automatizadas para verificar la funcionalidad de creación de kits mediante una API REST. Las pruebas validan tanto escenarios positivos como negativos relacionados con el campo name del kit.

El objetivo es garantizar que la API acepte nombres válidos y rechace aquellos que incumplen las reglas de validación establecidas.

## Estructura del Proyecto

├── configuration.py<br>
├── data.py <br>
├── sender_stand_request.py <br>
├── create_kit_name_kit_test.py <br>
└── README.md

### Archivos principales

- data.py: contiene los datos de prueba utilizados en las solicitudes.
- sender_stand_request.py: contiene los métodos para enviar solicitudes a la API.
- create_kit_name_kit_test.py: contiene los casos de prueba para la creación de kits.

## Casos de Prueba Implementados

### Escenarios positivos

- Creación de un kit con nombre de 1 carácter.
- Creación de un kit con nombre de 511 caracteres.
- Creación de un kit con caracteres especiales.
- Creación de un kit con espacios.
- Creación de un kit con valores numéricos representados como texto.

### Escenarios negativos

- Creación de un kit con nombre vacío.
- Creación de un kit con 512 caracteres.
- Creación de un kit sin el campo name.
- Creación de un kit con tipo de dato numérico en lugar de texto.

## Ejecución de las pruebas

Instalar dependencias:

bash pip install -r requirements.txt 

Ejecutar todas las pruebas:

bash pytest 

Ejecutar una prueba específica:

bash pytest create_kit_name_kit_test.py 

## Resultado Esperado

Las pruebas positivas deben devolver:

text Status Code: 201 

Las pruebas negativas deben devolver:

text Status Code: 400 

## Objetivo

Verificar que la API implemente correctamente las reglas de validación para la creación de kits y garantice la integridad de los datos recibidos.