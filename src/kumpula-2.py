# kumpula-2.py - 06/09/2025. Practicing concepts from Part I, Section 3.
# Uses existing Kumpula weather data to calculate new values!

import pandas as pd

if __name__ == "__main__":
    in_file = ".\\data\\kumpula-modified-20250502-20250602.csv"

    data = pd.read_csv(
        filepath_or_buffer=in_file
    )

    # Creating the DIFF column with the default value 0.0, then calculating
    # the DIFF value for each row based on MAX and MIN values in the same row.
    data["DIFF"] = 0.0
    data["DIFF"] = data["MAX"] - data["MIN"]

    print("DATAFRAME (FIRST 5 ROWS, ALL FIELDS):")
    print(f"{ data.head(5) }\n")

    # The loc property can be used to get a subset of the dataframe!
    # Note that the range operator is inclusive on both ends -- rows 0 to 5!
    # This is because we are working with axis indices rather than ranges.
    print("DATAFRAME (FIRST 5 ROWS, DIFF ONLY):")
    print(f"{ data.loc[0:5, "DIFF"] }\n")

    # You can also get multiple columns with the loc property.
    print("DATAFRAME (FIRST 5 ROWS, MAX AND MIN ONLY):")
    print(f"{ data.loc[0:5, ["MAX", "MIN"]] }\n")

    # You can also use conditional statements inside of the loc! If you wanted 
    # to chain them together, logical operators & and | can be used.
    max_mask = data["MAX"] > 15.0
    min_mask = data["MIN"] < 5.0
    masked_data = data.loc[max_mask & min_mask]

    # Regenerates indexes. This also turns the masked_data dataframe into an 
    # independent dataframe rather than a view of the "data" dataframe.
    # This is important if you intend on modifying data inside of it.
    # Using .copy() can create an independent dataframe as well. Modifying 
    # data in a view changes the parent dataframe as well.
    masked_data = masked_data.reset_index(drop=True)

    print("DATAFRAME (WHERE MAX > 15 AND MIN < 5):")
    print(f"{ masked_data }\n")

    # You can convert the data types as well! Float to integer conversion below.
    int_data = data.copy()
    columns = ["MAX", "MIN", "DIFF"]
    int_data[columns] = int_data[columns].round(0).astype(int)

    print("DATAFRAME (FIRST 5 ROWS, FIELDS AS INTEGERS):")
    print(f"{ int_data.head(5) }\n")

    # The sort_values() function can be used to... sort values! Who'da guessed?
    # Note how the function arguments can be lists. Adding extra values to the 
    # lists allows for you to sort on multiple conditions in succession.
    sorted_data = data.sort_values(
        by=["DIFF"], 
        ascending=[False]
    )

    print("DATAFRAME (FIRST 5 ROWS, SORTED BY DIFF):")
    print(f"{ sorted_data.head(5) }\n")