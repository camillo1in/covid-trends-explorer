-- Daily new cases by country (e.g., United States)
SELECT date, location, new_cases
FROM covid
WHERE location = 'United States'
ORDER BY date;


-- 1. Daily new cases by country (e.g., United States)
SELECT date, location, new_cases
FROM covid_data
WHERE location = 'United States'
ORDER BY date;


-- 2. Top 10 countries with the highest total cases
SELECT location, MAX(total_cases) AS max_cases
FROM covid_data
GROUP BY location
ORDER BY max_cases DESC
LIMIT 10;


-- 3. Vaccination progress in United States
SELECT date, people_fully_vaccinated
FROM covid_data
WHERE location = 'United States'
ORDER BY date ASC
LIMIT 10;


-- 4. GDP vs Total Deaths (simple view)
SELECT location, gdp_per_capita, MAX(total_deaths) AS total_deaths
FROM covid_data
GROUP BY location
ORDER BY total_deaths DESC
LIMIT 10;
