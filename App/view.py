"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from App import controller
from DISClib.ADT import list as lt
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


crimefile = 'us_accidents_small.csv'
accidente1='us_accidents_dis_2016.csv'
accidente2='us_accidents_dis_2017.csv'
accidente3='us_accidents_dis_2018.csv'
accidente4='us_accidents_dis_2019.csv'
# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Busqueda de accidentes en una fecha especifica")
    print("4- Busqueda de accidentes anteriores a una fecha")
    print("5- Busqueda de accidententes un un rango de horas")
    print("6- Busqueda de accidententes por categoria")
    print("7- Busqueda de accidententes por estado")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        #controller.loadData(cont, crimefile)
        year_boi=int(input("marque 1 para cargar los crimenes del año 2016\nmarque 2 para cargar los crimenes del año 2017\nmarque 3 para cargar los crimenes del año 2018\nmarque 4 para cargar los crimenes del año 2019\n"))
        print("\nCargando información de accidentes ....")
        if year_boi==1:
            controller.loadData(cont, accidente1)
        if year_boi==2:
            controller.loadData(cont, accidente2)
        if year_boi==3:
            controller.loadData(cont, accidente3)
        if year_boi==4:
            controller.loadData(cont, accidente4)
        print('Accidentes cargados: ' + str(controller.cantidad_de_accidentes(cont)))
        print('Altura del arbol: ' + str(controller.altura_arbol(cont)))
        print('Elementos en el arbol: ' + str(controller.cantidad_nodos(cont)))

    elif int(inputs[0]) == 3:
        print("\nBuscando accidentes en una fecha especifica: ")
        the_date=input("Ingrese la fecha de la que desea saber: Formato YYYY-MM-DD\n")
        final=controller.accidentes_por_fechas(cont,the_date)
        print(f"Total de accidentes encontrados:{final[1]}\n{final[0]}")

    elif int(inputs[0]) == 4:
        print("\nBuscando accidentes anteriores a una fecha especifica: ")
        the_date=input("Ingrese la fecha de la que desea saber: Formato YYYY-MM-DD\n")
        final=controller.accidentes_por_fechas_anteriores(cont,the_date)
        print(f"Total de accidentes encontrados:{final[0]}\nFecha con mas accidentes:{final[1]} con un total de {final[2]} accidentes")

    elif int(inputs[0]) == 5:
        print("\nBuscando accidentes en una hora especifica: ")
        the_date=input("Ingrese la hora inicial: Formato HH:MM:SS\n")
        the_date2=input("Ingrese la hora final: Formato HH:MM:SS\n")
        final=controller.accidentes_por_horas(cont,the_date,the_date2)
        print(f"Total de accidentes encontrados:{final[1]}\nEl porcentaje de accidentes reportados entre las {the_date} y las {the_date2} es de {round(((final[1]*100)/controller.cantidad_de_accidentes(cont)),1)}%\nCantidad de crimenes reportados por su severidad: {final[0]}")
        
    elif int(inputs[0]) == 6:
        print("\nBuscando accidentes en un rango: ")
        inicial=input("Ingrese la fecha inicial: Formato YYYY-MM-DD\n")
        final=input("Ingrese la fecha final: Formato YYYY-MM-DD\n")
        total=controller.accidentes_en_rango(cont,inicial,final)
        print(f"Total de accidentes encontrados: {total[0]}")
        print(f"Categoría de accidentes más reportada: {total[1]}")

    elif int(inputs[0]) == 7:
        print("\nBuscando estado con más accidentes en un rango: ")
        inicial=input("Ingrese la fecha inicial: Formato YYYY-MM-DD\n")
        final=input("Ingrese la fecha final: Formato YYYY-MM-DD\n")
        total=controller.estados_en_rango(cont,inicial,final)
        print(f"Fecha con más accidentes reportados: {total[0]}")
        print(f"Estado con más accidentes reportados: {total[1]}")
    else:
        sys.exit(0)
sys.exit(0)

