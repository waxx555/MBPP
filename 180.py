'''
Write a function to calculate distance between two points using latitude and longitude.
'''


from math import radians, sin, cos, acos
def distance_lat_long(slat,slon,elat,elon):
 dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
 return dist


assert distance_lat_long(23.5,67.5,25.5,69.5)==12179.372041317429
assert distance_lat_long(10.5,20.5,30.5,40.5)==6069.397933300514
assert distance_lat_long(10,20,30,40)==6783.751974994595
