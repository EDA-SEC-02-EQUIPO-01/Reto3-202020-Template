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
    print("3- Requerimento 1")
    print("4- Requerimento 2")
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
        print('Crimenes cargados: ' + str(controller.cantidad_de_accidentes(cont)))
        print('Altura del arbol: ' + str(controller.altura_arbol(cont)))
        print('Elementos en el arbol: ' + str(controller.cantidad_nodos(cont)))

    elif int(inputs[0]) == 3:
        print("\nBuscando accidentes en una fecha especifica: ")
        the_date=input("Ingrese la fecha de la que desea saber: Formato YYYY-MM-DD\n")
        final=controller.accidentes_por_fechas(cont,the_date)
        print(f"Total de crimenes encontrados:{final}")

    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 1 del reto 3: ")

    else:
        sys.exit(0)
sys.exit(0)
