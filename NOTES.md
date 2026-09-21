Source URL: https://huggingface.co/datasets/Anthropic/EconomicIndex

Release: release\_2025\_09\_15

Download Date: 9/14/2026

License: Data released under CC-BY, code released under MIT License.

Citation:

Author = Ruth Appel and Peter McCrory and Alex Tamkin and Michael Stern and Miles McCain and Tyler Neylon, title = Anthropic Economic Index Report: Uneven Geographic and Enterprise AI Adoption, date = 2025-09-15,   year = 2025, url = https://www.anthropic.com/research/anthropic-economic-index-september-2025-report





How was data collected? The data was provided by Anthropic from two sources, real-world conversations on Claude.ai after using a privacy-preserving system called Clio on them and transcripts from 1P API customers. They also provided geographic data, but only with the Claude conversations.



Unit of observation: Anthropic has provided observations including:

1. 1P API usage from 8/4/2025 - 8/11/2025, excluding geographic information, a row = an API usage record
2. Claude AI usage from 8/4/2025 - 8/11/2025, including geographic information, a row = a Claude usage record
3. The GDP of countries for 2024, a row = One country and their GDP
4. The GDP of US states for 2024, a row = One UIS state and their GDP
5. ISO Country codes, a row = One country and their ISO country code
6. ONET Task statements, a row = one O\*NET task statement
7. SOC occupation codes, a row = one SOC occupation code
8. Working age populations for countries in 2024, a row = one country and their working-age population
9. Working age populations for US states in 2024, a row = one US state and their working-age population



How any labels were produced: The labels of Augmentation vs Automation is determined by how Claude is utilized by the user. If they give Claude the task to do itself, then it is Automation. If they collaborate upon a task, then it is Augmentation.



2-3 headline numbers:

1. The US has the highest total usage of Claude at 21.6%
2. Singapore and Canada have some of the highest usage per capita at 4.6x and 2.9x the expected value based upon population





Findings:

| Claim (from task 3) | Actual (from data) | Match? |
|---|---|---|
| US highest usage, ~21.6% | US highest at 21.5% | Yes |
| Singapore ~4.6x per capita | 4.57, but ranks 3rd | Yes |
| Canada ~2.9x per capita, among highest | Not in top 10 | No |


Value of US comes to be 21.5% which is similar to the stated 21.6 in the article.

Singapore is number 3 with a similar value of 4.57 to the 4.6, but Canada is not even in the top 10 meaning its not in the highest usage per capita.


Raw Examples: Inspected the data using Excel. Specifically looking at Augmentation percent, Automation percent, usage count, usage percent, and usage per capita.

1. Israel - With a total usage of 10,941 Israel has the 14th largest usage count out of all countries listed. They have a 54.01% augmentation use versus a 45.99% automation use. This means that more users in Israel tend to augment their workload than offload it to Claude. Israel also has only a 1.134% usage percent and a per capita usage of 0.0018. When looking at the usage per capita index, it increases to 7 which is the highest out of any country.
2. Brazil - Brazil has the third largest number of users with 35,482 users, only falling behind the United States and India. Brazil has a large automation user percentage at 63.95% and only 36.05% of users opting for augmentation. This means that more Brazilians tend to use Claude to do work for them. The total usage percent is around 3.68% with a per capita usage of 0.000242. Their per capita index is in the middle at 0.93.
3. South Korea - With 35,285 users, South Korea comes in fifth place in total users by country. They tend to use Claude to augment their workload instead of automate it. With an augmentation use percent of 55.47 and an automation usage percent of 44.53. The usage percent is 3.66 and usage per capita for South Korea is 0.000972. South Korea's per capita index value is 3.72 which is not as large as Israel but still a good thing to note.
4. United States - The United States has the most Claude usage out of any country present in the dataset with over 208,200. Their automation and augmentation percentages are almost split down the middle with a 50.93% augmentation and 49.07% automation. The usage percent is very large at 21.59%, a per capita usage of 0.00095, and their per capita index at 3.62. This all makes sense since the US is very active in adopting new technology. 
5. Morocco - Morocco only has a total of 4845 uses, much lower than the other countries looked at. The usage in this country tend to lean toward automation, not as heavily as Brazil, but a decent amount with a 57.30% automation usage and the augmentation percent comes to 42.70%. With a usage percent of 0.502 and per capita usage of 0.000192, the numbers check out as Morocco does have a smaller population. Their usage per capita index is only a 0.74, the smallest of any of the countries looked at but still within reason. 
6. Not Classified - There is a large number of usage the falls under the geo_name "not_classified" meaning that they were not assigned a country. This only has usage count and usage percent, with a usage count of 150,999 and percent of 15.66. This is something odd to keep in mind, as it affects the percentages of usage count and usage percent.

