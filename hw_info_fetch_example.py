## CPU INFO FETCH ##
####################
import cpuinfo
import psutil
import wmi
import wmi
import math as m
#Fetch exact name of cpu
print(cpuinfo.get_cpu_info()["brand_raw"].replace("with","").replace("Radeon","").replace("Vega","").replace("Graphics","").strip())
#Physical cores
print("Physical cores:", psutil.cpu_count(logical=False))
#Logical cores
print("Logical:", psutil.cpu_count(logical=True))
# CPU frequency Max
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
#current frequency
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
all_sensors = w.Sensor()
#print(temperature_infos)
count = 0
freq = 0
for sensor in all_sensors:
    if sensor.SensorType == "Clock":
        if("CPU Core" in sensor.Name):
            count += 1
            freq += sensor.Value
freq = freq / count
print(int(m.ceil(freq)), "MHz")
#CPU usage overall
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
#CPU Temperature
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
#print(temperature_infos)
for sensor in temperature_infos:
    #print(sensor)
    if sensor.SensorType == 'Temperature':
        if(sensor.Name == "CPU Package"):
            cpu_temp = int(m.ceil(sensor.Value))

print("CPU Temp : ",cpu_temp,"\u00b0C")

## GPU INFO FETCH AMD ##
########################
import pyamd_adl
from pyadl import *
#Fetch GPU name 
devices = ADLManager.getInstance().getDevices()
for device in devices:
    gpu = str(device.adapterName)
    gpu = gpu.replace('b','')
    gpu = gpu.replace("'","")
    print("GPU Name =",gpu)
#Fetch GPU VRAM size
for adapter in pyamd_adl.adapters:
    memory = adapter.memory
    print("Size:", ((memory.size)/(1024**3)),"GB")
#Fetch GPU core clocks along with maximum and minimum clocks
for device in devices:
    coreFrequencyMin, coreFrequencyMax = device.getEngineClockRange()
    print ("Engine clock: {0} MHz ({1} MHz - {2} MHz)".format(device.getCurrentEngineClock(), coreFrequencyMin, coreFrequencyMax))
#Fetch GPU Temperature
for device in devices:
    print(device.getCurrentTemperature(),"\u00b0C")
#Fetch GPU usage
for device in devices:
    print("Total GPU usage",device.getCurrentUsage(),"%")
#fetch GPU memory clock
for device in devices:
    print("GPU memory clock",device.getCurrentMemoryClock(),"MHz")

## RAM INFO FETCH ##
####################
import psutil
import math as m
total_system_memory = round(float(m.ceil(psutil.virtual_memory()[0]/(1024**3))),1)
available_system_memory = round(psutil.virtual_memory()[1]/(1024**3),1)
used_system_memory = round((total_system_memory - available_system_memory),1)
percentage_used_system_memory = int(psutil.virtual_memory()[2])
print("Total ",total_system_memory,"GB")
print("Available ",available_system_memory,"GB")
print("Used ",used_system_memory," GB")
print("Percentage ",percentage_used_system_memory,"%")