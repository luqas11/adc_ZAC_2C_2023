import csv
import numpy as np

def read_csv(columns_names, filename):
    """
    Lee datos de un archivo en formato CSV, dado un nombre de archivo y un array de nombres de columnas.

    Parameters
    ----------
    columns_names : list[str]
        Nombres de las columnas del archivo
    filename : str
        Nombre del archivo, sin la extensión

    Returns
    ----------
    out : dict_values[NDArray[float64]]
        Lista de listas con los valores de cada columna del archivo
    """
    columns = {key: np.empty(0) for key in columns_names}
    with open(f'Trabajo práctico/csv/{filename}.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for name in columns_names:
                columns[name] = np.append(columns[name], float(row[name]))
    return columns.values()
