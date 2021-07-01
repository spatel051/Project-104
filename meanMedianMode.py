import csv
from collections import Counter

with open('HeightWeight.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

def get_mean():
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][2]
        new_data.append(float(n_num))
    
    n = len(new_data)
    total = 0

    for x in new_data:
        total += x
    
    mean = total / n
    print("Mean (Average) is -> " + str(mean))

def get_median():
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][2]
        new_data.append(float(n_num))
    
    n = len(new_data)
    new_data.sort()

    if n % 2 == 0:
        median1 = float(new_data[n // 2])
        median2 = float(new_data[n // 2 - 1])
        median = (median1 + median2) / 2
    else:
        median = new_data[n // 2]
    
    print("Median is -> " + str(median))

def get_mode():
    new_data = []

    for i in range(len(file_data)):
        n_num = file_data[i][2]
        new_data.append(float(n_num))

    data = Counter(new_data)
    mode_data_for_range = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }

    for weight, occurance in data.items():
        if 75 < float(weight) < 85:
            mode_data_for_range["75-85"] += occurance
        elif 85 < float(weight) < 95:
            mode_data_for_range["85-95"] += occurance
        elif 95 < float(weight) < 105:
            mode_data_for_range["95-105"] += occurance
        elif 105 < float(weight) < 115:
            mode_data_for_range["105-115"] += occurance
        elif 115 < float(weight) < 125:
            mode_data_for_range["115-125"] += occurance
        elif 125 < float(weight) < 135:
            mode_data_for_range["125-135"] += occurance
        elif 135 < float(weight) < 145:
            mode_data_for_range["135-145"] += occurance
        elif 145 < float(weight) < 155:
            mode_data_for_range["145-155"] += occurance
        elif 155 < float(weight) < 165:
            mode_data_for_range["155-165"] += occurance
        elif 165 < float(weight) < 175:
            mode_data_for_range["165-175"] += occurance
    
    mode_range, mode_occurance = 0, 0

    for Range, occurance in mode_data_for_range.items():
        if occurance > mode_occurance:
            mode_range, mode_occurance = [int(Range.split("-")[0]), int(Range.split("-")[1])], occurance
    
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print("Mode is -> " + str(mode))

get_mean()
get_median()
get_mode()