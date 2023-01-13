import csv

def check_DGT(direccion):
   """"Esta función se dedica a abrir el documento, a leerlo y partir los datos; y finalmente cerrar el archivo.
   :param direccion: Es la dirección que tiene el archivo dentro de la carpeta donde esta guardada.
   :return Te devuelve los datos que ha corregido y los sobreescribe en el archivo original.
   """
   with open(direccion, 'r', encoding='utf-8') as file:
       fichero = file.readlines()
       fichero_partido = []
   with open(direccion, 'w', encoding='utf-8', newline='') as documento:
       titulos = ['Nombre', 'Apellidos', 'DNI', 'Teléfono', 'País', 'Vehículo', 'Multas Radar',
                  'Multas ITV', 'Multas Estupefacientes', 'Total Multas']
       escribir = csv.DictWriter(documento, fieldnames=titulos)
       escribir.writeheader()
       for datos in fichero:
           fichero_partido.append(datos.split(','))
       lista_final = []
       for lista in fichero_partido:
           dict_lista = {}
           dict_lista['Nombre'] = lista[0]
           dict_lista['Apellidos'] = lista[1]
           dict_lista['DNI'] = lista[2]
           dict_lista['Teléfono'] = lista[3]
           dict_lista['Vehículo'] = lista[4]
           dict_lista['Multas Radar'] = lista[5]
           dict_lista['Multas ITV'] = lista[6]
           dict_lista['Multas Estupefacientes'] = lista[7]
           lista_final.append(dict_lista)

       lista_final.pop(0)

       for datos_dgt in lista_final:
           datos_dgt['Nombre'] = check_username(datos_dgt['Nombre'])
           datos_dgt['Apellidos'] = check_username(datos_dgt['Apellidos'])
           datos_dgt['Teléfono'] = check_phone(datos_dgt['Teléfono'])
           datos_dgt['DNI'] = check_nif(datos_dgt['DNI'])
           datos_dgt['Total Multas'] = calculate_bill(datos_dgt['Multas Radar'], datos_dgt['Multas ITV'],
                                                      datos_dgt['Multas Estupefacientes'])

           escribir.writerow(datos_dgt)
   return
