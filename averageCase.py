def averageCase(size):
	result = 0
	for count in range(size):
		result += size / (size - count)
	return result

def main():
	for size in range(1, 101):
		print("size", size, "averages %.2f" % averageCase(size), "iterations or", size, " * %.2f" % (averageCase(size) / size))

main()