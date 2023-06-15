import csv
from datetime import datetime

run = True
distance = 0.0

def generateDirectionCSV(ser):

    baud = 115200  # arduino uno runs at 115200 baud

    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    fileName = "DirectionData_" + formatted_datetime + ".csv" # name of the CSV file generated

    print_labels = False
    line = 2  # start at 0 because our header is 0 (not real data)
    sensor_data = []  # store data

    file = open(fileName, "w")
    print("Created file")

    # display the data to the terminal
    getData = ser.readline()
    dataString = getData.decode('utf-8')
    data = dataString.strip()
    readings = data.split(",")
    sensor_data.append(readings)

    # collect the samples
    while run:
        try:
            getData = ser.readline()
            dataString = getData.decode('utf-8')
            data = dataString[0:][:-2]
        except:
            continue

        readings = data.split(",")

        readings.append(distance)
        print(readings)

        sensor_data.append(readings)

    # create the CSV
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data[5:-1])

    print("Data collection complete!")
    file.close()