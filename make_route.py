"""
CIS 422 
Project 1

The arithmetic for making the route

The result will show the detialed route for started place to ended place.
For exampl: 
	0.0km Start at 19th and Agate
	1.2km Left on Franklin Blvd
	1.4km Left on 11th Ave
"""
import math

"""
Cite from https://blog.csdn.net/qq_37742059/article/details/101554565
"""
earth_radius = 6370.856  
math_2pi = math.pi * 2
pis_per_degree = math_2pi / 360  
 
def lat_degree2km(dif_degree=.0001, radius=earth_radius):

    return radius * dif_degree * pis_per_degree
 
 
def lat_km2degree(dis_km=111, radius=earth_radius):
   
    return dis_km / radius / pis_per_degree
 
 
def lng_degree2km(dif_degree=.0001, center_lat=22):
   
    real_radius = earth_radius * math.cos(center_lat * pis_per_degree)
    return lat_degree2km(dif_degree, real_radius)
 
 
def lng_km2degree(dis_km=1, center_lat=22):
    
    real_radius = earth_radius * math.cos(center_lat * pis_per_degree)
    return lat_km2degree(dis_km, real_radius)
 
 
def ab_distance(a_lat, a_lng, b_lat, b_lng):
    
    center_lat = .5 * a_lat + .5 * b_lat
    lat_dis = lat_degree2km(abs(a_lat - b_lat))
    lng_dis = lng_degree2km(abs(a_lng - b_lng), center_lat)
    return math.sqrt(lat_dis ** 2 + lng_dis ** 2)


class Route():
    """ This class is used to store the result of the route """

    def __init__(self, roadname):
        self.times = 1
        self.turn = ["Start at"]
        self.distance = [0]
        self.road = [roadname]


class Points():
    """ This class is used to store the points between start and end """

    def __init__(self):
        self.amount = 0
        self.lat = []
        self.lon = []
        self.roadname = []
        self.turnpoints = []
        self.num_tp = 0

    def add_newpoint(self, lat, lon, roadname):
        self.amount += 1
        self.lat.append(lat)
        self.lon.append(lon)
        self.roadname.append(roadname)

    def add_turnpoint(self, p):
        self.turnpoints.append(p)
        self.num_tp += 1

    def show_p(self):
        for i in range(self.amount):
            print(self.lat[i])
            print(self.lon[i])
            print(self.roadname[i])
    
    def show_tp(self):
        for i in range(self.num_tp):
            print(self.turnpoints[i])


def find_turnpoints(head, tail, Points):
    if Points.roadname[head] != Points.roadname[tail]:
        if head+1 != tail:
            midpoint = (head + tail) // 2
            if (head+1 == midpoint):
                if Points.roadname[head] != Points.roadname[midpoint]:
                    Points.add_turnpoint(midpoint)
                    find_turnpoints(midpoint, tail, Points)
                else:
                    find_turnpoints(midpoint, tail, Points)
            else:
                if Points.roadname[head] != Points.roadname[midpoint]:
                    find_turnpoints(head, midpoint, Points)
                    find_turnpoints(midpoint, tail, Points)
                else:
                    find_turnpoints(midpoint, tail, Points)
        else:
            Points.add_turnpoint(tail)



#"""
if __name__ == '__main__':
    # eg:深圳一点到北京一点的直线距离，比较符合百度地图测距结果
    print(ab_distance(22.522850036621094, 113.93990325927734, 39.90303039550781, 116.40496063232422))
    print(ab_distance(44.0584707554669, -123.057163779429, 44.045509, -123.069740812934))
    print(ab_distance(44.587662, -123.256691, 44.587616, -123.256927))

    p = Points()
    p.add_newpoint(1,1,"a")
    p.add_newpoint(2,2,"a")
    p.add_newpoint(3,3,"a")
    p.add_newpoint(4,4,"b")
    p.add_newpoint(5,5,"b")
    p.add_newpoint(6,6,"c")
    p.add_newpoint(7,7,"c")
    p.add_newpoint(8,8,"c")
    p.add_newpoint(9,9,"d")
    p.add_newpoint(10,10,"e")
    find_turnpoints(0, p.amount-1, p)
    p.show_tp()
#"""
