import numpy as np

# Task 1: Load the data file to create a NumPy array
brfss_data = np.genfromtxt('brfss-cdc.csv', delimiter=',', skip_header=1)

# Task 2: Display the first five rows and shape of the array
print("First Five Rows of the Data:")
print(brfss_data[:5])
print("Shape of the data:", brfss_data.shape)

# Task 3: Calculate weight change
weight_change = brfss_data[:, 2] - brfss_data[:, 3]

# Task 4: Calculate descriptive statistics for weight change
mean_weight_change = np.mean(weight_change)
median_weight_change = np.median(weight_change)
std_dev_weight_change = np.std(weight_change)
quartiles = np.percentile(weight_change, [25, 75])
iqr_weight_change = quartiles[1] - quartiles[0]

print("\nDescriptive Statistics for Weight Change Data:")
print("Mean:", mean_weight_change)
print("Median:", median_weight_change)
print("Standard Deviation:", std_dev_weight_change)
print("Interquartile Range:", iqr_weight_change)

# Task 5: Concatenate weight change array with the main data array
brfss_data_with_change = np.concatenate((brfss_data, weight_change.reshape(-1, 1)), axis=1)

# Task 6: Display the first five rows and shape of the concatenated array
print("\nFirst Five Rows of the Data with Weight Changes:")
print(brfss_data_with_change[:5])
print("Shape of the data:", brfss_data_with_change.shape)

# Task 7: Split the concatenated array based on the gender column
males_data = brfss_data_with_change[brfss_data_with_change[:, 5] == 1]
females_data = brfss_data_with_change[brfss_data_with_change[:, 5] == 2]

# Task 8: Display the first five rows and shape of the array relevant to males data
print("\nFirst Five Rows of the Data relevant to Males:")
print(males_data[:5])
print("Shape of the data:", males_data.shape)

# Task 9: Calculate descriptive statistics for males data
mean_males = np.mean(males_data[:, 6])
median_males = np.median(males_data[:, 6])
std_dev_males = np.std(males_data[:, 6])
quartiles_males = np.percentile(males_data[:, 6], [25, 75])
iqr_males = quartiles_males[1] - quartiles_males[0]

print("\nDescriptive Statistics for Data relevant to Males:")
print("Mean:", mean_males)
print("Median:", median_males)
print("Standard Deviation:", std_dev_males)
print("Interquartile Range:", iqr_males)

# Task 10: Display the first five rows and shape of the array relevant to females data
print("\nFirst Five Rows of the Data relevant to Females:")
print(females_data[:5])
print("Shape of the data:", females_data.shape)

# Task 11: Calculate descriptive statistics for females data
mean_females = np.mean(females_data[:, 6])
median_females = np.median(females_data[:, 6])
std_dev_females = np.std(females_data[:, 6])
quartiles_females = np.percentile(females_data[:, 6], [25, 75])
iqr_females = quartiles_females[1] - quartiles_females[0]

print("\nDescriptive Statistics for Data relevant to Females:")
print("Mean:", mean_females)
print("Median:", median_females)
print("Standard Deviation:", std_dev_females)
print("Interquartile Range:", iqr_females)
