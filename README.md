# DataViz-global-population
# World Population Data Analysis (1970–2022)

This project explores and visualizes global population trends by country and continent from 1970 to 2022. It leverages Python's powerful libraries — pandas, matplotlib, and seaborn — to perform insightful data analysis and create impactful visualizations.

## Key Objectives
- Analyze top and bottom countries by population in 2022.
- Visualize population growth trends across continents from 1970 to 2022.
- Identify fastest-growing and declining countries.
- Explore continent-wise population distribution and growth.
- Highlight population density extremes (most and least densely populated countries).

## Tools & Libraries Used
- Python 3.x
- pandas
- matplotlib
- seaborn


## Sample Visualizations
- Bar charts comparing top 10 most and least populated countries.
- Line chart showing decade-wise growth for each continent.
- Pie chart of 2022 continent population distribution.
- Dual bar plots for high vs low density countries.

## Insights Gained
- Asia continues to lead global population with massive growth over decades.
- Certain small nations have the highest population densities.
- Some countries have seen population decline since 1970.

## Data Source
The dataset used is `world_population.csv`, which includes population metrics from 1970 to 2022, area, density, and continent classification.

## Visualizations Overview

This project includes multiple visualizations to explore the data effectively. Each plot was created using seaborn or matplotlib, styled with clean color palettes for clarity and insight.

### 1. Top 10 Most and Least Populated Countries (2022)
- **Type:** Horizontal Bar Charts (2 subplots)
- **Purpose:** Compare the 10 countries with the highest and lowest populations.
- **Details:**
  - Used two distinct but related color gradients (dark to light).
  - Helps visualize the vast differences between populous countries like India/China and small nations like Tuvalu or Nauru.

**Output:** `01 Top 10 population countries.png`

---

### 2. Population Growth by Continent (1970–2022)
- **Type:** Multi-line Chart
- **Purpose:** Track and compare population growth across continents over five decades.
- **Details:**
  - Each line represents a continent.
  - X-axis includes years from 1970 to 2022.
  - Y-axis shows population (scaled appropriately).

**Output:** `02 growthhh.png`

---

### 3. Fastest Growing and Declining Countries
- **Type:** Dual Horizontal Bar Charts (2 subplots)
- **Purpose:** Identify the countries with the largest increase or decrease in population from 1970 to 2022.
- **Details:**
  - Sorted by absolute change in population.
  - Separate colors and gradient direction used for growing vs declining countries.

**Output:** `03 top fastest growing and decreasing countries.png`

---

### 4. Population by Continent (1970 vs 2022)
- **Type:** Grouped Bar Chart
- **Purpose:** Compare total population by continent for two different years.
- **Details:**
  - Two bars per continent (1970 and 2022).
  - Shows how some continents (like Africa and Asia) grew significantly, while others remained stable.

**Output:** `04 Continent bar chart.png`

---

### 5. Population Density Insights
- **Type:** Dual Bar Charts (2 subplots)
- **Purpose:** Highlight countries with highest and lowest population densities.
- **Details:**
  - Top subplot: Highest density countries (e.g., Bangladesh, Singapore).
  - Bottom subplot: Lowest density countries (e.g., Australia, Canada).

**Output:** `05 density populated.png`

---

### 6. Population Distribution by Continent (2022)
- **Type:** Pie Chart
- **Purpose:** Show the percentage share of each continent in global population as of 2022.
- **Details:**
  - Soft color palette for clarity.
  - Labels are clean and adjusted to prevent overlap.

**Output:** `06 Continent population.png`
