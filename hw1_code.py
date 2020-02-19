# Import the neccessary packages
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew

# Question 2
# Generate 1,000 standard normal distribution samples with mean equals 0 and variance equals 1 and store the samples in sample_data
mu, sigma = 0, 1
sample_data = np.random.normal(mu, sigma, 1000)

# Define a function data_estimators that returens the sample mean, standard deviation, skewness and kurtosis of the sample_data in a list
def data_estimators(dataset):
    sample_mean = np.mean(dataset)
    std = np.std(dataset)
    kur = kurtosis(dataset)
    sample_skew = skew(dataset)
    print([sample_mean, std, kur, sample_skew])
    
# Plot the histogram of the 1,000 samples generated and save the image
plt.hist(sample_data, 60, density = True)
plt.xlabel('X')
plt.title('Sample_data Histogram')
plt.savefig('D:\\Sample Distribution.png')
plt.show()

# Generate the sample statistics of sample_data
data_estimators(sample_data)