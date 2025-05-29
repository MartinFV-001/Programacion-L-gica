import cv2
import mediapipe as mp
import numpy as np
import requests
import mysql.connector
import time
from mysql.connector import Error
import socket
import pandas as pd

# Función para obtener IP privada
def obtener_ip_privada():
    try:
        ip_privada = socket.gethostbyname(socket.gethostname())
        return ip_privada
    except socket.error as e:
        return f"Error al obtener la IP privada: {e}"

# Función para obtener IP pública
def obtener_ip_publica():
    try:
        respuesta = requests.get('https://api.ipify.org?format=json')
        respuesta.raise_for_status()
        ip_publica = respuesta.json()['ip']
        return ip_publica
    except requests.RequestException as e:
        return f"Error al obtener la IP pública: {e}"

# Función para insertar datos en MySQL y exportar a Excel
def insertar_datos(ip_privada, ip_publica, nombre_usuario):
    conexion = mysql.connector.connect(
        host='serverdb.cthplnkf3hqq.us-east-1.rds.amazonaws.com',
        database='prolog',
        user='admin',
        password='Admin12345#!'
    )

    cursor = conexion.cursor()
    query = "INSERT INTO datos_usuario (ip_privada, ip_publica, nombre_usuario) VALUES (%s, %s, %s)"
    valores = (ip_privada, ip_publica, nombre_usuario)
    cursor.execute(query, valores)
    conexion.commit()
    cursor.close()

    # Exportar a Excel
    consulta = "SELECT * FROM datos_usuario"
    datos = pd.read_sql(consulta, conexion)
    datos.to_excel('datos_usuario.xlsx', index=False)
    conexion.close()
    print("Datos exportados exitosamente a datos_usuario.xlsx")

# Inicializar FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Dibujado
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Captura de video
cap = cv2.VideoCapture(0)

# Función para calcular distancia entre dos puntos
def calcular_distancia(punto1, punto2):
    return np.linalg.norm(np.array(punto1) - np.array(punto2))

# Obtener IPs
ip_publica = obtener_ip_publica()
ip_privada = obtener_ip_privada()
nombre_usuario = "Gamero"

# Variables de control de detección
boca_abierta = False
inicio_boca_abierta = 0
umbral_duracion = 2  # segundos

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("No se puede acceder a la cámara")
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = face_mesh.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec
            )

            # Coordenadas de los labios
            labio_superior = face_landmarks.landmark[13]
            labio_inferior = face_landmarks.landmark[14]
            altura, ancho, _ = image.shape
            labio_superior = (int(labio_superior.x * ancho), int(labio_superior.y * altura))
            labio_inferior = (int(labio_inferior.x * ancho), int(labio_inferior.y * altura))

            # Distancia entre labios
            distancia_boca = calcular_distancia(labio_superior, labio_inferior)
            umbral_boca_abierta = 10

            if distancia_boca > umbral_boca_abierta:
                if not boca_abierta:
                    boca_abierta = True
                    inicio_boca_abierta = time.time()
                elif time.time() - inicio_boca_abierta > umbral_duracion:
                    cv2.putText(image, '¡Boca Abierta!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    insertar_datos(ip_privada, ip_publica, nombre_usuario)
                    print("Se guardó el registro en la base de datos...")
                    inicio_boca_abierta = time.time()
            else:
                boca_abierta = False

    cv2.imshow('Reconocimiento de Gestos Faciales con FaceMesh', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
