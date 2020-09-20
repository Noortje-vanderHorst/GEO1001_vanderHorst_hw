#-- GEO1001.2020--hw01
#-- Noortje van der Horst
#-- 4697952

import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import thinkstats2
import thinkplot
import numpy as np


def pmfFiveSensors(data_all_sensors):
    probability_counts = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp = sensor["Temperature"]
        counts = data_temp.value_counts()
        probability = counts / len(data_temp)
        probability = probability.sort_index()
        probability_counts.append(probability)

    fig, ax = plt.subplots(1, 5, sharey=True)
    plot_number = 1
    for sensor in probability_counts:
        ax[(plot_number-1)].bar(sensor.index, sensor)
        ax[(plot_number-1)].set(title=sensor_names[(plot_number-1)])
        plot_number += 1
    fig.suptitle(f"PMF Distribution Temperature for 5 sensors")
    plt.setp(ax[2], xlabel="Temperature [degrees Celsius]")
    plt.setp(ax[0], ylabel="Mass Probability")
    plt.show()


def pdfFiveSensorsTemperature(data_all_sensors):
    data_temp= []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor["Temperature"])

    fig, ax = plt.subplots(1, 5, sharey=True)
    plot_number = 1
    for sensor in data_temp:
        ax[(plot_number-1)].hist(x=sensor, bins='auto', density=True, color=(0.2, 0.8, 1), alpha=0.7, rwidth=0.85)
        ax[(plot_number-1)].set(title=sensor_names[(plot_number-1)])
        plot_number += 1
    fig.suptitle(f"PDF Distribution Temperature for 5 sensors")
    plt.setp(ax[2], xlabel="Temperature [degrees Celsius]")
    plt.setp(ax[0], ylabel="Probability Density")
    plt.show()


def cdfFiveSensors(data_all_sensors):
    data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor["Temperature"])

    fig, ax = plt.subplots(1, 5, sharey=True)
    plot_number = 1
    for sensor in data_temp:
        ax[(plot_number-1)].hist(x=sensor, bins='auto', density=True, cumulative=True, color=(0.2, 0.8, 1), alpha=0.7, rwidth=0.85)
        ax[(plot_number-1)].set(title=sensor_names[(plot_number-1)])
        plot_number += 1
    fig.suptitle(f"CDF Distribution Temperature for 5 sensors")
    plt.setp(ax[2], xlabel="Temperature [degrees Celsius]")
    plt.setp(ax[0], ylabel="Cumulative Probability Density")
    plt.show()

def statsWindSpeed(data_all_sensors):
    data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor["Wind Speed"])

    fig, ax = plt.subplots(1, 5)
    plot_number = 1
    for sensor in data_temp:
        density = stats.gaussian_kde(sensor)
        n, x, _ = ax[(plot_number - 1)].hist(x=sensor, bins='auto', density=True, color=(0.2, 0.8, 1), alpha=0.7, rwidth=0.85)
        ax[(plot_number - 1)].plot(x, density(x))
        ax[(plot_number - 1)].set(title=sensor_names[(plot_number - 1)])
        plot_number += 1
    fig.suptitle(f"PDF Distribution Wind Speed for 5 sensors")
    plt.setp(ax[2], xlabel="Wind Speed [m/s]")
    plt.setp(ax[0], ylabel="Probability Density")
    plt.show()


def statsWindSpeedLine(data_all_sensors):
    data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor["Wind Speed"])

    fig, ax = plt.subplots(1, 5, sharey=True)
    plot_number = 0
    for sensor in data_temp:
        density = stats.gaussian_kde(sensor)
        n, x, _ = ax[plot_number].hist(x=sensor, bins='auto', density=True, color=(0.2, 0.8, 1), alpha=0, rwidth=0.85)

        midpoints = 0.5 * (x[1:] + x[:-1])
        begin_point = [x[0] - (x[1] - x[0]) / 2]
        end_point = [x[-1] + (x[-1] - x[-2]) / 2]
        midpoints = np.insert(midpoints, 0, begin_point)
        midpoints = np.insert(midpoints, len(midpoints), end_point)

        n = np.insert(n, 0, 0)
        n = np.append(n, 0)

        ax[plot_number].plot(midpoints, n)
        ax[plot_number].plot(x, density(x))

        ax[plot_number].set(title=sensor_names[plot_number])
        plot_number += 1

    fig.suptitle(f"PDF Distribution Wind Speed for 5 sensors")
    plt.setp(ax[2], xlabel="Wind Speed [m/s]")
    plt.setp(ax[0], ylabel="Probability Density")
    plt.show()


def statsWindSpeedLineSearborn(data_all_sensors):
    data_temp = []
    sensor_names = ["A", "B", "C", "D", "E"]
    for sensor in data_all_sensors:
        data_temp.append(sensor["Wind Speed"])

    fig, ax = plt.subplots(1, 5, sharey=True, sharex=True)
    plot_number = 0
    for sensor in data_temp:
        # sns.distplot(sensor, ax=ax[plot_number], norm_hist=True)
        n, x, _ = ax[plot_number].hist(x=sensor, bins='auto', density=True, color=(0.2, 0.8, 1), alpha=0, rwidth=0.85)

        midpoints = 0.5 * (x[1:] + x[:-1])
        begin_point = [x[0] - (x[1] - x[0]) / 2]
        end_point = [x[-1] + (x[-1] - x[-2]) / 2]
        midpoints = np.insert(midpoints, 0, begin_point)
        midpoints = np.insert(midpoints, len(midpoints), end_point)

        n = np.insert(n, 0, 0)
        n = np.append(n, 0)

        ax[plot_number].plot(midpoints, n, label="pdf")
        sns.distplot(sensor, ax=ax[plot_number], label="kde", hist=False, kde=True)
        ax[plot_number].set(title=sensor_names[plot_number])
        plot_number += 1

    fig.suptitle(f"PDF Distribution Wind Speed for 5 sensors")
    plt.setp(ax[2], xlabel="Wind Speed [m/s]")
    plt.setp(ax[0], ylabel="Probability Density")
    plt.show()




