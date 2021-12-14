# US Yield Curve Dashboard

## Motivations
This project stems from a desire to learn more about FIRV. I decided that before getting into the RV side of things, it would be worth revising my understanding of what has driven G3 bond yields since the beginning of 2021.

In order to best understand what has happened to yields, I believe it would be most useful to be able to _visualise_ how yields themselves have evolved over time. Moreover, since the ultimate goal of this exercise is to improve my understanding of RV (and exploiting yield curve anomalies is one such application of RV to trading), I think it makes the most sense to consider yields in their relative context (i.e. in terms of the yield curve), rather than in their absolute context (i.e. just looking at the yield for a specific security). Thus, my first instinct was to try and find a yield curve visualiser on Google - by visualiser I mean something that is able to plot the evolution of the yield curve over time.

However, whilst raw data is widely available (e.g. on https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield), I was unable to find such a tool after some thorough Googling. Consequently, I have programmed a Python script that produces this tool (the visualisation occurs via a dashboard). Since too many requests resulted in a (temporary(?)) ban from Investing.com's API, I simply decided to copy and paste 2021 data from the above hyperlink into an Excel document.

## Tool Functionality
1) User decides the start and end dates for the period that they are interested in.
2) User decides how many graphs they want in the period (inclusive of the start date and a date which is approximately the same as the end date). The tool then calculates the dates for which individual yield curves will be plotted.
3) *Alternatively, the user can just specify the dates that they want plots of the yield curve for.*
4) The tool calculates the summary statistics (mean, standard deviation, coefficient of variation, minimum value, maximum value and 'current' value at the end of the date range) for US Treasuries (or T-bills) of each maturity.
5) The tool generates a dashboard consisting of a plot of the yield curve at each given date (with an accompanying legend) and followed by a table of all the summary statistics.

## Program




## Tips for Using The Tool


## Ideas for Further Development
1) Make it so that the user can input the start date, end date and number of graphs on the frontend rather than the backend of the tool.
2) Make the user input process error free such that it only accepts: dates for which there is data (e.g. it would not accept weekend dates since there is no data available for weekends) and a number of graphs <= size of the date interval.
3) Harder: create another dashboard section consisting of an animation of the yield curve over the _entire_ period.
4) Much harder: program a theoretical model of the yield curve to contrast with the actual yield curve for different dates - also include some summary statistics (e.g. difference between theoretical and actual yield for bonds of all the different maturities).
