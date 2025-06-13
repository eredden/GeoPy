# shark-2.py - 06/13/2025. Practicing concepts from Part I, Section 4.
# We are reusing the original shark-1.py and plotting its data!

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def fahrenheit_to_celsius(temperature: int | float) -> float:
    return (temperature - 32) / 1.8

if __name__ == "__main__":
    in_file = ".\\data\\shark-stew.txt"

    data = pd.read_csv(
        filepath_or_buffer=in_file,
        na_values=[-9999],
        parse_dates=["DATE"], # This can be used to convert UNIX timestamps too!
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
        stop=7   # Exclusive end.
    )

    # Plotting the offset between the Fahrenheit and Celsius temperatures
    # and rendering that to the user using the show() function.
    data = data.set_index("DATE")
    temperatures = data[["TMAX_F", "TMAX_C"]]

    start_date = datetime(2005, 11, 15)
    end_date = datetime(2005, 12, 15)

    temperatures.plot(
        # kind="area", YOU CAN CHANGE THE TYPE OF GRAPH! Lines by default.
        linestyle="none", # Omit lines between data points.
        style=["ro", "bo"], # Red and blue lines, circle data points.
        title="Fahrenheit/Celsius Offset by Day",
        xlabel="Day",
        xlim=(start_date, end_date), # Results only shown between these dates.
        ylabel="Temperature"
    )
    plt.show()