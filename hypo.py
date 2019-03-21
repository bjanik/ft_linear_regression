#!/usr/bin/python3
import numpy as np
import sys
from regression import predict_price
from utils import *


def main():
	theta = [0.0, 0.0]
	try:
		theta[0] = float(input("Please enter value for theta0 as output of regression program: "))
		theta[1] = float(input("Please enter value for theta1 as output of regression program: "))
		mileage = float(input("Please enter a mileage: "))
	except ValueError:
		output_error_exit("Inputs must be an int or a float")
	if mileage < 0:
		output_error_exit("Sorry, mileage cannot be negative")
	price = predict_price(mileage, theta)
	if price < 0:
		price = 0
	print("Estimated car price is {} $".format(round(price)))

if __name__ == '__main__':
	try:
		main()
	except (EOFError, KeyboardInterrupt):
		sys.exit(130)