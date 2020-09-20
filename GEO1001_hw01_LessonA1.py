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


def printMeans(data_all_sensors):
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor_id in sensor_names:
        print(f"The means of sensor {sensor_id} are:")
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        # pandas can't calculate the mean of datetimes in a dataframe, but it can calculate them for a series
        # the means of the first column have therefore been calculated separately
        dates = current_sensor_data["FORMATTED DATE-TIME"]
        print(f"FORMATTED DATE-TIMES            {dates.mean()}")
        print(current_sensor_data[current_sensor_data.columns[1:]].mean())

def csvMeans(data_all_sensors):
    sensor_names = ["A", "B", "C", "D", "E"]
    means_list = []
    for sensor_id in sensor_names:
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        means = current_sensor_data[current_sensor_data.columns[1:]].mean()
        means_list.append(round(means, 2))
    means_all_sensors = pd.DataFrame(means_list, index=sensor_names)
    means_all_sensors.to_csv('GEO1001_hw01_A1_means.csv')


def printVariances(data_all_sensors):
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor_id in sensor_names:
        print(f"The variances of sensor {sensor_id} are:")
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        # # pandas can't calculate the variance of datetimes in a dataframe either
        # # so far I haven't figured this one out
        # dates = current_sensor_data["FORMATTED DATE-TIME"]
        # dates_as_array = dates.to_numpy()
        # dates_as_timestamps = []
        # for date in dates_as_array:
        #     dates_as_timestamps.append(pd.Timestamp(date))
        # dates_as_timestamps = np.array(dates_as_timestamps.astype(int))
        # print(dates_as_timestamps)
        # print(f"FORMATTED DATE-TIMES            {???.var()}")

        print(current_sensor_data[current_sensor_data.columns[1:]].var())


def csvVariances(data_all_sensors):
    sensor_names = ["A", "B", "C", "D", "E"]
    vars_list = []
    for sensor_id in sensor_names:
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        var = current_sensor_data[current_sensor_data.columns[1:]].var()
        vars_list.append(round(var, 2))
    means_all_sensors = pd.DataFrame(vars_list, index=sensor_names)
    means_all_sensors.to_csv('GEO1001_hw01_A1_vars.csv')


def printStandardDeviations(data_all_sensors):
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor_id in sensor_names:
        print(f"The standard deviations of sensor {sensor_id} are:")
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        # this has the same problem with the datetimes as the variance function...

        print(current_sensor_data[current_sensor_data.columns[1:]].std())


def csvStandardDeviations(data_all_sensors):
    sensor_names = ["A", "B", "C", "D", "E"]
    stds_list = []
    for sensor_id in sensor_names:
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        stds = current_sensor_data[current_sensor_data.columns[1:]].std()
        stds_list.append(round(stds, 2))
    means_all_sensors = pd.DataFrame(stds_list, index=sensor_names)
    means_all_sensors.to_csv('GEO1001_hw01_A1_stds.csv')


def histogramsTemperature(data_all_sensors, nr_of_bins):
    hist_data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        hist_data_temp.append(sensor['Temperature'])
    n, bins, _ = plt.hist(x=hist_data_temp, bins=nr_of_bins, alpha=0.5)
    plt.title(f"Frequency Temperature for 5 sensors, {nr_of_bins} bins")
    plt.gca().legend(sensor_names)
    if nr_of_bins <= 10:
        plt.xticks(np.around(bins, 1))
    plt.xlabel("Temperature [degrees Celsius]")
    plt.ylabel("Times temperature was measured")
    plt.show()

def frequencyPolygons(data_all_sensors):
    hist_data_temp = []
    colors = [(1, 1, 0.1), (1, 0.2, 0.2), (0.5, 1, 0.5), (0.2, 0.8, 1), (0.98, 0.5, 0.98)]
    nr_of_bins = 50
    for sensor in data_all_sensors:
        hist_data_temp.append(sensor['Temperature'])
    n, bins, _ = plt.hist(x=hist_data_temp, bins=nr_of_bins, alpha=0, color=colors)

    midpoints = 0.5 * (bins[1:] + bins[:-1])
    begin_point = [bins[0] - (bins[1] - bins[0])/2]
    end_point = [bins[-1] + (bins[-1] - bins[-2])/2]
    midpoints = np.insert(midpoints, 0, begin_point)
    midpoints = np.insert(midpoints, len(midpoints), end_point)

    zeroes = np.zeros(len(n)).reshape(len(n), 1)
    n = np.append(n, zeroes, axis=1)
    n = np.insert(n, 0, np.zeros(len(n)), axis=1)

    sensor_names = ["A", "B", "C", "D", "E"]
    x = 0
    for sensor_values in n:
        plt.plot(midpoints, sensor_values, color=colors[x])
        x += 1
    plt.title("Frequency Polygons Temperature for 5 sensors")
    plt.gca().legend(sensor_names)
    plt.xlabel("Temperature [degrees Celsius]")
    plt.ylabel("Times temperature was measured")
    x_axis_label_points = np.round(midpoints, 1)
    plt.xticks(np.linspace(0, 35, 8))
    plt.show()


def boxplotFiveSensors(data_all_sensors, column_name):
    hist_data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        hist_data_temp.append(sensor[column_name])
    plt.boxplot(x=hist_data_temp, labels=sensor_names)
    plt.title(f"Distribution {column_name} for 5 sensors")
    plt.xlabel("Sensor Tag")
    if column_name == "Temperature":
        plt.ylabel("Temperature [degrees Celsius]")
    if column_name == "Direction ‚ True":
        plt.ylabel("Wind Direction [degrees]")      # a better unit for this probably exists
    if column_name == "Wind Speed":
        plt.ylabel("Wind Speed [m/s]")
    plt.show()



