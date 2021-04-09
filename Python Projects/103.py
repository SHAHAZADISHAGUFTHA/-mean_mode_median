import plotly.express as px
import pandas as pd 
df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.line(df,x="date",y="cases",color="country")
fig.show()