#-- GEO1001.2020--hw01
#-- Noortje van der Horst
#-- 4697952

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import xlwt
import thinkstats2
import thinkplot
# import brfss
from scipy import stats
import seaborn as sns
import math

def plotCDF(data_all_sensors):
    data_temp = []
    data_wind_speed = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor["Temperature"])
        data_wind_speed.append(sensor["Wind Speed"])

    fig, ax = plt.subplots(2, 5)
    plot_number = 0
    for sensor in data_temp:
        ax[0, plot_number].hist(x=sensor, bins='auto', density=True, cumulative=True, alpha=0.7, rwidth=0.85)
        ax[0, plot_number].set(title=sensor_names[plot_number])
        plot_number += 1

    plot_number = 0
    for sensor in data_wind_speed:
        n, bins, _ = ax[1, plot_number].hist(x=sensor, bins='auto', density=True, cumulative=True, alpha=0.7, rwidth=0.85)
        ax[1, plot_number].set(title=sensor_names[plot_number])
        x_axis = range(0, math.ceil(bins[-1]), 2)
        # x_axis = np.linspace(0, bins[-1], 5)
        ax[1, plot_number].set(xticks=x_axis)
        plot_number += 1

    fig.suptitle(f"CDF Distribution Temperature for 5 sensors")
    plt.setp(ax[0, 2], xlabel="Temperature [degrees Celsius]")
    plt.setp(ax[1, 2], xlabel="Wind Speed [m/s]")
    plt.setp(ax[0, 0], ylabel="Cumulative Probability Density")
    plt.setp(ax[1, 0], ylabel="Cumulative Probability Density")
    plt.tight_layout()
    plt.show()


def confidenceIntervalCdf(data_all_sensors, column_name):
    sensor_names = ["A", "B", "C", "D", "E"]
    cols = ["CI min", "mean", "CI max"]
    data = []

    for sensor in sensor_names:
        current_sensor_data = data_all_sensors[sensor_names.index(sensor)][column_name]
        cdf = thinkstats2.Cdf(current_sensor_data, label=column_name)
        # thinkplot.Cdf(cdf, color='b')   # color parameter because the thinkplot default color array was not long enough
        # thinkplot.Show(xlabel=column_name, ylabel='CDF')    # enable for seeing the CDF plot
        interval_min = thinkstats2.Cdf.Value(cdf, p=0.025)
        interval_max = thinkstats2.Cdf.Value(cdf, p=0.975)
        interval_mean = round(current_sensor_data.mean(), 1)
        data.append((interval_min, interval_mean, interval_max))

    confidence_intervals = pd.DataFrame(data, columns=cols, index=sensor_names)
    # print(confidence_intervals)
    return confidence_intervals


def confidenceIntervalToCsv(data_all_sensors, filepath):
    CI_temperature = confidenceIntervalCdf(data_all_sensors, "Temperature")
    CI_wind_speed = confidenceIntervalCdf(data_all_sensors, "Wind Speed")
    joined_intervals = CI_temperature.join(CI_wind_speed, lsuffix=' Temperature', rsuffix=' Wind Speed')
    joined_intervals.to_csv(filepath)


def meansStdsDataframe(data_all_sensors):
    temp_means = []
    wind_speed_means = []
    temp_std = []
    wind_speed_std = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor_id in sensor_names:
        current_sensor_data = data_all_sensors[sensor_names.index(sensor_id)]
        temp_means.append(current_sensor_data["Temperature"].mean())
        temp_std.append(current_sensor_data["Temperature"].std())
        wind_speed_means.append(current_sensor_data["Wind Speed"].mean())
        wind_speed_std.append(current_sensor_data["Wind Speed"].std())
    data_means = {"Temperature mean": temp_means, "Temperature std": temp_std,
                  "Wind speed mean": wind_speed_means, "Wind Speed std": wind_speed_std}
    means_stds = pd.DataFrame(data_means, index=sensor_names)
    print(means_stds)


def tTest(data_all_sensors, sensor_combination):
    sensor1, sensor2 = sensor_combination
    sensor_names = ["A", "B", "C", "D", "E"]
    used_columns = ["FORMATTED DATE-TIME", "Temperature", "Wind Speed"]
    result = {}

    sensor_data1 = data_all_sensors[sensor_names.index(sensor1)].filter(used_columns)
    sensor_data2 = data_all_sensors[sensor_names.index(sensor2)].filter(used_columns)
    data = sensor_data1.set_index(used_columns[0]).join(sensor_data2.set_index(used_columns[0]),
                                                        rsuffix=f" {sensor2}", lsuffix=f" {sensor1}")
    data = data.dropna()
    for column in used_columns[1:]:
        data1 = data[f"{column} {sensor1}"]
        data2 = data[f"{column} {sensor2}"]
        # mean_diff = data1.mean() - data2.mean()
        # SE_means = math.sqrt((data1.std()**2 / len(data1)) + (data2.std()**2 / len(data2)))
        # t_value = (mean_diff - 0) / SE_means
        # ok found built in function that does the same :(
        # at least I know it was correct...
        t, p = stats.ttest_ind(data1, data2)
        result[f"{sensor_combination} {column} t"] = t
        result[f"{sensor_combination} {column} p"] = p

    return result


def getValuesTtest(dataframes_all_sensors):
    sensors = [("E", "D"), ("D", "C"), ("C", "B"), ("B", "A")]
    data = pd.DataFrame(columns=["sensors", "Temperature t", "Temperature p", "Wind Speed t", "Wind Speed p"])
    for sensor_combo in sensors:
        results = []
        key = f"{sensor_combo[0]}{sensor_combo[1]}"
        res_dict = tTest(dataframes_all_sensors, sensor_combo)
        for value_key in res_dict:
            results.append(round(res_dict[value_key], 4))
        data.loc[sensors.index(sensor_combo)] = [key] + results
    data = data.set_index("sensors")
    return data


def printTtest(dataframes_all_sensors):
    print(getValuesTtest(dataframes_all_sensors))


def csvTtest(dataframes_all_sensors, filepath):
    data = getValuesTtest(dataframes_all_sensors)
    data.to_csv(filepath)



