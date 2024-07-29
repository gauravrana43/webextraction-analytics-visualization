import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv('book_data.csv')
fig= go.Figure()
fig.add_trace(go.Pie(
    labels=df['category'],
    values=df['book_price'],
    hole=0.3,
    textinfo='label+percent',  # Display both labels and percentage
    title='Category vs price'
))

fig.update_layout(
    title='Pie Chart Example',
    annotations=[dict(text='Fruit', x=0.5, y=0.5, font_size=20, showarrow=False)]  # Center annotation
)
# fig.update_layout(
#     title='Interactive Line Plot',
#     xaxis_title='Category',
#     yaxis_title='Price',
#     hovermode='x unified'
# )
fig.show()