# Day 15 part 2
# Takes quite a while to run, but it works
from common.common import parse_input_into_list_of_strings
import re

lines = parse_input_into_list_of_strings("input.txt")
sensors = []
relative_beacons = []

for l in lines:
    groups = re.search('Sensor at x=([0-9]+), y=([0-9]+): closest beacon is at x=([0-9\\-]+), y=([0-9\\-]+)', l)
    sensors.append([int(groups.group(1)), int(groups.group(2))])
    relative_beacons.append([int(groups.group(3)), int(groups.group(4))])

actual_beacons = []
sensor_radii = []

for i in range(len(sensors)):
    if relative_beacons[i] not in actual_beacons:
        actual_beacons.append(relative_beacons[i])

    sensor_radii.append(abs(sensors[i][0] - relative_beacons[i][0]) + abs(sensors[i][1] - relative_beacons[i][1]))

ans = 0

for y_limit in range(4000001):
    sensor_areas = []
    for i in range(len(sensors)):
        if sensors[i][1] - sensor_radii[i] <= y_limit <= sensors[i][1] + sensor_radii[i]:
            a = abs(sensors[i][1] - y_limit)
            extra = sensor_radii[i] - a

            if sensors[i][0] - extra < 0:
                b = 0
            else:
                b = sensors[i][0] - extra
            if sensors[i][0] + extra > 4000000:
                t = 4000000
            else:
                t = sensors[i][0] + extra
            s = [b, t]

            sensor_areas.append(s)

    sorted_ranges = sorted(sensor_areas, key=lambda x: x[0])

    current_range = [sorted_ranges[0][0], sorted_ranges[0][1]]
    areas_of_2m = []
    for i in range(len(sorted_ranges) - 1):
        if sorted_ranges[i + 1][0] <= current_range[1]:
            if sorted_ranges[i + 1][1] > current_range[1]:
                current_range[1] = sorted_ranges[i + 1][1]
        else:
            areas_of_2m.append(current_range.copy())
            current_range = [sorted_ranges[i + 1][0], sorted_ranges[i + 1][1]]

    areas_of_2m.append(current_range)

    count = 0
    for elt in areas_of_2m:
        count += abs(elt[1] - elt[0])

    if count < 4000000:
        ans = areas_of_2m[0][1] + 1
        print(ans, y_limit)
        print(ans * 4000000 + y_limit)
        break
