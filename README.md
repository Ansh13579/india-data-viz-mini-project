# India Data Viz Mini Project

A small Streamlit dashboard for exploring state- and union-territory-level
indicators from India's 2011 Census, rendered with Plotly.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

The dashboard includes sortable population, literacy, sex-ratio and growth
indicators, plus a literacy-versus-sex-ratio scatter plot and a population
share chart.

## Data

`india_census_2011.csv` contains commonly published 2011 Census totals and
rates. It is provided as a local, offline dataset for this mini visualization.