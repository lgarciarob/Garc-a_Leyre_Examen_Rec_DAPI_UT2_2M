# Ejercicio1

import csv

with open("D:\\2M\\DAPI\\Leyre García Robledo - DGT.csv", "r", encoding="utf-8") as csv_fichero:
    reader = csv.reader(csv_fichero)
    for user in reader:
        print(user)

def check_DGT(file):
    """
    Esta funcion sirve para abrir un fichero de texto, comprobar los datos de los usuarios y sobrescribir los datos
    corregidos en el mismo fichero.
    Parametros:
        - csv_fichero: ruta del fichero (.csv) a abrir.
    Salidas:
        - No devuelve nada
    """

    with open(file, "r") as csv_fichero:
        lineas = csv_fichero.readlines()
        correccion = []
        lista_datos = []
    with open("D:\\2M\\DAPI\\Leyre García Robledo - DGT.csv","w", encoding="utf-8", newline="") as fichero:
        claves = ["Nombre", "Apellidos", "DNI", "Teléfono", "País", "Vehículo", "Multas Radar",
                  "Multas ITV", "Multas Estupefacientes", "Total Multas"]
        escrito = csv.DictWriter(fichero, fieldnames= claves)
        escrito.writeheader()

        for row in correccion:
            escrito.writerow(row)
            lista = []

            for user in lista_datos:
                dict_dgt = {}
                datos_corregidos = [user_name, user_apellido, user_nif, telefono, pais, vehiculo, multas_totales]
                user_name = check_username(user[0])
                user_apellido = check_username(user[1])
                user_nif = check_nif(user[2])
                telefono = check_phone(user[3])
                pais = check_phone(user[4])
                vehiculo = user[5]
                multas_totales = calculate_bill(user[6], user[7], user[8])
                datos_corregidos.append(dict_dgt)

            for datos in lista:
                caracteres_especiales = csv.writer(csv_fichero, quotechar="", quoting=csv.QUOTE_ALL)
                caracteres_especiales.writerow(datos)

        print(check_DGT(file))
    return


    # Ejercicio2

countries_dict = {"30": "Grecia", "33": "Francia", "34": "España", "351": "Portugal",
                  "380": "Ucrania", "39": "Italia", "41": "Suiza",
                  "44": "Reino Unido", "49": "Alemania", "7": "Rusia"}

# Ejercicio3

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
            "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
            "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
            "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}


# Ejercicio4

def check_username(datos_user):
    """
    Esta funcion sirve para comprobar si el nombre del usuario está en formato capitalizado o Camelcase.
    Parametros:
        - user_name: es el nombre del usuario (que puede estar bien escrito o no)
    Salidas:
        - user_data: es el nombre comprobado (en formato capitalizado o Camelcase)
    """
    user_data = datos_user.title()

    return user_data


    # Ejercicio5

def check_nif(user_nif):
    """
    Esta función sirve para comprobar si número del nif se corresponde con la letra asociada
    Parametros:
        - user_nif: es el numero nif del usuario (8 numeros y una letra)
    Salidas:
        - nif_corregido: numero nif corregido con su letra asociada correspondiente
    """
    nif_number = int(user_nif[0:8])
    letra_correcta = str(nif_number % 23)
    nif_corregido = user_nif[0:8] + nif_dict[letra_correcta]
    return nif_corregido

    # Ejercicio6

def check_phone(telefono):
    """
    Esta funcion sirve para chequear e identificar si un número de teléfono está bien escrito
    y a qué país corresponde su prefijo.
    Parametros:
        - telefono: numero de telefono en formato ((XYZ)ABC-DEFGHI)
    Salidas:
        - numero_corregido: es el numero en formato ((XYZ)-ABCDEFGHI)
    """
    numero_separado = telefono.split(")")
    prefijo = numero_separado[0].replace("(", "")
    numero = numero_separado[1].replace("-", "")
    numero_corregido = "+" + prefijo + "-" + numero
    prefijo_corregido = countries_dict[prefijo]

    return numero_corregido, prefijo_corregido

    # Ejercicio7

def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """
    Esta funcion sirve para realizar la suma de la cantidad de las multas y devolver el total a pagar
    Parametros:
        - multas_radar: multas por radar del usuario
        - multas_ITV: multas por ITV del usuario
        - multas_estupefacientes: multas por estupefacientes del usaurio
    Salidas:
        - bill: la suma total de multas
    """
    bill = int(multas_radar) + int(multas_ITV) + int(multas_estupefacientes)
    return int(bill)

help(check_DGT)
help(check_username)
help(check_nif)
help(check_phone)
help(calculate_bill)