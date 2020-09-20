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
import seaborn as sns

sns.set_style("darkgrid")

def scatterplotPerVariable(data_all_sensors, column_name):
    data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor[column_name])

    visited = []
    fig, ax = plt.subplots(2, 5, sharey=True, sharex=True)
    plot_number = 1
    for sensor_id in sensor_names:
        print(len(data_temp[sensor_names.index(sensor_id)]))
        current_id = 0
        while current_id < 5:
            if sensor_names[current_id] not in visited and sensor_names[current_id] != sensor_id:
                sensor1 = data_temp[sensor_names.index(sensor_id)]
                sensor2 = data_temp[current_id]
                if len(sensor1) != len(sensor2):
                    sensor1 = np.interp(np.linspace(0,len(sensor2), len(sensor2)),
                                        np.linspace(0,len(sensor1),len(sensor1)),
                                        sensor1)
                if plot_number < 6:
                    ax[0, (plot_number - 1)].scatter(sensor1, sensor2)
                    ax[0, (plot_number - 1)].set(title=f'{sensor_names[sensor_names.index(sensor_id)]} x {sensor_names[current_id]}')
                if plot_number >= 6:
                    ax[1, (plot_number - 1) - 5].scatter(sensor1, sensor2)
                    ax[1, (plot_number - 1) - 5].set(title=f'{sensor_names[sensor_names.index(sensor_id)]} x {sensor_names[current_id]}')

                plot_number += 1
            current_id += 1
        visited.append(sensor_id)
    plt.show()

def plotCorrelations(data_all_sensors):
    column_names = ["Temperature", "WBGT", "Crosswind Speed"]
    sensor_names = ["A", "B", "C", "D", "E"]
    pearson_r_temp = []
    pearson_r_wet_bulb = []
    pearson_r_crosswind = []
    spearmans_r_temp = []
    spearmans_r_wet_bulb = []
    spearmans_r_crosswind = []
    xaxis_labels = []

    for column in column_names:
        data_temp = []
        for sensor in data_all_sensors:
            data_temp.append(sensor[column])

        visited = []
        for sensor_id in sensor_names:
            current_id = 0
            while current_id < 5:
                if sensor_names[current_id] not in visited and sensor_names[current_id] != sensor_id:
                    if column == "Temperature":
                        xaxis_labels.append(f"{sensor_id}x{sensor_names[current_id]}")
                    sensor1 = data_temp[sensor_names.index(sensor_id)]
                    sensor2 = data_temp[current_id]
                    if len(sensor1) != len(sensor2):
                        sensor1 = np.interp(np.linspace(0,len(sensor2), len(sensor2)),
                                            np.linspace(0,len(sensor1),len(sensor1)),
                                            sensor1)
                    pearson_r, p_value = stats.pearsonr(sensor1, sensor2)
                    spearmans_r, p_value = stats.spearmanr(sensor1, sensor2)
                    if column == "Temperature":
                        pearson_r_temp.append(pearson_r)
                        spearmans_r_temp.append(spearmans_r)
                    if column == "WBGT":
                        pearson_r_wet_bulb.append(pearson_r)
                        spearmans_r_wet_bulb.append(spearmans_r)
                    if column == "Crosswind Speed":
                        pearson_r_crosswind.append(pearson_r)
                        spearmans_r_crosswind.append(spearmans_r)
                current_id += 1
            visited.append(sensor_id)

    fig, ax = plt.subplots(1, 2, sharey=True)
    fig.suptitle("Pearson and Pearson's Correlations")
    sns.scatterplot(xaxis_labels, pearson_r_temp, ax=ax[0])
    sns.scatterplot(xaxis_labels, pearson_r_wet_bulb, ax=ax[0])
    sns.scatterplot(xaxis_labels, pearson_r_crosswind, ax=ax[0])
    ax[0].set(title='Pearson Correlations all sensors, 3 variables')
    ax[0].set_xlabel('Sensor combinations')
    ax[0].set_ylabel('Pearson r')

    sns.scatterplot(xaxis_labels, spearmans_r_temp, ax=ax[1])
    sns.scatterplot(xaxis_labels, spearmans_r_wet_bulb, ax=ax[1])
    sns.scatterplot(xaxis_labels, spearmans_r_crosswind, ax=ax[1])
    ax[1].set(title='Spearman Correlations all sensors, 3 variables')
    ax[1].set_xlabel('Sensor combinations')
    ax[1].set_ylabel("Spearman's r")

    fig.legend(["Temperature", "Wet Bulb Globe", "Crosswind Speed"], loc='upper center', bbox_to_anchor=(0.5, 0.15), fancybox=True)
    fig.subplots_adjust(bottom=0.25)
    plt.show()
