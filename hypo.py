import numpy as np
import sys
from regression import predict_price

# def predict_price(theta, mileage):
	# return theta[0] + theta[1] * mileage

def main():
	theta = [0.00008134, 0.045279]
	try:
		mileage = float(input("Please enter a mileage: "))
		print("Estimated price is {} $".format(theta[0] + theta[1] * mileage))
	except (EOFError, KeyboardInterrupt):
		sys.exit(130)
	except ValueError:
		print("Mileage must be an int or a float", file=sys.stderr)

if __name__ == '__main__':
	main()