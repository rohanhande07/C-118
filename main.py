import pandas as pd
import plotly.express as px

df = pd.read_csv("petals_sepals.csv")

print(df.head())

fig = px.scatter(df, x="petal_size", y="sepal_size")
fig.show()
