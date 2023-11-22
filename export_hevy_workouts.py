import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from os import remove
from os import path

# Intentamos acceder y conectarnos a la página de hevy.com con usuario y contraseña

# Opciones de navegación
options_ =  webdriver.ChromeOptions()
options_.add_argument('--start-maximized')
options_.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\EMOCA7N\\Downloads\\chrome-win64\\chrome-win64\\chrome.exe'

driver = webdriver.Chrome(options=options_)

# Inicializamos el navegador
driver.get('https://hevy.com/login?postLoginPath=%2F')

# Introducimos usuario
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input')))\
    .send_keys('CORREO')

# Introducimos contraseña
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/form/div[2]/input')))\
    .send_keys('CONTRASEÑA')

# Clickamos en el botón de login
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div/div/form/button')))\
    .click()

# Clickamos en el botón de aceptar
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[9]/div/div/div/div[3]/button')))\
    .click()

# Clickamos en Settings
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/a[5]/div/div/p')))\
    .click()

# Clickamos en Exportar data
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div[3]/div[3]/div/div/div[1]/div[1]/div/div[6]/div[1]/div[1]/p')))\
    .click()

# Clickamos en el botón para exportar
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div[3]/div[3]/div/div/div[1]/div[2]/div/div[2]/button')))\
    .click()

time.sleep(8)

driver.quit()
#input("Esperando que no se cierre webdriver: ")

# Después de esto, el fichero se ha descargado en la carpeta DESCARGAS

# Los siguientes pasos serán 
# abrir el fichero desde la carpeta DESCARGAS
# hacer las transformaciones necesarias (por ejemplo modificar el punto de los decimales)

# Leemos el csv que se ha exportado
df = pd.read_csv('C:/Users/EMOCA7N/Downloads/workouts.csv', sep=',', index_col=False)
#print(df)

# Nos quedamos con las columnas que necesitamos, excluyendo las 3 últimas
df_v1 = df[df.columns[:-3]]

# Transformamos la columna weight_kg, reemplazando los puntos por comas
df_v1['weight_kg'] = df_v1['weight_kg'].astype(str).str.replace('.', ',')

# Transformamos la columna set_index, reemplazando los números de las series para que empiecen por 1
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('6','7')
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('5','6')
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('4','5')
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('3','4')
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('2','3')
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('1','2')
df_v1['set_index'] = df_v1['set_index'].astype(str).str.replace('0','1')

# Exportamos el fichero a csv con la fecha de hoy

# Obtener la fecha de hoy
fecha_hoy = datetime.now().strftime("%d%m%Y")

# Crear el nombre del archivo CSV con el formato deseado
nombre_archivo = f"workouts_{fecha_hoy}.csv"

df_v1.to_csv(nombre_archivo, index=False)

# Por último, se elimina el fichero de la carpeta descargas

if path.exists('C:/Users/EMOCA7N/Downloads/workouts.csv') :
    remove('C:/Users/EMOCA7N/Downloads/workouts.csv')
