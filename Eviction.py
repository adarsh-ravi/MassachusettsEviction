import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
import plotly
import plotly.plotly as py
import plotly.figure_factory as ff

# Read the CSV File
df_Eviction = DataFrame(pd.read_csv("Massachusetts Evictions Data.csv"))

# Line Plot Poverty Rate & Percentage Renter Occupied in Massachusetts
years = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['year'].values
poverty_rate = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['poverty-rate'].values
pct_renter = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-renter-occupied'].values
plt.title("Poverty Rate & Percentage Renter Occupied in Massachusetts (2000-2017)")
plt.xlim([2000, 2017])
plt.ylim([0, 100])
plt.xlabel("Year")
plt.ylabel("Percentage")
plt.fill_between(years, poverty_rate)
plt.fill_between(years, poverty_rate, pct_renter)
sns.lineplot(years, poverty_rate, label="Poverty Rate")
sns.lineplot(years, pct_renter, label="Percentage Renter Occupied")
plt.show()
plt.gcf().clear()

# Percentage Stacked Bar Chart of different races in Massachusetts
White = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-white'].values
AfricanAmerican = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-af-am'].values
Hispanic = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-hispanic'].values
AmericanIndian = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-am-ind'].values
Asian = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-asian'].values
NHPI = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-nh-pi'].values
Other = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-other'].values
Multiple = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['pct-multiple'].values
barWidth = 0.5
plt.bar(years, White, width=barWidth, label='White')
plt.bar(years, AfricanAmerican, bottom=White, width=barWidth, label='African American')
plt.bar(years, Hispanic, bottom=[i+j for i, j in zip(White, AfricanAmerican)], width=barWidth, label='Hispanic')
plt.bar(years, AmericanIndian, bottom=[i+j+k for i, j, k in zip(White, AfricanAmerican, Hispanic)], width=barWidth, label='American Indian & Alaska Native')
plt.bar(years, Asian, bottom=[i+j+k+l for i, j, k, l in zip(White, AfricanAmerican, Hispanic, AmericanIndian)], width=barWidth, label='Asian')
plt.bar(years, NHPI, bottom=[i+j+k+l+m for i, j, k, l, m in zip(White, AfricanAmerican, Hispanic, AmericanIndian, Asian)], width=barWidth, label='Native Hawaiian and Other Pacific Islander')
plt.bar(years, Other, bottom=[i+j+k+l+m+n for i, j, k, l, m, n in zip(White, AfricanAmerican, Hispanic, AmericanIndian, Asian, NHPI)], width=barWidth, label='Other')
plt.bar(years, Multiple, bottom=[i+j+k+l+m+n+o for i, j, k, l, m, n, o in zip(White, AfricanAmerican, Hispanic, AmericanIndian, Asian, NHPI, Other)], width=barWidth, label='Multiple')
plt.title("Percentage of Races in Massachusetts (2000-2017)")
plt.xlim([2000, 2017])
plt.ylim([0, 100])
plt.xlabel("Year")
plt.ylabel("Percentage")
plt.legend(title="Races")
plt.show()
plt.gcf().clear()

# Geo Plot of population of the counties of Massachusetts in 2017
county_2017 = DataFrame(df_Eviction.loc[(df_Eviction['parent-location'] == 'Massachusetts') & (df_Eviction['year'] == 2017)].values)
fips = []
population = []

for index, row in county_2017.iterrows():
    if "County" in row[2]:
        fips.append(row[0])
        population.append(row[4])
endPts = list(np.mgrid[min(population):max(population):4j])
colorScale = ["#030512", "#1d1d3b", "#323268", "#3d4b94", "#3e6ab0",
              "#4989bc", "#60a7c7", "#85c5d3", "#b7e0e4", "#eafcfd"]
fig = ff.create_choropleth(
    fips=fips, values=population, scope=['MA'], show_state_data=True,
    colorscale=colorScale, binning_endpoints=endPts, round_legend_values=True,
    plot_bgcolor='rgb(229,229,229)',
    paper_bgcolor='rgb(229,229,229)',
    legend_title='Population by County',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    exponent_format=False
)
py.plot(fig, filename='choropleth_massachusetts')

# Grouped Bar chart of Median Gross Rent and Median household income
gross_rent = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['median-gross-rent'].values
household_income = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['median-household-income'].values
property_value = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['median-property-value'].values

barWidth = 0.25
r1 = np.arange(len(household_income))
r2 = [x + barWidth for x in r1]
# r3 = [x + barWidth for x in r2]

plt.bar(r1, household_income, label="Median Household Income", width=barWidth)
plt.bar(r2, property_value, label="Median Property Value", width=barWidth)
# plt.bar(r2, property_value, label="Median Property Value", width=barWidth)
plt.xticks([r + barWidth / 2 for r in range(len(gross_rent))], years)
plt.xlabel("Year")
plt.title("Gross Rent and Household Income in Massachusetts (2000-2017)")
plt.legend()
plt.show()
plt.gcf().clear()

# Line chart of eviction filings vs evictions in Massachusetts
eviction_filings = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['eviction-filings'].values
eviction = df_Eviction.loc[df_Eviction['name'] == 'Massachusetts']['evictions'].values
sns.lineplot(years, eviction, label="Evictions", markers=True, dashes=False)
sns.lineplot(years, eviction_filings, label="Eviction Filings", markers=True, dashes=False)
plt.title("Eviction Filings & Evictions in Massachusetts (2000-2017)")
plt.xlim([2000, 2018])
plt.xlabel("Year")
plt.ylabel("Evictions")
plt.show()
plt.gcf().clear()

county_2000_2017 = DataFrame(df_Eviction.loc[(df_Eviction['parent-location'] == 'Massachusetts') & (df_Eviction['year'].isin([2000, 2017]))].values)
lstCounty2000 = []
lstGRent2000 = []
lstCounty2017 = []
lstGRent2017 = []
for index, row in county_2000_2017.iterrows():
    if "County" in row[2]:
        if row[1] == 2000:
            lstCounty2000.append(row[2])
            lstGRent2000.append(row[7])
        elif row[1] == 2017:
            lstCounty2017.append(row[2])
            lstGRent2017.append(row[7])

barWidth = 0.25
r1 = np.arange(len(lstCounty2000))
r2 = [x + barWidth for x in r1]
plt.bar(r1, lstGRent2000, label="2000", width=barWidth)
plt.bar(r2, lstGRent2017, label="2017", width=barWidth)
# plt.bar(r2, property_value, label="Median Property Value", width=barWidth)
plt.xticks([r + barWidth / 2 for r in range(len(lstGRent2000))], lstCounty2000, rotation=35)
plt.xlabel("Counties")
plt.title("Median Gross Rent in Massachusetts 2000 & 2017")
plt.legend()
plt.show()
plt.gcf().clear()
