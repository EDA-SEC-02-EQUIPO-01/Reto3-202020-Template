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
                    "fechas_accidente":None,
                    "horas_accidentes":None
                    }
    adt_analizador["accidentes"]=lt.newList()
    adt_analizador["fechas_accidente"]=om.newMap(omaptype="RBT",comparefunction=compareDates)
    adt_analizador["horas_accidentes"]=om.newMap(omaptype="RBT",comparefunction=compareDates)

    return adt_analizador

# Funciones para agregar informacion al catalogo

def agregar_accidente(analizador,accidente):
    lt.addLast(analizador["accidentes"],accidente)
    actualizar_fechas(analizador["fechas_accidente"],accidente)
    agregar_hora_de_accidentes(analizador["horas_accidentes"],accidente)
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
    severidad=entrada["fecha_del_accidente"]
    tiempo_accidente = accidente["Start_Time"]
    entrada["Date"]=datetime.datetime.strptime(tiempo_accidente, '%Y-%m-%d %H:%M:%S')
    severidadconf=m.get(severidad,accidente["Severity"])
    if accidente["Severity"] not in entrada["severidades_reportadas"]:
        entrada["severidades_reportadas"].append(accidente["Severity"])
    if severidadconf is None:
        entry=nueva_fecha(accidente["Severity"])
        lt.addLast(entry["lista_de_accidentes"],accidente)
        m.put(severidad,accidente["Severity"],entry)
    else:
        entry = me.getValue(severidadconf)
        lt.addLast(entry["lista_de_accidentes"], accidente)
    return entrada


def agregar_hora_de_accidentes(map, accidente):
    tiempo_accidente = accidente["Start_Time"]
    fecha_accidente = datetime.datetime.strptime(tiempo_accidente, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, fecha_accidente.time())
    if entry is None:
        datentry = newHourEntry(accidente)
        om.put(map, fecha_accidente.time(), datentry)
    else:
        datentry = me.getValue(entry)
    configurar_hora_del_accidente(datentry, accidente)
    return map

def configurar_hora_del_accidente(entrada,accidente):
    severidad=entrada["hora_del_accidente"]
    tiempo_accidente = accidente["Start_Time"]
    entrada["Date"]=datetime.datetime.strptime(tiempo_accidente, '%Y-%m-%d %H:%M:%S')
    severidadconf=m.get(severidad,accidente["Severity"])
    if accidente["Severity"] not in entrada["severidades_reportadas"]:
        entrada["severidades_reportadas"].append(accidente["Severity"])
    if severidadconf is None:
        entry=nueva_fecha(accidente["Severity"])
        lt.addLast(entry["lista_de_accidentes"],accidente)
        m.put(severidad,accidente["Severity"],entry)
    else:
        entry = me.getValue(severidadconf)
        lt.addLast(entry["lista_de_accidentes"], accidente)
    return entrada


def newHourEntry(crime):
    entry = {"hora_del_accidente": None,
             "severidades_reportadas":None,
             "Date":None}
    
    entry["hora_del_accidente"] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareSeverity)
    entry["severidades_reportadas"]=[]
    return entry


def newDataEntry(crime):
    entry = {"fecha_del_accidente": None,
             "severidades_reportadas":None,
             "Date":None}
    
    entry["fecha_del_accidente"] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareSeverity)
    entry["severidades_reportadas"]=[]
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

def estructura_criminal(lista):
    estr_crimenes={"Severidad de los crimenes":None,
                   "Cantidad de crimenes":0}
    estr_crimenes["Severidad de los crimenes"]=lista["severidad_del_accidente"]
    estr_crimenes["Cantidad de crimenes"]+=lt.size(lista["lista_de_accidentes"])
    return estr_crimenes

def busqueda_por_fechas(analyzer,initialDate):
    lst = om.values(analyzer["fechas_accidente"], initialDate,initialDate)
    lstiterator = it.newIterator(lst)
    crimenes_por_severidad=[]
    totcrimes = 0
    total=0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        the_map=lstdate["fecha_del_accidente"]
        for g in lstdate["severidades_reportadas"]:
            totcrimes = m.get(the_map,g)
            totcrimes = me.getValue(totcrimes)
            estr_crimenes=estructura_criminal(totcrimes)
            crimenes_por_severidad.append(estr_crimenes)
            total+=lt.size(totcrimes["lista_de_accidentes"])
    return (crimenes_por_severidad,total)

def busqueda_por_fechas_anteriores(analyzer,initialDate):
    min_valor=om.minKey(analyzer["fechas_accidente"])
    lst = om.values(analyzer["fechas_accidente"], min_valor,initialDate)
    lstiterator = it.newIterator(lst)
    totcrimes = lt.newList()
    llave_mayor=0
    comprobante1=0
    fecha=0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        the_map= lstdate["fecha_del_accidente"]
        comprobante2=0
        for g in lstdate["severidades_reportadas"]:
            totcrimes = m.get(the_map,g)
            totcrimes = me.getValue(totcrimes)
            llave_mayor+=lt.size(totcrimes["lista_de_accidentes"])
            comprobante2+=lt.size(totcrimes["lista_de_accidentes"])
        if comprobante1<comprobante2:
            comprobante1=comprobante2
            fecha=lstdate["Date"]
        
    return (llave_mayor,str(fecha.date()),comprobante1)

def accidentes_por_horas(analyzer,initialDate, FinalDate):
    lst = om.values(analyzer["horas_accidentes"], initialDate,FinalDate)
    lstiterator = it.newIterator(lst)
    crimenes_por_severidad=[]
    totcrimes = 0
    total=0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        the_map=lstdate["hora_del_accidente"]
        for g in lstdate["severidades_reportadas"]:
            totcrimes = m.get(the_map,g)
            totcrimes = me.getValue(totcrimes)
            estr_crimenes=estructura_criminal(totcrimes)
            crimenes_por_severidad.append(estr_crimenes)
            total+=lt.size(totcrimes["lista_de_accidentes"])
    return (crimenes_por_severidad,total)



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
