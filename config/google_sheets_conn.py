"""
ANTES DE EJECUTAR:
---------------
1. Habilitar Google Sheets API, crear las credenciales y autorizar los Scopes
   https://console.developers.google.com/apis/api/sheets
2. Instalar la librería correspondiente
   pip install --upgrade google-api-python-client`
3. Definir las variables necesarias
    Renombrar el .json descargado a "credentials.json"
    Tener ubicado el archivo token.pickle en la misma carpeta (ruta local)


TODO: Habilitar los Scopes correspondientes (ver que nivel queremos dar)
https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
     'https://www.googleapis.com/auth/drive'
     'https://www.googleapis.com/auth/drive.file'
     'https://www.googleapis.com/auth/spreadsheets'
"""

# Importo las librerías
import pickle
import os.path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import discovery

# Ruta local de ubicación de archivos
sheet_id = '1Ai209GagEF30giH0xbSQhaXHFSqpJvcvliv-MCKA6kI'
sheet_range = "crypto_list!B2:Z"


def checkSheet(sheet_id, sheet_range):
    """
    Connection to GoogleSheets

    :param sheetRange: Sheet and Range
    :return: sabe Dios
    """

    # Defino el scope a autorizar, variable para las credenciales e ID de la hoja
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    spreadsheet_id = sheet_id

    # Defino rango de muestreo y de insert (los valores se insertarán al final del rango)
    sample_range = sheet_range
    creds = None

    # Solicito credenciales
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Defino service a utilizar (ver Scopes)
    service = discovery.build('sheets', 'v4', credentials=creds, cache_discovery=False)

    # Ejecuto Request de  lectura de tickers
    # print("Leyendo datos...")
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                 range=sample_range).execute()

    result = result['values']

    return result


data = checkSheet(sheet_id, sheet_range)

print(data)


