# Predicción en el Precio de Coches con Flask y Azure ML

Este proyecto es una aplicación web desarrollada con **Flask** que se conecta a un **endpoint de Azure Machine Learning** para predecir el precio de un coche en función de sus características.

## 🚀 ¿Cómo funciona?

1. Al abrir la aplicación en [http://127.0.0.1:5000](http://127.0.0.1:5000), se mostrará un formulario para rellenar.
2. El formulario se rellena por defecto con los datos de un coche de ejemplo.
3. Puedes editar los valores para introducir tus propios datos.
4. Al enviar el formulario, se realiza una petición al endpoint de Azure ML que devuelve el precio estimado del coche.

## 🛠️ Requisitos

- Python 3.8+
- Flask
- Requests
- python-dotenv

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

## ⚙️ Variables de entorno

Deebes de crear un archivo `.env` con tus credenciales de Azure:

```env
API_KEY=tu_api_key_aqui
ENDPOINT=https://tu-endpoint.azurewebsites.net/score
```

## ▶️ Pruebalo

En terminal:

```bash
flask run
```

La aplicación estará disponible en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

![image](https://github.com/user-attachments/assets/cc139280-8b32-4c5d-b3d4-d112ed937d56)



---
