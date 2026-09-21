import pandas
import glob

#Loop
files = glob.glob("data/*.csv")

for f in files:
    df = pandas.read_csv(f)
    print(f)
    #Columns
    print(df.columns)
    #Number of rows
    print(len(df))
    #Missing rates
    print(df.isna().mean() * 100)


df = pandas.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")

usage = df[(df["geography"] == "country") & (df["variable"] == "usage_pct")]
print(usage)

usage_sorted = usage.sort_values("value", ascending= False)
print(usage_sorted.head())

#Value of US comes to be 21.5% which is similar to the stated 21.6 in the article

percap = df[((df["geography"] == "country") & (df["variable"] == "usage_per_capita_index"))]
print(percap)

percap_sorted = percap.sort_values("value", ascending= False)
print(percap_sorted.head(10))

#Singapore is number 3 with a similar value of 4.57 to the 4.6, but Canada is not even in the top 10. 