'''
The Robot Tour Optimization is a version of the Traveling Salesman Problem (TSP).

The TSP is commonly described as follows:

"A salesman must visit a list of cities located on a map. He must visit every city during a single sales trip
and he must do so in the most efficient way possible (shortest total distance). All of the pairwise distances between cities are known ahead of time. Find an algorithm to calculate the shortest cycle which visits each city one time."

The problem input is a set S of n point on a plane. 
The desired algorithm solves the TSP by outputting the shortest cycle tour that visits each point in the set S.

The TSP is known to be an NP-hard problem. 
'''

#input data is in the form of sets of floating point (x,y) tuples which identify a point on the two dimensional plane.

#Points lie in a path that is roughly circular. This is a good instance for the nearest-neighbor heuristic.
circular_example = set([(5.0, 0.0), (3.0, 3.0), (0.0, 5.0), (-3.0, 3.0), (-5.0, 0.0), (-3.0, -3.0), (0.0, -5.0), (3.0, -3.0)])

def nearest_neighbor(point_set):
	#Put all the points from the set into a list.
	unvisited_points = [pt for pt in point_set]
	result_path = []
	
	#Pick an abitrary initial point.
	p0 = unvisited_points.pop(0)
	result_path.append(p0)
	
	#While there are unvisited points, select the next point to visit.
	while len(unvisited_points) > 0:
		pt_i = find_closest(result_path[-1], unvisited_points)
		print pt_i, unvisited_points
		result_path.append(unvisited_points.pop(unvisited_points.index(pt_i)))
		print result_path
		
	return result_path

		
def find_closest(start_point, point_list):
	#Find the point from point list that is the closest point to the start point.
	min_dist = float('inf')
	closest_point = None
	
	for pt in point_list:
		current_dist = distance(start_point, pt)
		if current_dist < min_dist:
			closest_point = pt
			min_dist = current_dist
			
	return closest_point

def distance(a, b):
	from math import sqrt
	#Finds the distance between two points a & b on the x, y coordinate plane.
	print a, b
	xx = b[0]-a[0]
	yy = b[1]-a[1]
	return sqrt(xx**2 + yy**2)