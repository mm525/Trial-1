# US Yield Curve Dashboard

## Motivations
Economics degrees are incredibly theoretical, with the associated homework assignments often lacking real world applicability. Since macroeconomics and econometrics are my two favourite parts of my economics degree, I wanted to create something that would combine both subjects. Moreover, given my interest in financial markets, I decided that the macroeconomics component should have a financial macroeconomics lean.

Since a clear financial macroeconomics application is interest rates (trading), so I decided to go for that. A common econometric technique used to analyse interest rates (more specifically, the yield curve) is Principal Components Analysis (PCA), which effectively decomposes the covariance (multidimensional spread) into the orthogonal (single-dimensional) factors that explain historical returns for zero-coupon US T-bills and USTs.



## Tool Functionality
1) User inputs the start date for the date range.

## Program




## Tips for Using The Tool


## Ideas for Further Development
1) Implement a script that allows the user to input figures on the tool's front-end, rather than having to manually update the back-end.
2) Make the user input process error free such that it only accepts: dates for which there is data (e.g. it would not accept weekend dates since there is no data available for weekends) and a number of graphs <= size of the date interval.
3) Harder: create another dashboard section consisting of an animation of the yield curve over the _entire_ period.
4) Much harder: model a theoretical yield curve and contrast it with the actual yield curve for different dates - also include some summary statistics (e.g. difference between theoretical and actual yield for bonds of all the different maturities).
