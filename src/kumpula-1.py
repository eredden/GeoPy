# kumpula-1.py - 06/09/2025. Practicing concepts from Part I, Section 3.
# Imports Kumpula's weather data from a CSV file, normalizes the dates,
# saves that data to another CSV file, and shows stats about the data.

import pandas as pd

if __name__ == "__main__":
    in_file = ".\\data\\kumpula-20250502-20250602.csv"
    out_file = ".\\data\\kumpula-modified-20250502-20250602.csv"

    raw = pd.read_csv(
        filepath_or_buffer=in_file,
        usecols=[
            "Year",
            "Month",
            "Day",
            "Maximum temperature [°C]",
            "Minimum temperature [°C]"
        ]
    )

    data = raw.rename(
        columns={
            "Year": "YEAR",
            "Month": "MONTH",
            "Day": "DAY",
            "Maximum temperature [°C]": "MAX", 
            "Minimum temperature [°C]": "MIN"
        }
    )
    
    dates = pd.to_datetime(
        arg=data[["YEAR", "MONTH", "DAY"]]
    )

    data.insert(
        loc=0, 
        column="DATE", 
        value=dates
    )

    data = data.drop(
        columns=["YEAR", "MONTH", "DAY"]
    )

    data.to_csv(
        path_or_buf=out_file, 
        index=False, # If this is not included, generated indexes will appear.
        sep=","
    )

    # Every operation below this comment displays data and does not modify it.
    print(f"DATAFRAME LENGTH: {len(data)}")
    print(f"DATAFRAME SHAPE: {data.shape}")
    print("DATAFRAME DATA TYPES:")
    print(f"{data.dtypes}\n")

    print("DATAFRAME CONTENTS (FIRST 5 ROWS):")
    print(data.head(5))
    print("")

    # Note how a list containing a list must be used to get the contents of
    # two columns. For one column, you can do data["COL_NAME"] to address it.
    print("DATAFRAME CONTENTS (FIRST 5 ROWS, MAX AND MIN ONLY):")
    print(data[["MAX", "MIN"]].head(5))
    print("")

    print("DATAFRAME DESCRIPTION (MAX AND MIN ONLY):")
    print(data[["MAX", "MIN"]].describe())
    print("")

    print(f"DATAFRAME MEAN OF THE MAX COLUMN: {data["MAX"].mean()}")
    print(f"DATAFRAME MEAN OF THE MIN COLUMN: {data["MIN"].mean()}")