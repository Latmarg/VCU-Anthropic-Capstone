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