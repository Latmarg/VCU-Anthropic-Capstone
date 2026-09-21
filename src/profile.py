import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("data/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv")
percap = df[(df["geography"] == "country") & (df["variable"] == "usage_per_capita_index")]
percap2 = df[(df["geography"] == "country") & (df["variable"] == "augmentation_pct")]
percap3 = df[(df["geography"] == "country") & (df["variable"] == "automation_pct")]
percap4 = df[(df["geography"] == "country") & (df["variable"] == "usage_pct")]
percap5 = df[(df["geography"] == "country") & (df["variable"] == "gdp_per_working_age_capita")]

plt.hist(percap["value"])  
plt.title("Distribution of per-capita usage index (countries)")
plt.xlabel("usage_per_capita_index")
plt.ylabel("Number of countries")
plt.savefig("figures/percap_index.png") 
plt.clf()

plt.hist(percap2["value"])  
plt.title("Distribution of augmentation percent(countries)")
plt.xlabel("augmentation_pct")
plt.ylabel("Number of countries")
plt.savefig("figures/augmentation_pct.png") 
plt.clf()

plt.hist(percap3["value"])  
plt.title("Distribution of automation percent(countries)")
plt.xlabel("automation_pct")
plt.ylabel("Number of countries")
plt.savefig("figures/automation_pct.png") 
plt.clf()

plt.hist(percap4["value"])  
plt.title("Distribution of country usage by percent(countries)")
plt.xlabel("usage_pct")
plt.ylabel("Number of countries")
plt.savefig("figures/usage_pct.png") 
plt.clf()

plt.hist(percap5["value"])  
plt.title("Distribution of country gdp per working age(countries)")
plt.xlabel("gdp_per_working_age_capita")
plt.ylabel("Number of countries")
plt.savefig("figures/gdp_per_capita.png") 
plt.clf()


#usage count, usage percent, and usage per capita.

