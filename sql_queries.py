import sqlite3

conn = sqlite3.connect("covid_data.db")
cursor = conn.cursor()

# 1. Daily new cases by country
print("\n1. Daily new cases in the US:")
cursor.execute("""
SELECT date, location, new_cases
FROM covid
WHERE location = 'United States'
ORDER BY date
LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

# 2. Top 10 countries with highest total cases (exclude aggregate regions)
print("\n2. Top 10 countries with highest total cases:")
cursor.execute("""
SELECT location, MAX(total_cases) AS max_cases
FROM covid
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY max_cases DESC
LIMIT 10;
""")
for row in cursor.fetchall():
    print(row)

# 3. Vaccination progress in US (skip nulls)
print("\n3. Vaccination progress in the US:")
cursor.execute("""
SELECT date, people_fully_vaccinated
FROM covid
WHERE location = 'United States' AND people_fully_vaccinated IS NOT NULL
ORDER BY date ASC
LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

# 4. GDP vs Total Deaths (country-level only)
print("\n4. GDP vs Total Deaths (top 10):")
cursor.execute("""
SELECT location, gdp_per_capita, MAX(total_deaths) AS total_deaths
FROM covid
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY total_deaths DESC
LIMIT 10;
""")
for row in cursor.fetchall():
    print(row)

conn.close()
