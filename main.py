import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, SIGNAL
import time

#HW INFO modules
import cpuinfo
import psutil
import wmi
import pyamd_adl
from pyadl import *
import math as m

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            self.timer.stop()
            if UIFunctions.returnStatus() == 1:

                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
            
            self.timer.start(1000)

        # SET TITLE BAR
        self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ##initialize Static values
        self.setStaticValues()
        ## CALL THE setDynamicValues() FUNCTION REPEATEDLY

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.setDynamicValues)
        self.timer.start(0)

    ## SET ALL VALUES
    def setStaticValues(self):
        all_cpu_data = self.fetch_all_cpu_info()
        all_gpu_data = self.fetch_all_gpu_info()
        all_ram_data = self.fetch_all_ram_info()

        ##SETTING Name labels
        self.ui.label_cpu_name.setText(str(all_cpu_data["cpu_name"]))
        self.ui.label_gpu_name.setText(str(all_gpu_data["gpu_name"]))

        ##SETTING RAM memory label values
        htmlTextFormatRamTotal = """<p><span style=" font-weight:600;">Total:</span> {TOTAL_RAM_VALUE} GB</p>"""
        self.ui.totalSize_label_ram.setText(htmlTextFormatRamTotal.replace("{TOTAL_RAM_VALUE}",str(all_ram_data["ram_total"])))

        ##SETTING Max frequency labels
        htmlTextFormatCpuMaxFreq = """<p>Max Frequency: {CPU_MAXFREQ_VALUE} MHz</p>"""
        self.ui.label__max_cpu_freq.setText(htmlTextFormatCpuMaxFreq.replace("{CPU_MAXFREQ_VALUE}",str(all_cpu_data["cpu_max_freq"])))
        htmlTextFormatGpuMaxFreq = """<p>Max Frequency: {GPU_MAXFREQ_VALUE} MHz</p>"""
        self.ui.label_gpu_max_freq.setText(htmlTextFormatGpuMaxFreq.replace("{GPU_MAXFREQ_VALUE}",str(all_gpu_data["gpu_max_freq"])))

        ##SETTING CPU core labels
        htmlTextFormatCpuPhyCores = """<p>Physical Processors: {PHYSICAL_CORES_VALUE}</p>"""
        self.ui.label_physical_cores.setText(htmlTextFormatCpuPhyCores.replace("{PHYSICAL_CORES_VALUE}",str(all_cpu_data["cpu_cores_physical"])))
        htmlTextFormatCpuLogCores = """<p>Logical Processors: {LOGICAL_CORES_VALUE}</p>"""
        self.ui.label_logical_cores.setText(htmlTextFormatCpuLogCores.replace("{LOGICAL_CORES_VALUE}",str(all_cpu_data["cpu_cores_logical"])))

        ##SETTING GPU memory and memory freq labels
        htmlTextFormatGpuMemSize = """<p>Total VRAM: {VRAM_SIZE_VALUE} GB</p>"""
        self.ui.label_gpu_max_vram.setText(htmlTextFormatGpuMemSize.replace("{VRAM_SIZE_VALUE}",str(all_gpu_data["gpu_vram_total"])))



    def setDynamicValues(self):
        all_cpu_data = self.fetch_all_cpu_info()
        all_gpu_data = self.fetch_all_gpu_info()
        all_ram_data = self.fetch_all_ram_info()
        app.processEvents()

        ##SETTING percentage label VALUES
        htmlTextFormatPercentLabel = """<b>{PERCENT_VALUE}%</b>"""
        self.ui.usage_label_cpu.setText(htmlTextFormatPercentLabel.replace("{PERCENT_VALUE}",str(all_cpu_data["cpu_usage_percentage"])))
        self.ui.usage_label_gpu.setText(htmlTextFormatPercentLabel.replace("{PERCENT_VALUE}",str(all_gpu_data["gpu_usage_percentage"])))
        self.ui.usage_label_ram.setText(htmlTextFormatPercentLabel.replace("{PERCENT_VALUE}",str(all_ram_data["ram_usage_percentage"])))
        app.processEvents()

        ##SETTING Frequency label VALUES of BIG LABELS
        htmlTextFormatFreqLabelBig = """<p><span style=" font-weight:600;">Freq: </span>{FREQ_VALUE} MHz</p>"""
        self.ui.freq_label_cpu.setText(htmlTextFormatFreqLabelBig.replace("{FREQ_VALUE}",str(all_cpu_data["cpu_current_freq"])))
        self.ui.freq_label_gpu.setText(htmlTextFormatFreqLabelBig.replace("{FREQ_VALUE}",str(all_gpu_data["gpu_current_freq"])))
        app.processEvents()

        ##SETTING TEMPERATURE label values
        htmlTextFormatTemperature = """<p><span style=" font-weight:600;">Temperature:</span> {TEMPERATURE_VALUE} °C</p>"""
        self.ui.temp_label_cpu.setText(htmlTextFormatTemperature.replace("{TEMPERATURE_VALUE}",str(all_cpu_data["cpu_temp"])))
        self.ui.temp_label_gpu.setText(htmlTextFormatTemperature.replace("{TEMPERATURE_VALUE}",str(all_gpu_data["gpu_temp"])))
        app.processEvents()

        ##SETTING RAM memory label values
        htmlTextFormatRamUsed = """<p><span style=" font-weight:600;">Used:</span> {USED_RAM_VALUE} GB</p>"""
        self.ui.usedSize_label_ram.setText(htmlTextFormatRamUsed.replace("{USED_RAM_VALUE}",str(all_ram_data["ram_used"])))
        app.processEvents()

        ##SETTING GPU memory and memory freq labels
        htmlTextFormatGpuMemFreq = """<p>Memory Freq: {GPU_MEMFREQ_VALUE} MHz</p>"""
        self.ui.label_gpy_mem_freq.setText(htmlTextFormatGpuMemFreq.replace("{GPU_MEMFREQ_VALUE}",str(all_gpu_data["gpu_memory_freq"])))
        app.processEvents()

        self.progressBarValue(all_cpu_data["cpu_usage_percentage"],self.ui.circularProgress_CPU,"rgba(085, 170, 255, 255)")
        self.progressBarValue(all_gpu_data["gpu_usage_percentage"],self.ui.circularProgress_GPU,"rgba(255, 040, 090, 255)")
        self.progressBarValue(all_ram_data["ram_usage_percentage"],self.ui.circularProgress_RAM,"rgba(170, 000, 255, 255)")
        app.processEvents()

    def fetch_all_cpu_info(self):
        ## CPU INFO FETCH ##
        ####################
        #Fetch exact name of cpu
        cpu_name = str(cpuinfo.get_cpu_info()["brand_raw"].replace("with","").replace("Radeon","").replace("Vega","").replace("Graphics","").strip())
        app.processEvents()

        #Physical cores
        cpu_cores_physical = int(psutil.cpu_count(logical=False))
        app.processEvents()

        #Logical cores
        cpu_cores_logical = int(psutil.cpu_count(logical=True))
        app.processEvents()

        # CPU frequency Max
        cpufreq = psutil.cpu_freq()
        cpu_max_freq = int(cpufreq.max)
        app.processEvents()

        #current frequency
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        all_sensors = w.Sensor()
        count = 0
        cpu_current_freq = 0
        for sensor in all_sensors:
            if sensor.SensorType == "Clock":
                if("CPU Core" in sensor.Name):
                    count += 1
                    cpu_current_freq += sensor.Value
        if(count != 0):
            cpu_current_freq = cpu_current_freq / count
        cpu_current_freq = int(m.ceil(cpu_current_freq))
        app.processEvents()

        #CPU usage overall
        cpu_usage_percentage = int(m.floor(psutil.cpu_percent()))
        app.processEvents()

        #CPU Temperature
        cpu_temp = 0
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            #print(sensor)
            if sensor.SensorType == 'Temperature':
                if(sensor.Name == "CPU Package"):
                    cpu_temp = sensor.Value
        cpu_temp = int(m.ceil(cpu_temp))
        app.processEvents()

        all_cpu_data = {
            "cpu_name" : cpu_name,
            "cpu_cores_physical" : cpu_cores_physical,
            "cpu_cores_logical" : cpu_cores_logical,
            "cpu_max_freq" : cpu_max_freq,
            "cpu_current_freq" : cpu_current_freq,
            "cpu_usage_percentage" : cpu_usage_percentage,
            "cpu_temp" : cpu_temp
        }
        app.processEvents()

        return all_cpu_data

    def fetch_all_gpu_info(self):
        ## GPU INFO FETCH AMD ##
        ########################
        #Fetch GPU name 
        devices = ADLManager.getInstance().getDevices()
        for device in devices:
            gpu = str(device.adapterName)
            gpu = gpu.replace('b','')
            gpu_name = gpu.replace("'","").replace("Series","")
        app.processEvents()

        #Fetch GPU VRAM size
        for adapter in pyamd_adl.adapters:
            memory = adapter.memory
            gpu_vram_total = int((memory.size)/(1024**3))
        app.processEvents()

        #Fetch GPU core clocks along with maximum and minimum clocks
        for device in devices:
            coreFrequencyMin, coreFrequencyMax = device.getEngineClockRange()
            gpu_current_freq = int(device.getCurrentEngineClock())
            gpu_max_freq = int(coreFrequencyMax)

        #Fetch GPU Temperature
            gpu_temp = int(device.getCurrentTemperature())

        #Fetch GPU usage
            gpu_usage_percentage = int(device.getCurrentUsage())

        #fetch GPU memory freq
            gpu_memory_freq = int(device.getCurrentMemoryClock())
        app.processEvents()

        all_gpu_data = {
            "gpu_name": gpu_name,
            "gpu_vram_total": gpu_vram_total,
            "gpu_current_freq": gpu_current_freq,
            "gpu_max_freq" : gpu_max_freq,
            "gpu_temp" : gpu_temp,
            "gpu_usage_percentage" : gpu_usage_percentage,
            "gpu_memory_freq" : gpu_memory_freq
        }

        return all_gpu_data
    
    def fetch_all_ram_info(self):
        
        total_system_memory = round(float(m.ceil(psutil.virtual_memory()[0]/(1024**3))),1)
        available_system_memory = round(psutil.virtual_memory()[1]/(1024**3),1)
        used_system_memory = round((total_system_memory - available_system_memory),1)
        percentage_used_system_memory = int(psutil.virtual_memory()[2])
        app.processEvents()

        all_ram_data = {
            "ram_total" : total_system_memory,
            "ram_available" : available_system_memory,
            "ram_used" : used_system_memory,
            "ram_usage_percentage" : percentage_used_system_memory
        }
        app.processEvents()
        
        return all_ram_data

    def progressBarValue(self, value, frame_widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        frame_widget.setStyleSheet(newStylesheet)

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())