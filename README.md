# Simulación de Frenado

![Simulación de Frenado](https://example.com/simulation_image.png)

## Descripción

Este proyecto simula el frenado de un automóvil utilizando Pygame y Tkinter. La simulación gráfica muestra cómo un automóvil desacelera hasta detenerse, y los resultados se almacenan en una base de datos SQLite.

## Estructura del Proyecto

## Flujo de Datos de la Simulación

1. **Inicialización**: Se inicializa la clase [`Automovil`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fautomovil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A6%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A22%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fsimulador_frenado.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A6%7D%7D%5D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "Go to definition") con los parámetros de velocidad inicial y desaceleración.
2. **Simulación**: La clase [`Simulador`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A22%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fsimulador.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A6%7D%7D%5D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "Go to definition") ejecuta la simulación y calcula la distancia de frenado.
3. **Almacenamiento**: Los resultados de la simulación se almacenan en una base de datos SQLite.
4. **Visualización**: La simulación gráfica se muestra utilizando Pygame y Tkinter.

![Flujo de Datos](https://example.com/data_flow_diagram.png)

## Explicación de Archivos

- **[`src/automovil.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fautomovil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "/home/boolean/Fisica I/src/automovil.py")**: Define la clase [`Automovil`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fautomovil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A6%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A22%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fsimulador_frenado.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A7%2C%22character%22%3A6%7D%7D%5D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "Go to definition") que maneja las propiedades y el movimiento del automóvil.
- **[`src/main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "/home/boolean/Fisica I/src/main.py")**: Archivo principal que inicia la aplicación Tkinter y maneja la interfaz gráfica.
- **[`src/simulador_frenado.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fsimulador_frenado.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "/home/boolean/Fisica I/src/simulador_frenado.py")**: Contiene la lógica para la simulación gráfica del frenado utilizando Pygame.
- **[`src/simulador.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fsimulador.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "/home/boolean/Fisica I/src/simulador.py")**: Define la clase [`Simulador`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A22%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fboolean%2FFisica%20I%2Fsrc%2Fsimulador.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A6%7D%7D%5D%2C%22dcb69d5f-2dfe-4c99-aee2-be9726ec24df%22%5D "Go to definition") que ejecuta la simulación y guarda los resultados en la base de datos.

## Instalación

Para instalar las dependencias del proyecto, ejecuta:

```sh
pip install -r requirements.txt

## Hecho por

Boolean/Bit