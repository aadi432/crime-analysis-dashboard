# 🚔 Crime Analysis Dashboard

## 📌 Project Overview
The **Crime Analysis Dashboard** is an end-to-end **team-based data analytics project** developed by a group of **5 members**.  
The project analyzes crime data across India to identify trends, high-risk regions, reporting delays, and case resolution performance.

It demonstrates a complete analytics workflow including **data cleaning, SQL-based data storage, and interactive visualization using Power BI**.

---

## 🎯 Project Objectives
- Analyze crime distribution across **states and cities**
- Identify **high-crime regions** and major crime domains
- Understand **time-based crime patterns and reporting delays**
- Evaluate **case closure efficiency**
- Generate **actionable insights and recommendations**

---

## 🛠️ Tech Stack
- **Python** – Data cleaning & ETL pipelines  
- **Pandas** – Data preprocessing  
- **SQLAlchemy** – Database interaction  
- **MySQL & PostgreSQL** – Relational databases  
- **Power BI** – Interactive dashboards  
- **GitHub** – Version control & team collaboration  

---

## 📂 Project Structure
```
crime-analysis-dashboard/
│
├── data/
│   ├── FinalCrimeData.csv
│   └── StateCity.csv
│
├── python/
│   ├── loader.py              # Python data cleaning + MySQL ETL
│   └── postgresUpload.py      # PostgreSQL ETL pipeline (SQL via Python)
│
├── powerbi/
│   └── Crime_Analysis_Dashboard.pbix
│
├── screenshots/
│   ├── home_page.png
│   ├── overview.png
│   ├── state_analysis.png
│   ├── city_analysis.png
│   ├── time_analysis.png
│   └── insights.png
│
├── README.md
└── requirements.txt
```

---

## 🔄 Data Pipeline Architecture
**Raw CSV Data → Python Cleaning → SQL Databases → Power BI Dashboards**

---

## 🧹 Data Cleaning & MySQL ETL (`loader.py`)
This script performs **data cleaning and loading into MySQL**.

### Cleaning & Transformation Steps:
- Removed duplicate records
- Trimmed extra spaces from string columns
- Converted column names to SQL-friendly format
- Handled missing values and invalid entries
- Converted age fields to numeric
- Standardized gender values (`M`, `F`)
- Parsed date columns safely

### Output:
- Cleaned data automatically loaded into **MySQL tables**
- Tables created dynamically using Pandas & SQLAlchemy

---

## 🗄️ PostgreSQL ETL Pipeline (`postgresUpload.py`)
This script implements a **PostgreSQL ETL workflow** using Python with SQL-style operations.

### Key Features:
- Column name sanitization for SQL compatibility
- Handling of missing and invalid values
- Automatic detection of date and numeric columns
- Efficient bulk data insertion into PostgreSQL

### Output:
- Clean, structured PostgreSQL tables ready for analysis and BI usage

---

## 📊 Power BI Dashboard Overview

### 🏠 Home Page
- Navigation hub for all dashboard sections
- High-level overview of insights available

---

### 📈 Overview Analysis
**Key KPIs**
- Total Crimes Recorded: **50K**
- Violent Crimes: **14K**
- Crime Rate per Capita: **27%**
- Pending Crime Cases: **9,360**

**Visuals**
- Crimes by domain
- Year-wise crime trend (2014–2025)
- Crime distribution by category
- Top 5 states by crime rate
- Crime rate per capita map

---

### 🏛️ State-wise Crime Analysis
- Crimes segmented by **victim age groups**
- Identification of:
  - Most crime-affected states
  - States with highest violent crimes
  - Lowest crime states
- Maharashtra and Uttar Pradesh identified as major hotspots

---

### 🏙️ City-wise Crime Analysis
- **Safest City:** Nashik  
- **Most Affected City:** Delhi  
- **Overall Closure Rate:** 81.28%

**Insights**
- Top and lowest crime cities
- Metro vs Non-metro crime comparison
- Crimes by city and victim gender

---

### ⏱️ Delay & Time Analysis
- **Average Case Closure Time:** 467 days
- **Average Reporting Delay:** 142 days
- **Night Crimes:** 28%

**Analysis Includes**
- Best & worst performing states by resolution time
- Time-of-day and day-of-week crime heatmap
- Reporting delay categories

---

### 💡 Insights & Recommendations

#### Key Insights
- Resource mismatch in high-severity crime regions
- Large backlog of unresolved cases
- High volume of violent crimes impacting public safety

#### Recommendations
- Dynamic patrol allocation using hotspot analysis
- Encourage early crime reporting within 24 hours
- Implement digital case management systems

---

## 👥 Team Collaboration (5 Members)
- Tushar Chauhan
- Yash Malusare
- Aditya Shukla  
- Sejal Badwaik
- Piyush Ghule

