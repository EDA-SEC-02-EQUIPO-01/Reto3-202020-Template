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
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------
def analizador_nuevo():
    adt_analizador={"accidentes":None,
                    "fechas_accidente":None
                    }
    adt_analizador["accidentes"]=lt.newList()
    adt_analizador["fechas_accidente"]=om.newMap(comparefunction=compareDates)
    return adt_analizador
# Funciones para agregar informacion al catalogo
def agregar_accidente(analizador,accidente):
    lt.addLast(analizador["accidentes"],accidente)
    actualizar_fechas(analizador["fechas_accidente"],accidente)
    return analizador

def actualizar_fechas(map,accidente):
    tiempo_accidente = accidente["Start_Time"]
    fecha_accidente = datetime.datetime.strptime(tiempo_accidente, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fecha_accidente.date())
    if entry is None:
        datentry = newDataEntry(accidente)
        om.put(map, fecha_accidente.date(), datentry)
    else:
        datentry = me.getValue(entry)
    agregar_fecha_del_accidente(datentry, accidente)
    return map


def agregar_fecha_del_accidente(entrada,accidente):
    lista=entrada["lista_de_accidentes"]
    lt.addLast(lista,accidente)
    severidad=entrada["severidad_del_accidente"]
    severidadconf=m.get(severidad,accidente["Severity"])
    if severidadconf is None:
        entry=nueva_fecha(accidente["Severity"])
        lt.addLast(entry["lista_de_accidentes"],accidente)
        m.put(severidad,accidente["Severity"],entry)
    else:
        entry = me.getValue(severidadconf)
        lt.addLast(entry["lista_de_accidentes"], accidente)
    return entrada

def newDataEntry(crime):
    entry = {"severidad_del_accidente": None, 
             "lista_de_accidentes": None}
    
    entry["severidad_del_accidente"] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareSeverity)
    entry["lista_de_accidentes"] = lt.newList()
    return entry

def nueva_fecha(severidad):    
    entry={"severidad_del_accidente":None,
           "lista_de_accidentes":None
           }
    entry["severidad_del_accidente"]=severidad
    entry["lista_de_accidentes"]=lt.newList()
    return entry
# ==============================
# Funciones de consulta
# ==============================
def num_accidentes(lst):
    return lt.size(lst["accidentes"])

def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer["fechas_accidente"])

def num_nodos(analyzer):
    """
    Numero de nodos en un arbol
    """
    return om.size(analyzer["fechas_accidente"])

def busqueda_por_fechas(analyzer,initialDate):
    lst = om.values(analyzer["fechas_accidente"], initialDate,initialDate)
    lstiterator = it.newIterator(lst)
    totcrimes = 0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        totcrimes += lt.size(lstdate["lista_de_accidentes"])
    return totcrimes


# ==============================
# Funciones de Comparacion
# ==============================
def compareDates (id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareSeverity (id1, id2):
    """
    Compara dos crimenes
    """
    id2=me.getKey(id2)
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
