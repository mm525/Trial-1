# US Yield Curve Dashboard

## Motivations
AAAAA

## Tool Functionality
1) User decides the start and end dates for the period that they are interested in.
2) User decides how many graphs they want in the period (inclusive of the start date and a date which is approximately the same as the end date). The tool then calculates the dates for which individual yield curves will be plotted.
3) *Alternatively, the user can just specify the dates that they want plots of the yield curve for.*
4) The tool calculates the summary statistics (mean, standard deviation, coefficient of variation, minimum value, maximum value and 'current' value at the end of the date range) for US Treasuries (or T-bills) of each maturity.
5) The tool generates a dashboard consisting of a plot of the yield curve at each given date (with an accompanying legend) and followed by a table of all the summary statistics.

## Program




## Tips for Using The Tool


## Ideas for Further Development
1) Implement a script that allows the user to input figures on the tool's front-end, rather than having to manually update the back-end.
2) Make the user input process error free such that it only accepts: dates for which there is data (e.g. it would not accept weekend dates since there is no data available for weekends) and a number of graphs <= size of the date interval.
3) Harder: create another dashboard section consisting of an animation of the yield curve over the _entire_ period.
4) Much harder: model a theoretical yield curve and contrast it with the actual yield curve for different dates - also include some summary statistics (e.g. difference between theoretical and actual yield for bonds of all the different maturities).
