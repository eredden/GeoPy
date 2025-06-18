# vector-2.py - 06/18/2025. Working with geopandas for the first time!

import geopandas as gpd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    in_file = "./data/dc-grocery-stores.geojson"
    out_file = "./data/dc-grocery-stores-modified.geojson"

    # Note how read_file() does not need to be given a parameter to denote what 
    # type of file it reads -- it figures this out by itself. We use GeoJSON 
    # in this particular case.
    data = gpd.read_file(
        filename=in_file,
        columns=["STORENAME", "ADDRESS", "ZIPCODE", "geometry"],
        # A GeoJSON file can contain multiple "layers" of geospatial data.
        # Since there is only one in our sample file, this isn't really needed.
        layer="Grocery_Store_Locations" 
    )

    # Note how show() must be called from pyplot, not from the Axes instance.
    # The geometry is plotted using the geopandas plot() function, and color
    # coded by ZIPCODE using the column attribute.
    data.plot(
        column="ZIPCODE",
        legend=True
    )

    plt.show()

    data.to_file(
        filename=out_file,
        # This isn't strictly necessary as geopandas can infer this based off 
        # the file name.
        driver="GeoJSON"
    )