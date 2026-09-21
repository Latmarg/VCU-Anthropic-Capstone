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

