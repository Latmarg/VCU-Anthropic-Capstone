import pandas

merged = pandas.read_csv("data/merged_occupation_internet.csv")
merged = merged.rename(columns={"2024": "internet"})
anthropic = pandas.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")

adoption = anthropic[(anthropic["geography"] == "country") &
                     (anthropic["variable"] == "usage_per_capita_index")][["geo_id", "value"]]
adoption = adoption.rename(columns={"value": "adoption"}).drop_duplicates("geo_id")

# Join adoption onto your existing merged table (the one with internet + dispersion)
final = merged.merge(adoption, on="geo_id", how="inner")

# keep only countries with all three variables present
final = final.dropna(subset=["adoption", "internet", "dispersion"])
print("Final countries with all three variables:", len(final))

final.to_csv("data/merged_final.csv", index=False)