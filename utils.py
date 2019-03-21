import sys

def output_error_exit(message):
	print(message, file=sys.stderr)
	sys.exit(1)

def predict_price(mileage, theta):
	return theta[0] + theta[1] * mileage