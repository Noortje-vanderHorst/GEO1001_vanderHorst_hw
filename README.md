# GEO1001_vanderHorst_hw
# This file describes in detail what all the pyhton code for hw01 is for. I separated the lessons into 4 different files, called from the main pyhton file. 
# The main pyhton file somretimes includes several options to generate an answer to a question, this will be explained with comments above these functions.

# /////////////////////////////Lesson A1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# > printMeans
# > csvMeans
# > printVariances
# > csvVariances
# > printStandardDeviations
# > csvStandardDeviations
# All these functions take the dataframes of all the sensor data generated in the main file.
# They the calculate a mean statistic for each sensor.
# This result can be either printed or exported to csv file. I found csv fiels easier to read (with excel), which is why I included these functions.

# > histogramsTemperature
# Firsts extracts the right column data from the input dataframes. 
# This method of getting the right data from the larger dataframes containing all the sensor's data is used throughout the assignment.
# Function plots temperature histograms with pyplot, showing all sensor data in 1 histogram with a color legend.
# This was to see the differences bewteen sensors easily, and also to show how the number of bins can impact legibility on this front.
# Number of bins is included in the input to easier answer the question.

# > frequencyPolygons
# Makes a pyplot histogram for each sensor's Temperature values, then plots these as frequency polygons in the same figure, with a color legend.
# This was done to easier see the differences between the sensors.

# > boxplotFiveSensors
# Makes a pyplot boxplot for each of the variables, with the 5 sensors next to eachother to easily compare them.

# /////////////////////////////Lesson A2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# > pmfFiveSensors
# Plots the PMF for Temperature.
# First counts the occurances of each measured temperature value, then normalizes them (/n), and sorts these pobabilities in increasing order.
# The plot is a pyplot bar graph, with each occuring temperature as a bar.

# > pdfFiveSensorsTemperature
# Plots the PDF of Temperature.
# Uses pyplot histogram, with density set to true. PDF is therefor in the shape of bars. Amount of bins left on auto, this visualized well enough.

# > cdfFiveSensors
# Plots the CDF of Temperature.
# Uses the same method as pdfFiveSensorsTemperature, where the histogram also has (cumulative=True) as a parameter.

# > statsWindSpeed
# > statsWindSpeedLine
# > statsWindSpeedLineSearborn
# These functions plot the PDF of the Wind Speed against the kde of that PDF.
# There is 3 versions, as mentioned in the report.
# The first one is the original, where the PDF is plotted with pyplot's histogram.
# The second is a line fitted to that histogram, for a cleaner visualisation.
# The third uses seaborn instead of scipy to fit the kde, as that function covered the values on the right of the minimum of the data as well.

# /////////////////////////////Lesson A3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# > scatterplotPerVariable
# Plots the actual scatterplots of all the variables.
# Not used in answer to question, or included in the main file. Was just for comprehension.

# > plotCorrelations
# Goes through each variable, for each sensor, and appends the pearson's r and spearmans rho to a result list.
# This list is then used to create 2 scatterplots: 1 for pearson, 1 for spearman, and visualizes the corelations of the 3 variables for all possible 10 sensor correlations.
# Correlation pairs were determined going over the 5 sensors one by one, and pairing them with the possible sensors, keeping a list of these second sensors already visited.
# If the potential paired sensor was not visited yet, and not paired with itself, the correlation coefficients were appended to the appropriate list.
# A list of labels was also kept, describing the right order and names of sensor pairs found.


# /////////////////////////////Lesson A4\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# > plotCDF
# Not used in final result, just for comprehension.

# > confidenceIntervalCdf
# > confidenceIntervalToCsv
# Functions were split up for less complexity in the code. First one can be printed to look at the data before it is written to the csv file.

# > confidenceIntervalToCsv
# Takes all the data plus a desired filepath for the csv file, so this path can be determined before the file is made/edited.
# The corresponding temperature values were acquired using thinkstats2 to generate a CDF function, and then finding the values for p = 0.025 and p = 0.975.
# The values within this range would correspond to a total of p = 0.950, since the CDF is symmetrical. 
# The confidence interval's upper and lower bound were written to a pandas dataframe, together with the appropriate mean. This dataframe was then exported to csv.
# The mean was included to be able to check if the interval's boundaries were logical values, and roughly symmetrical about the mean.

# > meansStdsDataframe
# This function just prints the means and stds of Temperature and Wind Speed.
# Not included in final result, just for comprehension.

# > tTest
# > getValuesTtest
# Functions work together, first to generate a dictionary of sensor combinations + Variable + t or p value, and the calculated t and p values.
# The second function then uses this dictionary to generate a pandas dataframe, with a row for each tested sensor combination, and columns for if it is the p or t value, and for which variable.
# A dataframe is returned, which can be either printed or exported to a csv file in the main pyhton file.

# > printTtest
# > csvTtest
# These functions are just for less complexity of the code. They take the dataframe with t and p values from the previous functions, and either print or export it.
