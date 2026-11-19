from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_FILE = Path(__file__).parent / "india_census_2011.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_FILE)


def main() -> None:
    st.set_page_config(page_title="India Census 2011", layout="wide")
    st.title("India Census 2011")
    st.caption("State and union territory population indicators")

    data = load_data()

    metric_labels = {
        "population": "Population",
        "literacy_rate": "Literacy rate (%)",
        "sex_ratio": "Sex ratio (women per 1,000 men)",
        "growth_rate": "Population growth (2001-2011, %)",
    }
    metric = st.sidebar.selectbox("Indicator", list(metric_labels), format_func=lambda key: metric_labels[key])
    top_n = st.sidebar.slider("States to display", min_value=5, max_value=len(data), value=15)

    chart_data = data.sort_values(metric, ascending=False).head(top_n)
    bar = px.bar(
        chart_data,
        x=metric,
        y="state",
        orientation="h",
        color=metric,
        color_continuous_scale="Teal",
        labels=metric_labels,
        title=f"Top {top_n}: {metric_labels[metric]}",
        text=metric,
    )
    bar.update_layout(yaxis={"categoryorder": "total ascending"}, coloraxis_showscale=False)
    bar.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    st.plotly_chart(bar, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        population = px.scatter(
            data,
            x="literacy_rate",
            y="sex_ratio",
            size="population",
            color="growth_rate",
            hover_name="state",
            labels=metric_labels,
            title="Literacy, sex ratio and population",
        )
        st.plotly_chart(population, use_container_width=True)
    with col2:
        distribution = px.pie(
            chart_data.head(10),
            names="state",
            values="population",
            title="Share of selected population",
        )
        st.plotly_chart(distribution, use_container_width=True)

    st.subheader("Census data")
    st.dataframe(
        data.rename(columns={"state": "State/Union Territory", **metric_labels}).sort_values(
            "population", ascending=False
        ),
        use_container_width=True,
        hide_index=True,
    )


if __name__ == "__main__":
    main()
