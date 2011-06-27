import math


nautical_mile_per_lat = 60.00721
nautical_mile_per_longitude = 60.10793
rad = math.pi / 180.0
meters_per_nautical_mile = 1852

def distance_between_coordinates_meters(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two latitude and longitude coordinates
    in meters.
    Taken from http://www.geesblog.com/2009/01/calculating-distance-between-latitude-longitude-pairs-in-python/
    """
    y_distance = (lat2 - lat1) * nautical_mile_per_lat
    x_distance = (math.cos(lat1 * rad) + math.cos(lat2 * rad)) * (lon2 - lon1) * (nautical_mile_per_longitude / 2)
    distance = math.sqrt(y_distance**2 + x_distance**2)
    return distance * meters_per_nautical_mile

