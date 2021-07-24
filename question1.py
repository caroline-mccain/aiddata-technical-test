# https://docs.python.org/3/library/math.html
import math
# https://docs.python.org/3/library/os.html
import os

# create arrays to hold the points
a_points = []
b_points = []

# hard-coded file paths
# file_path_a = "C:\\Users\\carol\\Desktop\\Sophomore Year\\TechnicalTest\\TechnicalTest\\Question1\\a.csv"
# file_path_b = "C:\\Users\\carol\\Desktop\\Sophomore Year\\TechnicalTest\\TechnicalTest\\Question1\\b.csv"

# relative file paths
cur_wd = os.getcwd()
file_path_a = os.path.join(cur_wd, "Question1\\a.csv")
file_path_b = os.path.join(cur_wd, "Question1\\b.csv")

# helper function that reads points from file
def points_from_file(file, array):
    # open the specified file
    with open (file, 'r') as file_r:
        # skip over the header line of the file
        file_r.readline()
        # read in each line in the file
        for line in file_r.readlines():
            # split the line at the commas
            point = line.split(',')
            # the x coordinate is in the first cell
            x = float(point[0]);
            # the y coordinate is in the second cell
            y = float(point[1]);
            # create a point array
            point_array = [x, y]
            # append this point to the specified points array
            array.append(point_array)

# read in point set a and point set b and populate their respective arrays
points_from_file(file_path_a, a_points)
points_from_file(file_path_b, b_points)

# helper function that calculates the distance between a and b
def distance_calc(a, b):
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]),2))

# holds the current minimun distance
min_dist = float('inf')
# holds the points that give the current minimun distance
min_dist_points = ["a","b"]

# holds the current maximum distance
max_dist = 0.0
# holds the points that give the current maximum distance
max_dist_points = ["a","b"]

# traverse through all of the a points
for p_a in a_points:
    # traverse through all of the b points
    for p_b in b_points:
        # calculate the distance between the current pair of points
        dist = distance_calc(p_a, p_b)
        # compare the calculated distance to the current minimum
        if (dist < min_dist):
            # if this pair yields a smaller distance, store that distance and these points
            min_dist = dist
            min_dist_points[0] = p_a
            min_dist_points[1] = p_b
        # compare the calculated distance to the current maximum
        if (dist > max_dist):
            # if this pair yields a greater distance, store that distance and these points
            max_dist = dist
            max_dist_points[0] = p_a
            max_dist_points[1] = p_b

# print results
print("Minimun Distance (Closest Together): " + str(min_dist_points))
print("Maximum Distance (Farthest Apart): " + str(max_dist_points))
