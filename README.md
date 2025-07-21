# 📊 Google Search Trend Analysis using Python

## 🔍 Description

This project analyzes Google search trends for specific keywords (e.g., "Instagram") across regions and time periods using the Pytrends API. It visualizes trends using bar charts and pie charts to show interest by region and time.

## 🛠️ Tech Stack

- Python  
- Pytrends (Google Trends API wrapper)  
- Pandas  
- Matplotlib  

## ✅ Features

- Connects to Google Trends using Pytrends
- Tracks keyword popularity over time
- Identifies regions and cities with highest interest
- Fetches related queries
- Visualizes data using bar and pie charts
- Supports retry mechanism to handle request limits

*You may include:
- Interest Over Time graph
- Top Cities bar chart
- Pie chart showing city-level distribution*

## 🚀 How to Run

1. **Install dependencies**:
    ```bash
    pip install pytrends pandas matplotlib
    ```

2. **Run the script**:
    ```bash
    python "Google search analysis using Python (1).py"
    ```

3. **Modify the keyword**:
   - Update `kw_list = ["Instagram"]` to analyze different keywords.
   - You can also change the `geo`, `timeframe`, or resolution (e.g., city-level).

4. **View results**:
   - Bar and pie charts will be displayed.
   - Top related queries and regional interest will be printed in the terminal.

## 🌐 Notes

- Google Trends data is normalized (0–100) and may vary depending on time and region.
- The project uses retry logic to handle `TooManyRequestsError` from the API.

---

*Author: Tanuja Subhash Shinde*

