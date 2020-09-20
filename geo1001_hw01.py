#-- GEO1001.2020--hw01
#-- Noortje van der Horst
#-- 4697952

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import xlwt
# import thinkstats2
# import brfss
from scipy import stats
from GEO1001_hw01_LessonA1 import *
from GEO1001_hw01_LessonA2 import *
from GEO1001_hw01_LessonA3 import *
from GEO1001_hw01_LessonA4 import *

def readSensorData():
    # reads the provided xls files into a list of pandas dataframes
    filepath_all_sensors = ('hw01/hw01/HEAT - A_final.xls', 'hw01/hw01/HEAT - B_final.xls',
                            'hw01/hw01/HEAT - C_final.xls','hw01/hw01/HEAT - D_final.xls',
                            'hw01/hw01/HEAT - E_final.xls')
    dataframes = []
    for filepath in filepath_all_sensors:
        dataframe = pd.read_excel(filepath, skiprows=[0, 1, 2, 4])
        dataframes.append(dataframe)
    return dataframes


dataframes_all_sensors = readSensorData()


# ///////////////////Lesson A1\\\\\\\\\\\\\\\\\\\\\\\

# mean statistics for all sensors
# data can be printed or exported to a csv
printMeans(dataframes_all_sensors)
# csvMeans(dataframes_all_sensors)
printVariances(dataframes_all_sensors)
# csvVariances(dataframes_all_sensors)
printStandardDeviations(dataframes_all_sensors)
# csvStandardDeviations(dataframes_all_sensors)

# histograms for temperature, 5 bins
histogramsTemperature(dataframes_all_sensors, 5)
# histograms for temperature, 50 bins
histogramsTemperature(dataframes_all_sensors, 50)

# # frequency polygons plot for temperature
frequencyPolygons(dataframes_all_sensors)

# boxplots of all sensors, wind speed
boxplotFiveSensors(dataframes_all_sensors, "Wind Speed")
# boxplots of all sensors, wind direction
boxplotFiveSensors(dataframes_all_sensors, "Direction ‚ True")
# boxplots of all sensors, temperature
boxplotFiveSensors(dataframes_all_sensors, "Temperature")


# ///////////////////Lesson A2\\\\\\\\\\\\\\\\\\\\\\\

# PMF Temperatures
pmfFiveSensors(dataframes_all_sensors)
# PDF Temperatures
pdfFiveSensorsTemperature(dataframes_all_sensors)
# CDF Temperature
cdfFiveSensors(dataframes_all_sensors)

# PDF & Kernel Density Wind Speed
# I made 2 different versions, 1 with seaborn and 1 with just pyplot, because pyplot did not fit a kde past
# the extent of the original data (past 0 "back" to the x-axis), while seaborn did
# V1: pyplot, 1 option for histogram bins as pdf, 1 option for a line fitted to that as a visualisation
# statsWindSpeed(dataframes_all_sensors)
# statsWindSpeedLine(dataframes_all_sensors)
# V2: pyplot & seaborn
statsWindSpeedLineSearborn(dataframes_all_sensors)


# ///////////////////Lesson A3\\\\\\\\\\\\\\\\\\\\\\\

# Spearman's and Pearson's r for the 3 variables, with all 10 combinations of sensors
plotCorrelations(dataframes_all_sensors)


# ///////////////////Lesson A4\\\\\\\\\\\\\\\\\\\\\\\

# Plot CDF all sensors all variables: neat plots of all CDFs
# plotCDF(dataframes_all_sensors)
# Confidence intervals (95%) for all sensors & all variables, not necessary for the final csv result below
# Can be printed to get a quick look
print(confidenceIntervalCdf(dataframes_all_sensors, "Temperature"))
print(confidenceIntervalCdf(dataframes_all_sensors, "Wind Speed"))

# Confidence interval dataframes to csv file
confidenceIntervalToCsv(dataframes_all_sensors, 'GEO1001_hw01_A4_intervals.csv')

# p-tests for hypothesis
# Included options to just print as a dictionary, or export to csv
printTtest(dataframes_all_sensors)
csvTtest(dataframes_all_sensors, 'GEO1001_hw01_A4_ttest.csv')
