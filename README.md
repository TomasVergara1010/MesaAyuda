🎧 MesaAyuda

### Gestión de solicitudes de soporte técnico con **pilas** y **colas** hechas desde cero

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Control%20de%20versiones-Git%20%26%20GitHub-F05032?logo=git&logoColor=white)

*Aplicación de consola · Programación orientada a objetos · Nodos enlazados*

</div>

## 📑 Contenido

- [🎯 Objetivo](#-objetivo)
- [✨ Funcionalidades](#-funcionalidades)
- [🧠 Cómo funciona](#-cómo-funciona)
- [🗂️ Estructura del proyecto](#️-estructura-del-proyecto)
- [🤝 Trabajo colaborativo](#-trabajo-colaborativo)
- [👥 Integrantes](#-integrantes)

---
## 🎯 Objetivo

Construir una aplicación de consola que registre solicitudes de soporte técnico, las atienda **en orden de llegada** y conserve un **historial** de las ya atendidas.
---

## ✨ Funcionalidades

| # | Opción del menú | Qué hace |
|:-:|---|---|
| 1 | 📝 **Registrar solicitud** | Captura los datos y la agrega al final de la cola de pendientes |
| 2 | ✅ **Atender siguiente** | Retira la solicitud más antigua y la guarda en el historial |
| 3 | 📋 **Ver pendientes** | Muestra las solicitudes que esperan, respetando su orden |
| 4 | 🕘 **Ver última atendida** | Muestra la cima de la pila sin retirarla |
| 5 | 🔢 **Cantidad de pendientes** | Informa cuántas solicitudes siguen en la cola |
| 6 | 🚪 **Salir** | Termina el programa de forma controlada |

---

## 🗂️ Estructura del proyecto

```text
MesaAyuda/
├── main.py          # 🚀 Punto de inicio de la aplicación
├── Mesa.py          # 🎛️ MesaAyuda: coordina la cola, la pila y el menú
├── Solicitud.py     # 📄 Solicitud: id, usuario y descripción
├── Node.py          # 🔗 Nodo: dato + referencia al siguiente
├── pilas.py         # 📚 Pila (historial)
├── cola.py          # 🚶 Cola (pendientes)
├── prueba_cola.py   # 🧪 Pruebas de la cola
├── Pruebas.py       # 🧪 Pruebas generales
├── .gitignore       # 🙈 Archivos que Git ignora (__pycache__, *.pyc)
└── README.md        # 📖 Este archivo
```
---

## 🤝 Trabajo colaborativo

El desarrollo se organizó con **Git y GitHub**:

- 🌿 Ramas de trabajo para desarrollar partes del sistema por separado
- 💬 Commits pequeños y con mensajes descriptivos
- 🔀 Integración de los cambios en la rama principal

## 👥 Integrantes

| Integrante | GitHub | 
|---|---|
| **Tomás Vergara** | [@TomasVergara1010](https://github.com/TomasVergara1010) | 
| **Jhonatan Oquendo** | [@Tatan072](https://github.com/Tatan072) | 

---

<div align="center">

📚 Proyecto académico · Asignatura **Estructuras de Datos**
