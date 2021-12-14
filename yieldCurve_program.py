import dash
import math
from dash import html
from dash import dcc
from dash import dash_table as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd

YC = pd.read_excel(r'/Users/marcusmayfield/Documents/US_Yield_Curve.xlsx')

start_inp = input("Please enter the start date in 'YYYY-MM-DD' format: ")
end_inp = input("Please enter the end date in 'YYYY-MM-DD' format: ")
graphs = int(input("Please enter the number of yield curves you want in your given interval: "))
start = YC.loc[YC['Date'] == start_inp].index.item()
end = YC.loc[YC['Date'] == end_inp].index.item()
step = math.floor((end-start)/(graphs-1))
dates = [start]
for i in range(graphs - 1):
    dates.append(dates[i] + step)

YC_no_dates = YC.drop(columns = 'Date', index = 1)
maturities = list(YC_no_dates.columns.values)
YCnp = YC_no_dates.to_numpy()
    
def generate_summaries(maturities, YC):
    for maturity in maturities:
        yield [maturity, '%.3f'%round(YC[maturity][start:end].mean(), 4), 
               '%.3f'%round(YC[maturity][start:end].std(), 4),
               '%.1f'%round((YC[maturity][start:end].std()/(YC[maturity][start:end].mean()))*100, 2),
               '%.2f'%round(YC[maturity][start:end].min(), 3), '%.2f'%round(YC[maturity][start:end].max(), 3), 
               '%.2f'%round(np.array(YC[maturity])[end], 3)]

s1M, s2M, s3M, s6M, s1Y, s2Y, s3Y, s5Y, s7Y, s10Y, s20Y, s30Y = generate_summaries(maturities, YC)
summary_table = pd.DataFrame([s1M, s2M, s3M, s6M, s1Y, s2Y, s3Y, s5Y, s7Y, s10Y, s20Y, s30Y], 
                             columns = ['Maturity', 'Mean', 'Std Dev', 'CV', 'Min', 'Max', 'Current'])

app = dash.Dash()

traces = [go.Scatter(x = maturities, y = YCnp[date], mode = 'lines', name = str(YC['Date'][date])) 
          for date in dates]
layout = go.Layout(title = 'Daily Treasury Par Yield Curve', xaxis = {'title': 'Maturity'}, 
                   yaxis = {'title': 'Yield (%)'}, yaxis_range = [0, 2.5])
fig = go.Figure(data = traces, layout = layout)

app.layout = html.Div(children = [
    html.Div([html.H1('US Yield Curve Visualisation Tool', style = {'textAlign': 'center', 
                                                                    'font-family': 'sans-serif'}),
    dcc.Graph(id = 'yield-curve', figure = fig)]),
    html.Div(children = [
        html.H2('Summary Statistics', style = {'font-family': 'sans-serif'}),
        dt.DataTable(
            id = 'summary-table',
            columns = [{'name': i, 'id': i} for i in summary_table.columns],
            data = summary_table.to_dict('records'),
            style_cell = {'textAlign': 'center', 'font-family': 'sans-serif'}
        )
    ])
])

if __name__ == '__main__':
    app.run_server()
