# shark-1.py - 06/10/2025. Practicing concepts from Part I, Section 3.
# Grouping, aggregation, applying functions to fields, etc. Neat stuff!

import pandas as pd

def fahrenheit_to_celsius(temperature: int | float) -> float:
    return (temperature - 32) / 1.8

if __name__ == "__main__":
    in_file = ".\\data\\shark-stew.txt"

    data = pd.read_csv(
        filepath_or_buffer=in_file,
        na_values=[-9999],
        sep=r"\s+", # The delimiter is multiple spaces.
        skiprows=[1],
        usecols=[
            "STATION",
            "DATE",
            "TMAX"
        ]
    )

    new_names = {
        "STATION": "STATION_ID",
        "TMAX": "TMAX_F"
    }

    data = data.rename(
        columns=new_names
    )

    # This function works as well, although .apply() is apparently
    # more efficient. That's something worth digging into.
    # data["TMAX_C"] = fahrenheit_to_celsius(data["TMAX_F"])
    data["TMAX_C"] = data["TMAX_F"].apply(fahrenheit_to_celsius)

    data["DATE_STR"] = data["DATE"].astype(str)
    data["YEAR_MONTH"] = data["DATE_STR"].str.slice(
        start=0, # Inclusive start.
        stop=6   # Exclusive end.
    )

    month_groups = data.groupby(by="YEAR_MONTH")

    print("UNIQUE YEAR_MONTH GROUPS:")
    print(f"{month_groups.nunique()}\n")

    print("2005/12 RECORDS:")
    print(f"{month_groups.get_group("200512")}\n")

    # Get each group, find the mean values of the given columns, then 
    # create a dataframe displaying these values.
    mean_columns = ["TMAX_F", "TMAX_C"]
    monthly_data = data.groupby(by="YEAR_MONTH")[mean_columns] \
        .mean() \
        .reset_index()
    
    print("MEAN TMAX_F FOR EACH GROUP:")
    print(f"{monthly_data}\n")