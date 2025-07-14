# COVID Trends Explorer (Python + SQL)

## Goal

This project analyzes global COVID-19 trends using real-world data from [Our World in Data](https://ourworldindata.org/coronavirus). It performs extraction, cleaning, and storage of data using Python and SQLite, then queries meaningful insights with SQL.

## Tech Stack

- Python
- Pandas
- SQLite
- SQL
- Git + GitHub

## Data Source

- [`owid-covid-data.csv`](https://covid.ourworldindata.org/data/owid-covid-data.csv)

## Key Insights

1. The United States recorded over 103 million total COVID-19 cases (the highest globally)

2. Vaccination rollout in the U.S. began in mid-December 2020, with steady early uptake.

3. Countries with higher GDP per capita (e.g., U.S., Germany, France) also saw higher death tolls. This hints at early exposure or reporting capacity.

4. India, Brazil, and China followed closely in total case count. The data highlights global spread across economic regions.

## Project Summary

- [x] Initialized GitHub repo
- [x] Loaded 98MB+ CSV into Pandas
- [x] Inspected dataset structure
- [x] Cleaned and selected key columns (cases, deaths, vax, etc.)
- [x] Converted date to datetime format
- [x] Saved clean DataFrame to `covid_data.db` using SQLite
- [x] Created `.gitignore` to exclude the database file
- [x] Committed and pushed Day 1 progress
- [x] Write and test SQL queries on the database
- [x] Document insights and finalize README
- [x] Add visual polish and post on LinkedIn

## Daily Log

July 10, 2025 (Day 1)
- Set up public GitHub repo  
- Loaded COVID-19 CSV with Pandas  
- Printed dimensions and inspected columns  
- Cleaned dataset: selected key columns, removed nulls  
- Converted date column to datetime format  
- Created and committed `README.md`  
- Wrote cleaned DataFrame to `covid_data.db` using SQLite  
- Created `.gitignore` to exclude the database  
- Final push of Day 1 complete  

July 11, 2025 (Day 2 Preview)
- Connect to `covid_data.db` using SQLite  
- Write SQL queries to extract insights:
  - Daily case trends by country  
  - Vaccination progress over time  
  - Mortality vs. GDP correlation  
  - Top 5 and bottom 5 countries by vaccination rate  
- Save queries and document results

July 12, 2025 (Day 3 Preview)
- Finalize and polish README:
  - Add SQL query samples and outputs  
  - Summarize 2–4 key insights in plain language  
  - (Optional) Add a project diagram or chart  
- Check Git commit history: clean, descriptive, and tight  
- Ensure `.db` file is ignored and repo is clean  
- Push all final changes  
- Add project to LinkedIn + pin to GitHub profile

## Insights

### 1. Daily New Cases in the US
- In early January 2020, reported cases were near 0.0.
- Confirms limited spread or underreporting in early phases.
- The pipeline can trace trends across time for a given country.

### 2. Countries with Highest Total Cases
- US, China, and India lead in total COVID-19 cases globally.
- Shows a blend of high testing capacity (US), dense population (India), and government-controlled reporting (China).

### 3. Vaccination Progress (US)
- Vaccinations began around December 13, 2020, starting with ~9,600 people fully vaccinated.
- Data confirms rollout trends and provides week-by-week progression.
- Steady increase over time supports vaccine logistics modeling.

### 4. GDP vs Total Deaths
- The US has both high GDP per capita (~$54K) with the world's highest absolute death count.
- Countries like India and Brazil show high deaths at much lower GDP per capita.
- Indicates economic output doesn't guarantee effective mitigation.

## GitHub Repo

https://github.com/camillo1in/covid-trends-explorer