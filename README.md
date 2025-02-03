# Stock Market Analysis Dashboard

A comprehensive project analyzing the 6-month stock performance of major technology companies, including NVIDIA (NVDA), AMD, Intel (INTC), and Qualcomm (QCOM). This project combines Python for data preprocessing and analysis with Tableau for interactive visualizations.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Features](#features)
- [Dataset](#dataset)
- [Tools and Technologies](#tools-and-technologies)
- [Analysis Workflow](#analysis-workflow)
- [Tableau Dashboard](#tableau-dashboard)
- [How to Run the Code](#how-to-run-the-code)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Project Overview
This project analyzes stock price data of major tech companies over a 6-month period, focusing on daily growth percentages. It provides insights into stock trends, volatility, and growth patterns. The results are visualized through an interactive Tableau dashboard for better decision-making.

---

## Objective
1. To analyze the daily growth percentages of NVDA, AMD, INTC, and QCOM stocks over six months.
2. To identify trends, patterns, and volatility in stock performance.
3. To create an interactive Tableau dashboard for visualizing and presenting insights.

---

## Features
- **Data Preprocessing**:
  - Calculated daily growth percentages using the formula:  
    \[
    \text{Growth (\%)} = \frac{\text{Close} - \text{Open}}{\text{Open}} \times 100
    \]
  - Cleaned and formatted data for analysis.
  
- **Exploratory Data Analysis (EDA)**:
  - Analyzed stock price trends over time.
  - Visualized growth distributions and company-wise comparisons.
  
- **Interactive Tableau Dashboard**:
  - Visualized stock performance trends and growth patterns.
  - Enabled dynamic filtering by company and time range.

---

## Dataset
The dataset includes the following columns:
1. **Date**: The date of the stock price record.
2. **Close**: The closing price of the stock on that day.
3. **High**: The highest price reached during the day.
4. **Low**: The lowest price reached during the day.
5. **Open**: The opening price of the stock on that day.
6. **Volume**: The total number of shares traded during the day.
7. **Growth**: Calculated as \((\text{Close} - \text{Open}) / \text{Open} \times 100\).
8. **Company**: The name of the company (e.g., NVDA, AMD, INTC, QCOM).

---

## Tools and Technologies
- **Python**: For data preprocessing and exploratory data analysis (EDA).
  - Libraries: Pandas, Matplotlib, Seaborn
- **Tableau Public**: For creating interactive dashboards.
- **Jupyter Notebook**: For running Python scripts interactively.

---

## Analysis Workflow
1. **Data Loading**:
   - Imported CSV file containing stock price data into a Pandas DataFrame.

2. **Data Cleaning & Transformation**:
   - Ensured proper formatting of date columns.
   - Calculated daily growth percentages if not already present in the dataset.

3. **Exploratory Data Analysis (EDA)**:
   - Visualized stock price trends over time for each company.
   - Analyzed distributions of daily growth percentages using histograms and boxplots.

4. **Dashboard Creation**:
   - Exported cleaned data to a CSV file for use in Tableau Public.
   - Designed an interactive dashboard to visualize trends and patterns dynamically.

---

## Tableau Dashboard
### Link to Dashboard:
[Nvidia, AMD, Intel, Qualcomm 6-Month Stock Performance (% Daily Growth)](https://public.tableau.com/views/Book1_17385612208100/Sheet1)

### Embed Code:
```
<div class='tableauPlaceholder' id='viz1738561389330' style='position: relative'> <noscript> <a href='#'> <img alt='Nvidia, AMD, Intel, Qualcomm 6-month stock performance (% Daily Growth)' src='https://public.tableau.com/static/images/Bo/Book1_17385612208100/Sheet1/1_rss.png' style='border: none' /> </a> </noscript> <object class='tableauViz' style='display:none;'> <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /> <param name='name' value='Book1_17385612208100/Sheet1' /> <param name='tabs' value='no' /> <param name='toolbar' value='yes' /> <param name='static_image' value='https://public.tableau.com/static/images/Bo/Book1_17385612208100/Sheet1/1.png' /> <param name='animate_transition' value='yes' /> <param name='display_static_image' value='yes' /> <param name='display_spinner' value='yes' /> <param name='display_overlay' value='yes' /> <param name='display_count' value='yes' /> <param name='language' value='en-US' /> <param name='filter' value='publish=yes' /> </object> </div> <script type='text/javascript'> var divElement = document.getElementById('viz1738561389330'); var vizElement = divElement.getElementsByTagName('object'); vizElement.style.width = '100%'; vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px'; var scriptElement = document.createElement('script'); scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; vizElement.parentNode.insertBefore(scriptElement, vizElement); </script> 
```

## How to Run the Code
1. Clone this repository: 
```
git clone https://github.com/Poojareddyk16/Stock-Market-Analysis-Dashboard.git
cd Stock-Market-Analysis-Dashboard
 ```
2. Install required Python libraries:
```
pip install pandas matplotlib seaborn jupyter

```
3. Open the Jupyter Notebook:
```
jupyter notebook stock_analysis.ipynb

```
4. Run all cells sequentially to reproduce the analysis.
5. Export cleaned data to a CSV file for use in Tableau.

## Future Enhancements
Integrate sentiment analysis data to correlate market sentiment with stock performance.
Add predictive modeling to forecast future stock prices or growth percentages.
Enhance dashboards with additional interactivity using Tableau or Power BI.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
