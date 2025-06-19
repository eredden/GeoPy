# vector-3.py - 06/19/2025. Working with common geometric operations.

import geopandas as gpd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    in_file = "./data/tigerline-2024-us-aiannh.zip"
    out_file = "./data/tigerline-2024-us-aiannh-water.geojson"

    data = gpd.read_file(
        filename=in_file,
        columns=["NAME", "AWATER", "GEOMETRY"]
    )

    # We set the coordinate reference system here.
    # https://spatialreference.org/ref/epsg/9311/
    print(f"OLD CRS: {data.crs}")
    data = data.to_crs(epsg=9311)
    print(f"NEW CRS: {data.crs}")

    # We get the centroid of each polygon and set that as the geometry to plot 
    # rather than using the polygons and multipolygons. Looks nicer on the plot!
    # data["CENTROID"] = data.geometry.centroid
    # data = data.set_geometry("CENTROID")

    # Color-code plotted territories by name, then display them.
    data.plot(
        column="NAME"
    )
    plt.axis("off")
    plt.show()

    # Dissolve (split apart data into groups) by whether they have water or not.
    water_data = data.copy()
    water_data["HASWATER"] = False
    water_data.loc[water_data["AWATER"] > 0, "HASWATER"] = True

    dissolved = water_data.dissolve(
        by="HASWATER",
        aggfunc="sum"
    )

    dissolved = dissolved.reset_index()

    dissolved.plot(
        column="HASWATER",
        legend=True
    )
    plt.axis("off")
    plt.show()

    print(water_data["HASWATER"].value_counts())
    print(dissolved)

    # Find the minimum-sized box to envelope all territories. Either function 
    # works, but the bounding box method gives a WKT formatted polygon while 
    # the total bounds attribute only gives the corner values.
    # data.bounds() can be used to get the boundaries of a given series.
    bounding_box = data.union_all().envelope
    convex_hull = data.union_all().convex_hull

    print(f"BOUNDING BOX: \n{bounding_box}\n")
    print(f"TOTAL BOUNDS: \n{data.total_bounds}\n")
    print(f"CONVEX HULL: \n{convex_hull}\n")

    # Write the results to a file.
    water_data.to_file(
        filename=out_file
    )