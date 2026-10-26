import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("data/merged_final.csv")
to_label = ["United States", "Niger", "Australia", "Brazil", "Uganda", "Botswana"]

plt.scatter(df["internet"], df["usage_per_capita"])
for i, row in df.iterrows():
    if row["geo_name"] in to_label:
        plt.annotate(row["geo_name"],
                     (row["internet"], row["usage_per_capita"]),
                     xytext=(5, 5), textcoords="offset points",
                     fontsize=8)
highlight = df[df["geo_name"].isin(to_label)]
plt.scatter(highlight["internet"], highlight["usage_per_capita"], color="red", zorder=5)
plt.xlabel("Internet Use of Countries: % of Population")
plt.ylabel("AI usage per capita")
plt.title("Internet Access of Countries vs AI Usage per capita ")
plt.savefig("figures/usage_vs_internet.png")
plt.clf()



plt.scatter(df["dispersion"], df["usage_per_capita"])
for i, row in df.iterrows():
    if row["geo_name"] in to_label:
        plt.annotate(row["geo_name"],
                     (row["dispersion"], row["usage_per_capita"]),
                     xytext=(5, 5), textcoords="offset points",
                     fontsize=8)
highlight = df[df["geo_name"].isin(to_label)]
plt.scatter(highlight["dispersion"], highlight["usage_per_capita"], color="red", zorder=5)
plt.xlabel("Dispersion of Monthly Earnings")
plt.ylabel("AI usage per capita")
plt.title("Dispersion of Monthly Earnings vs AI Usage per capita")
plt.savefig("figures/usage_vs_dispersion.png")
plt.clf()



plt.scatter(df["dispersion"], df["internet"])
for i, row in df.iterrows():
    if row["geo_name"] in to_label:
        plt.annotate(row["geo_name"],
                     (row["dispersion"], row["internet"]),
                     xytext=(5, 5), textcoords="offset points",
                     fontsize=8)
highlight = df[df["geo_name"].isin(to_label)]
plt.scatter(highlight["dispersion"], highlight["internet"], color="red", zorder=5)
plt.xlabel("Dispersion of Monthly Earnings")
plt.ylabel("Internet Use of Countries: % of Population")
plt.title("Dispersion of Monthly Earnings vs Internet Access of Countries")
plt.savefig("figures/internet_vs_dispersion.png")
plt.clf()
