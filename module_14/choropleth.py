import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("avgIQpercountry.csv")

df['Population - 2023'] = df['Population - 2023'].str.replace(',', '').astype(float)

fig = px.choropleth(df, locations='Country', locationmode='country names', hover_name='Country',
                     color='Average IQ', projection='natural earth', hover_data=['Literacy Rate' , 'Nobel Prices'],
                     title='Average IQ by Country', color_continuous_scale='agsunset')
fig.show()