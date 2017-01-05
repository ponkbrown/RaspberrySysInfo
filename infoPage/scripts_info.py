from socket import gethostname
import platform
import os
import subprocess
import re
from datetime import datetime

def get_info():

    info = {}

    # Esto es para sacar la informacion de el procesador con el Serial
    # y el modelo
    cpu = {}
    cpu_info = os.popen( "cat /proc/cpuinfo | grep 'model name\|Hardware\|Serial'|uniq").readlines()

    cpu_info = [ re.sub(r'\s', '', s) for s in cpu_info]

    for x in cpu_info:
        nombre, valor = x.split(':')
        cpu[nombre.capitalize()] = valor

    # Este comando para verificar la temperatura
    temperatura = os.popen('vcgencmd measure_temp').readline()
    temperatura = temperatura.replace('temp=','').strip()


    info['cpu'] = cpu
    info['hostname'] = gethostname()
    info['os'] = platform.platform()
    info['temp'] = temperatura


    return info
