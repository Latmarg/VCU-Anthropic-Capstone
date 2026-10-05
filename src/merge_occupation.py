import pandas

isco = pandas.read_csv("data/EAR_EMTA_SEX_OCU_CUR_NB_A-20261005T1454.csv")
print(isco.columns)
print(len(isco))

#Removing columns that arent needed
isco_small = isco[(isco["sex.label"] == "Total") & (isco["classif2.label"] == "Currency: U.S. dollars")]
print(len(isco_small))


tiers = [ 
    "Occupation (Skill level): Skill levels 3 and 4 ~ high",
    "Occupation (Skill level): Skill level 1 ~ low"
]

isco_tiers = isco_small[isco_small["classif1.label"].isin(tiers)]
print(len(isco_tiers))
print(isco_tiers["classif1.label"].value_counts())

#Finding each country's most recent year
latest_year = isco_tiers.groupby("ref_area.label")["time"].transform("max")
isco_recent = isco_tiers[isco_tiers["time"] == latest_year]
print(len(isco_recent))
print(isco_recent["ref_area.label"].nunique())

wide = isco_recent.pivot_table(
    index = "ref_area.label",
    columns = "classif1.label",
    values = "obs_value"
)
print(wide.head)
print(len(wide))

wide["dispersion"] = (
    wide["Occupation (Skill level): Skill levels 3 and 4 ~ high"]
    / wide["Occupation (Skill level): Skill level 1 ~ low"]
)
print(wide[["dispersion"]].head(10))
print(wide["dispersion"].notna().sum())

disp = wide[["dispersion"]].reset_index()
print(disp.head())

#Importing Anthropic dataset
anthropic = pandas.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")
bridge = anthropic[anthropic["geography"] == "country"][["geo_id", "geo_name"]].drop_duplicates()

#Joining wage data and bridge
disp_join = disp.merge(bridge, left_on = "ref_area.label", right_on = "geo_name", how = "left")

print("Total wage rows:", len(disp_join))
print("Got a geo_id:", disp_join["geo_id"].notna().sum())
print()
print("UNMATCHED names:")
print(disp_join[disp_join["geo_id"].isna()]["ref_area.label"].tolist)

#Fixing names of Unmatched countries
name_fixes = {
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "Republic of Korea": "South Korea",
    "Viet Nam": "Vietnam",
    "Türkiye": "Turkey",
    "Bolivia, Plurinational State of": "Bolivia",
    "Lao People's Democratic Republic": "Laos",
    "Tanzania, United Republic of": "Tanzania",
    "Côte d'Ivoire": "Ivory Coast",
    "Republic of Moldova": "Moldova",
    "Netherlands": "The Netherlands",
    "Cape Verde": "Cabo Verde",
    "Brunei Darussalam": "Brunei",
    "Timor-Leste": "Timor Leste",
    "Congo": "Republic of the Congo"
}


#Applying the name fixes to the dataset
disp["ref_area.label"] = disp["ref_area.label"].replace(name_fixes)

disp_join = disp.merge(bridge, left_on = "ref_area.label", right_on = "geo_name", how = "left")
print("Got a geo_id:", disp_join["geo_id"].notna().sum())
print("Still unmatched:", disp_join[disp_join["geo_id"].isna()]["ref_area.label"].tolist())

#Final merge
disp_final = disp_join[disp_join["geo_id"].notna()][["geo_id", "dispersion"]]
print(len(disp_final))
print(disp_final["dispersion"].notna().sum())

#importing internet merged data
merged = pandas.read_csv("data/merged_adoption_internet.csv")

final = merged.merge(disp_final, on = "geo_id", how = "inner")
print("Final Sample:", len(final))
print("Complete rows (all three vars):", final.dropna(subset=["2024", "dispersion"]).shape[0])

final.to_csv("data/merged_occupation_internet.csv", index = False)