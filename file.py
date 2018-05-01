'''
Created by: Matthew Rogers & [Jack put ur name here]
Stat Programming Final Visualization

Question: Its skeleton code so we can change it to baseball if you want, but rn it's; 
"How does temperature affect running at the state meet?"

Data was scraped from Athletic.net in accordance to their terms of use
If you want to see the scraper itself, I've committted it to my "running-scrapers" repo on
my github account. It's public b/c I can't make private ones

this file created on: 4/29/2018
'''
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#b/c the times in the sheet are in M:S format and its hard to work with that, convert those to seconds
def to_secs(time):
    #take a string in "M:S" and turn it into an integer in seconds
    in_secs = 0
    time = time.split('.')[0]
    split_time = time.split(':')
    in_secs += int(split_time[0]) * 60
    in_secs += int(split_time[1])
    
    return in_secs

def summary_stats(data):
	'''
	A simple function that'll give you the min/max, mean, and quartiles
	of a passed list
	
	takes a list of numbers
	simply prints the stats in a nice format
	'''
	print "--- Summary Statistics ---"
	print "mean:\t", np.mean(data)
	print "min:\t", min(data), " max:\t", max(data)
	print "Percentiles (25, 75):\t", np.percentile(data, 25), " ", np.percentile(data, 75)
	print "IQR:\t", np.percentile(data, 75) - np.percentile(data, 25)
	return

	
#use PANDAS to read the two csv files and format them as dataframes
runner_df = pd.read_csv('C:/Users/matte/Documents/GitHub/Stat-Project/runner_info.csv', header = "infer")
meet_df = pd.read_csv("C:/Users/matte/Documents/GitHub/Stat-Project/meet_info.csv", header = "infer")

#use the function above to make the "finish_time" column integers of seconds instead of "M:S"
# THIS TAKES AN ETERNITY # 
for time in runner_df['finish_time']:
    runner_df.replace(to_replace = time, value = to_secs(time), inplace = True)

#merge the data in one line lmao
merged_df = pd.merge(runner_df, meet_df, on='meet_id')

#define parameters for the loop below
group_list = ["1a", "2a", "3a", "4a", "5a", "6a"]
year_list = ["13", "14", "15", "16", "17"]

#create lists that'll become the x and y values for the scatter plot
averages = []
temps = []

#iterate through the merged data frame, averaging the different group's times through
#the years and storing the data, along with the temperature in lists
for year in year_list:
	for group in group_list:
		temp_df = merged_df[(merged_df.meet_id == 'vhsl' + group + year)]
		averages.append(temp_df['finish_time'].mean(axis = 0))
		temps.append(temp_df['mean_temp'].iloc[0])

#Call the summary Stats
summary_stats(averages)
summary_stats(temps)

#make the plot
plt.plot(temps, averages, 'ro')

#make a title
plt.title("Temperature and Average finish times")
plt.ylabel("Average Finish Time (in seconds)")
plt.xlabel("Mean Day temperature")
plt.show()





