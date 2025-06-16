# vector-1.py - 06/15/2025. Playing around with the geometric building blocks 
# of geospatial data analysis.

from shapely import LineString, Point, Polygon

if __name__ == "__main__":
    point = Point(2.2, 4.2)
    point3D = Point(9.26, -2.456, 0.57)
    point3D_coords = list(point3D.coords)

    # WKT stands for Well Known Text, which is a format for representing
    # vector geometry objects. Defined by the Open Geospatial Consortium (OGC).
    print("POINT:")
    print(f"WKT representation: {point3D.wkt}")
    print(f"Coordinates: {point3D_coords}\n")

    # You can also supply Point objects instead of tuples here. I was lazy!
    line = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
    line_coords = list(line.coords)

    print("LINESTRING:")
    print(f"WKT representation: {line}")
    print(f"Coordinates: {line_coords}")
    print(f"Length: {line.length}")
    print(f"Centroid: {line.centroid}\n") # Center of the line! A point object.

    # Note how the start and end of the polygon must both be defined, despite 
    # the fact that they are exactly the same. Also note that a second array 
    # of tuples can be passed in to represent holes in the polygon.
    exterior = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456), (2.2, 4.2)]
    # Multiple brackets/parentheses for multiple holes.
    hole_coords = [[(4.0, 1.5), (5.0, -9.0), (6.0, -4.0), (4.0, 1.5)]] 

    poly = Polygon(
        shell=exterior, 
        holes=hole_coords
    )

    print("POLYGON:")
    # Note how double parentheses enclose the points of the polygon. This is
    # also related to the holes issue from before.
    print(f"WKT representation: {poly.wkt}")
    print(f"Area: {poly.area}")
    print(f"Centroid: {poly.centroid}")
    print(f"Exterior: {poly.exterior}")
    print(f"Exterior Length: {poly.exterior.length}\n")

    # MultiPoints, MultiLineStrings, and MultiPolygons are all instantiated
    # the same way and just show multiple of the objects above at the same time.