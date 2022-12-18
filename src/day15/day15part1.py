# Day 15 part 1
# Initially tried with sets etc. but way too costly
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

sensor_areas = []
for i in range(len(sensors)):
    if sensors[i][1] - sensor_radii[i] <= 2000000 <= sensors[i][1] + sensor_radii[i]:
        a = abs(sensors[i][1] - 2000000)
        extra = sensor_radii[i] - a

        s = [sensors[i][0] - extra, sensors[i][0] + extra]

        sensor_areas.append(s)


sorted_areas = sorted(sensor_areas, key=lambda x: x[0])

current_range = [sorted_areas[0][0], sorted_areas[0][1]]
areas_of_2m = []
for i in range(len(sorted_areas) - 1):
    if sorted_areas[i + 1][0] <= current_range[1]:
        if sorted_areas[i + 1][1] > current_range[1]:
            current_range[1] = sorted_areas[i + 1][1]
    else:
        areas_of_2m.append(current_range.copy())
        current_range = [sorted_areas[i + 1][0], sorted_areas[i + 1][1]]

areas_of_2m.append(current_range)


count = 0
for elt in areas_of_2m:
    count += abs(elt[1] - elt[0]) + 1

minus_sensors = len(list(filter(lambda x: x[1] == 2000000, sensors)))
minus_beacons = len(list(filter(lambda x: x[1] == 2000000, actual_beacons)))
print(count - minus_sensors - minus_beacons)
