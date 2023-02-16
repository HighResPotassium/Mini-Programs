data_str = []
data_flt = []

index = 0

summation_avg = 0
summation_stdev = 0

print("Please put in the data from your trial.\n","Press 'ENTER' to insert a new number, and 'q' to quit.")

while True:
    num = input(">> ")

    data_str.append(num)

    if num == "q":
        break

for i in range(0,(len(data_str) - 1)):

    val = data_str[i]
    data_flt.append(float(val))

length = len(data_flt)

for number in data_flt:
    summation_avg += number

avg = summation_avg/length

for number in data_flt:
    summation_stdev += (number - avg)**2

stdev = (1/length)*(summation_stdev)**(1/2)

print("The uncertainty in the data is", stdev)
