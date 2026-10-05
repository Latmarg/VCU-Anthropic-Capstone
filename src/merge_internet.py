import pandas

wb = pandas.read_csv("data/API_IT.NET.USER.ZS_DS2_en_csv_v2_442976.csv", skiprows = 4)
print(wb.columns)
print(len(wb))

#Checking to see if aggregate rows are included ex: Africa Western and Central
print(wb[["Country Name", "Country Code", "2024"]].head(10))

#Removing columns that are not needed
wb_small = wb[["Country Name", "Country Code", "2024"]]

wb_small = wb_small.rename(columns={"Country Code": "geo_id"})

print(wb_small.head())
print(len(wb_small))

#Importing anthropic dataset
anthropic = pandas.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")
countries = anthropic[anthropic["geography"] == "country"][["geo_id", "geo_name"]].drop_duplicates()
print(len(countries))

#merging the countries
merged = countries.merge(wb_small, on="geo_id", how = "inner")
print(len(merged))
print(merged.head())
print(merged["2024"].notna().sum())


#Listing the countries that have no data from 2024
print(merged[merged["2024"].isna()]["geo_name"].tolist())

merged.to_csv("data/merged_adoption_internet.csv", index = False)