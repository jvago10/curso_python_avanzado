# Trabajo con archivos csv.
import csv
from pathlib import Path

FILE_PATH = Path('users.csv')


def read_csv():
    try:
        with open(FILE_PATH, 'r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row.get('first_name'), ':', row.get('email'))
    except FileNotFoundError:
        print("No se encontró el archivo")


def write_csv():
    try:
        with open(FILE_PATH, 'a', newline="") as file:
            write = csv.DictWriter(
                file, fieldnames=['first_name', 'last_name', 'email']
            )

            write.writerows([
                {
                    'first_name': 'José',
                    'last_name': 'Vargas',
                    'email': 'jose.vargas@intertech.network'
                },
                {
                    'first_name': 'Elvis',
                    'last_name': 'Rivera',
                    'email': 'elvis.rivera@intertech.network'
                }
            ])
            print('Datos agregados')
    except FileNotFoundError:
        print("Error en la lectura y escritura del archivo")


if __name__ == '__main__':
    write_csv()
    read_csv()
