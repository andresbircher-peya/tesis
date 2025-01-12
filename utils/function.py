import pandas as pd
import gspread
from google.oauth2.service_account import Credentials


def load_google_sheet_to_df(spreadsheet_id, sheet_name, data_range=None):
    """
    Carga datos de una hoja de cálculo de Google Sheets en un DataFrame.
    Usa la primera fila del rango como encabezados.
    
    Args:
        service_account_file (str): Ruta al archivo JSON de la cuenta de servicio.
        spreadsheet_id (str): ID del Google Sheet.
        sheet_name (str): Nombre de la hoja (pestaña) dentro del Google Sheet.
        data_range (str): Rango de celdas a leer (opcional). Ejemplo: 'A1:D100'.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de la hoja, usando la primera fila como encabezado.
    """
    # Configurar la autenticación
    service_account_file = 'C:/Users/andres.bircher/Documents/Personal/Tesis/credencials/service_account_cred.json'
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    credentials = Credentials.from_service_account_file(service_account_file, scopes=scopes)
    client = gspread.authorize(credentials)

    # Acceder al Google Sheet y seleccionar la hoja
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)

    # Obtener los datos del rango especificado o toda la hoja
    if data_range:
        data = worksheet.get(data_range)
    else:
        data = worksheet.get_all_values()

    # Convertir la primera fila en encabezados del DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # Primera fila como encabezados
    return df