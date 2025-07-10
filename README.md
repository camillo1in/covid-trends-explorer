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

## Work in Progress

- [x] Initialized GitHub repo
- [x] Loaded 98MB+ CSV into Pandas
- [x] Inspected dataset structure
- [x] Cleaned and selected key columns (cases, deaths, vax, etc.)
- [x] Converted date to datetime format
- [x] Saved clean DataFrame to `covid_data.db` using SQLite
- [x] Created `.gitignore` to exclude the database file
- [x] Committed and pushed Day 1 progress
- [ ] Write and test SQL queries on the database
- [ ] Document insights and finalize README
- [ ] Add visual polish and post on LinkedIn

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

## GitHub Repo

https://github.com/camillo1in/covid-trends-explorer