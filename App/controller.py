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

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analizador=model.analizador_nuevo()
    return analizador


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accidente in input_file:
        model.agregar_accidente(analyzer, accidente)
    return analyzer



# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def cantidad_de_accidentes(lst):
    return model.num_accidentes(lst)

def altura_arbol(tree):
    return model.indexHeight(tree)

def cantidad_nodos(tree):
    return model.num_nodos(tree)

def accidentes_por_fechas(analyzer, initialDate):
    
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    return model.busqueda_por_fechas(analyzer, initialDate.date())
                                  
def accidentes_por_fechas_anteriores(analyzer, FinalDate):
    
    FinalDate = datetime.datetime.strptime(FinalDate, '%Y-%m-%d')
    return model.busqueda_por_fechas_anteriores(analyzer, FinalDate.date())

def accidentes_por_horas(analyzer,initialDate, FinalDate):
    initialDate = datetime.datetime.strptime(initialDate, '%H:%M:%S')
    FinalDate = datetime.datetime.strptime(FinalDate, '%H:%M:%S')
    return model.accidentes_por_horas(analyzer, initialDate.time(),FinalDate.time())


