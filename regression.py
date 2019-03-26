#!/usr/bin/python3
import numpy as np
import pandas
import matplotlib.pyplot as plt
import sys
import time

from utils import *

def get_data(argv):
	try:
		data = pandas.read_csv(sys.argv[1])
	except FileNotFoundError:
		output_error_exit("{}: No such file or directory".format(sys.argv[1]))
	except (pandas.errors.EmptyDataError, pandas.errors.ParserError, UnicodeDecodeError):
		output_error_exit("{}: File is not csv type".format(sys.argv[1]))
	except OSError:
		output_error_exit("Initializing from file failed")
	data_len = len(data)
	if data_len == 0:
		output_error_exit("File provides no information")
	return data, data_len

def fit(mileage, price, theta, m, alpha, num_iters):
	for i in range(num_iters):
		sigma0 = sum(predict_price(mileage, theta) - price)
		sigma1 = sum((predict_price(mileage, theta) - price) * mileage)
		theta[0] = theta[0] - alpha * sigma0 / m
		theta[1] = theta[1] - alpha * sigma1 / m
	return theta

def plot_regression(mileage, price, theta):
	axes = plt.gca()
	axes.set_xlim(0, 250000)
	axes.set_ylim(0, 10000)
	plt.xlabel("Mileage")
	plt.ylabel("Price")
	plt.gcf().canvas.set_window_title("Car price function of mileage")
	plt.scatter(mileage, price, c='r', marker='x')
	plt.plot(mileage, predict_price(mileage, theta), c='b')
	plt.show()

def retrieve_theta(theta, mileage):
	min_mileage = min(mileage)
	max_mileage = max(mileage)
	tmp_theta0 = theta[0]
	tmp_theta1 = theta[1]
	theta[0] = tmp_theta0 + theta[1] * ((min_mileage * -1) / (max_mileage - min_mileage))
	theta[1] = tmp_theta0 + tmp_theta1 * (1 - min_mileage) / (max_mileage - min_mileage) - theta[0]

def main():
	if len(sys.argv) < 2:
		output_error_exit("Missing input file")
	data, data_len = get_data(sys.argv)
	try:
		mileage = np.array(data['mileage'])
		price = np.array(data['price'])
		scaled_mileage = (mileage - min(mileage)) / (max(mileage) - min(mileage))
	except KeyError:
		output_error_exit("Keys should be named 'mileage' and 'price'")
	except TypeError:
		output_error_exit("Data in file is not only numeric")
	if np.isnan(mileage).any() or np.isnan(price).any():
		output_error_exit("Incomplete information")
	theta = np.zeros(2)
	theta = fit(scaled_mileage, price, theta, data_len, 1, 250)
	retrieve_theta(theta, mileage)
	print("Theta0 is {}\nTheta1 is {}".format(theta[0], theta[1]))
	try:
		plot_regression(mileage, price, theta)
	except KeyboardInterrupt:
		sys.exit(1)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(130)