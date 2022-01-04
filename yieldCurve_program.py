import numpy as np
import pandas as pd
import dash
import math
from sklearn.decomposition import PCA
import plotly.graph_objs as go
from dash import html
from dash import dcc
from dash import dash_table as dt

                                            # PROGRAM SETUP #
# Read data into a DataFrame
YC = pd.read_excel(r'/Users/marcusmayfield/Documents/US_Yield_Curve.xlsx')

# Ask user for inputs
start_inp = input("Please enter the start date in 'YYYY-MM-DD' format: ")
end_inp = input("Please enter the end date in 'YYYY-MM-DD' format: ")
graphs = int(input("Please enter the number of yield curves you want in your given interval: "))

# Convert the start and end dates into their integer position in the entire date range
start = YC.loc[YC['Date'] == start_inp].index.item()
end = YC.loc[YC['Date'] == end_inp].index.item()

# Calculate the list of dates for which the yield curves will be plotted
step = math.floor((end - start)/(graphs - 1))
dates = [start]
for i in range(graphs - 1):
    dates.append(dates[i] + step)
    
# Drop the 'Date' column from YC, then assign the remaining column names (i.e. all the maturities) to a new variable
YC_nd = YC.drop(columns = 'Date', index = 1) # YC with "No Dates" (hence the *nd*)
maturities = list(YC_nd.columns.values)

# Convert YC without 'Date' into a numpy array
YCnp = YC_nd.to_numpy()

                                    # PRINCIPAL COMPONENT ANALYSIS # 

# Decompose the covariance into its (orthogonal) principal components
pca_level = PCA().fit(YC_nd[start:end])    

# Share of the total variance explained by the three main factors (level, slope and curvature)
fLevel = '%.2f'%round(pca_level.explained_variance_ratio_[0], 2)
fSlope = '%.2f'%round(pca_level.explained_variance_ratio_[1], 2)
fCurv = '%.2f'%round(pca_level.explained_variance_ratio_[2], 2)

# Eigenvectors for each of the factors
level = pca_level.components_[0]
slope = pca_level.components_[1]
curvature = pca_level.components_[2]

                                        # SUMMARY STATISTICS #

# Function for generating the summary statistics for a given maturity
def generate_summaries(maturities, YC):
    for maturity in maturities:
        yield [maturity, '%.3f'%round(YC[maturity][start:end].mean(), 4),                               # Mean
               '%.3f'%round(YC[maturity][start:end].std(), 4),                                          # Standard Deviation
               '%.1f'%round((YC[maturity][start:end].std()/(YC[maturity][start:end].mean()))*100, 2),   # Coefficient of Variation (CV)
               '%.2f'%round(YC[maturity][start:end].min(), 3),                                          # Minimum Value
               '%.2f'%round(YC[maturity][start:end].max(), 3),                                          # Maximum Value
               '%.2f'%round(np.array(YC[maturity])[end], 3)]                                            # (Current) Value at End of Date Range

# Generate summary statistics for the bond of each maturity
s1M, s2M, s3M, s6M, s1Y, s2Y, s3Y, s5Y, s7Y, s10Y, s20Y, s30Y = generate_summaries(maturities, YC)
# Convert all the summaries and the accompanying titles into a DataFrame
summary_table = pd.DataFrame([s1M, s2M, s3M, s6M, s1Y, s2Y, s3Y, s5Y, s7Y, s10Y, s20Y, s30Y], 
                             columns = ['Maturity', 'Mean', 'Std Dev', 'CV', 'Min', 'Max', 'Current'])

                                            # DASHBOARD #
# Create Dashboard
app = dash.Dash()

# Create graphs for the relevant sections on the Dashboard #
# Graphs for how the YC has changed over time
traces = [go.Scatter(x = maturities, y = YCnp[date], mode = 'lines', name = str(YC['Date'][date])) 
          for date in dates]
layout = go.Layout(title = 'Daily Treasury Par Yield Curve', xaxis = {'title': 'Maturity'}, 
                   yaxis = {'title': 'Yield (%)'}, yaxis_range = [0, 2.5])
fig = go.Figure(data = traces, layout = layout)

# Graphs for Principal Components Analysis (PCA)
data_level = go.Scatter(x = maturities, y = level, mode = 'lines')
layout_level = go.Layout(title = 'Change In Tenor Per 1 BPS Increase in Level of Rates',
                    xaxis = {'title': 'Maturity'}, yaxis = {'title': 'BPS'})
data_slope = go.Scatter(x = maturities, y = slope, mode = 'lines')
layout_slope = go.Layout(title = 'Change In Tenor Per 1 BPS Increase in Slope of Yield Curve',
                    xaxis = {'title': 'Maturity'}, yaxis = {'title': 'BPS'})
data_curvature = go.Scatter(x = maturities, y = curvature, mode = 'lines')
layout_curvature = go.Layout(title = 'Change In Tenor Per 1 BPS Increase in Curvature of Yield Curve',
                    xaxis = {'title': 'Maturity'}, yaxis = {'title': 'BPS'})

fig_level = go.Figure(data = data_level, layout = layout_level)
fig_slope = go.Figure(data = data_slope, layout = layout_slope)
fig_curvature = go.Figure(data = data_curvature, layout = layout_curvature)

# Code for Dashboard
app.layout = html.Div(children = [
    # Dashboard title
    html.Div([html.H1('US Yield Curve Visualisation Tool', style = {'textAlign': 'center', 
                                                                    'font-family': 'sans-serif'})
             ]),
    
    # Dashboard section for YC evolution over the inputted timeframe
    html.Div([html.H2('US Yield Curve Evolution Over Time', style = {'font-family': 'sans-serif',
                                                                    'textAlign': 'center',}),
              dcc.Graph(id = 'yield-curve', figure = fig)]),
    
    # Dashboard section for PCA
    html.Div([html.H2('Principal Components Analysis (PCA)', style = {'font-family': 'sans-serif',
                                                                     'textAlign': 'center',}),
              html.Div([
                  dcc.Graph(id = 'PCA1', figure = fig_level, style = {'display': 'inline-block'}),
                  dcc.Graph(id = 'PCA2', figure = fig_slope, style = {'display': 'inline-block'}),
                  dcc.Graph(id = 'PCA3', figure = fig_curvature, style = {'display': 'inline-block'}),
                  html.Div([
                      html.H3('Share of Variance Explained by The Different Factors',
                             style = {'font-family': 'sans-serif', 'padding-left': '2.5%'}),
                      html.H3(f'Level: {fLevel}',
                             style = {'font-family': 'sans-serif', 'padding-left': '5%'}),
                      html.H3(f'Slope: {fSlope}',
                             style = {'font-family': 'sans-serif', 'padding-left': '5%'}),
                      html.H3(f'Curvature: {fCurv}',
                              style = {'font-family': 'sans-serif', 'padding-left': '5%'})
                  ])
              ])
             ]),
    
    # Dashboard section for summary statistics
    html.Div([html.H2('Summary Statistics', style = {'font-family': 'sans-serif',
                                                    'textAlign': 'center',}),
              dt.DataTable(id = 'summary-table',
                           columns = [{'name': i, 'id': i} for i in summary_table.columns],
                           data = summary_table.to_dict('records'),
                           style_cell = {'textAlign': 'center', 'font-family': 'sans-serif'}
                          )
             ])
])

if __name__ == '__main__':
    app.run_server()
