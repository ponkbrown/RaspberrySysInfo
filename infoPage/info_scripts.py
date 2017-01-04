import platform
import os
import subprocess
import re
from datetime import datetime

def cpu_detalles():
    cpu_info = os.popen( "cat /proc/cpuinfo | grep 'model name\|Hardware\|Serial'|uniq").readlines()

    cpu_info = [ re.sub(r'\s', '', s) for s in cpu_info]

    return cpu_info

datos_sistema = { 'hora_actual' : datetime.now().strftime('%d-%b-%Y , %I : %m : %S %p '),
        'nombre_host' : platform.node()}
