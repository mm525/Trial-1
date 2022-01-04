# US Rates Dashboard

## Motivations
Economics degrees are incredibly theoretical. This means that the associated homework assignments often lack real world applicability. Since macroeconomics and econometrics are (in my opinion) the two most interesting parts of an economics degree, I wanted to create something that would combine both subjects. Moreover, given my interest in financial markets, I decided that the macroeconomics component should have a financial macroeconomics lean.

One such financial macroeconomics application is interest rates (trading). A common econometric technique used to analyse interest rates (and more specifically, the yield curve) is Principal Component Analysis (PCA), which effectively decomposes the covariance (i.e. a multidimensional spread) into the orthogonal (one-dimensional) factors that explain the historical returns for zero-coupon US T-bills and USTs. Further, since the analysis revolves around the yield curve, I decided that a plot of the yield curve would give useful context to the PCA decomposition. Finally, presenting summary statistics alongside the PCA and the graph plot would help in buiding a clearer picture of movements in interest rates.

In an attempt to make this as user friendly as possible, I decided to teach myself the Dash framework so that I would be able to provide the user with as nice a UX as possible via a dynamically updating dashboard.

## Aim

#### Produce a dashboard, that subject to data inputted by the user (e.g. a date range), graphs the evolution of the yield curve over the specified interval, performs Principal Component Analysis on bond returns over the period and outputs key yield curve statistics.

## Tool Functionality
1) User inputs the start date for the date range.
2) User inputs the end date for the date range.
3) User inputs how many graphs they want plotted over their stated date range.
4) Subject to user inputs, the tool calculates the dates over which the evolution of the yield curve will be plotted.
5) The tool decomposes bond returns into their principal components (level, slope and curvature), taking note of the share of the total variance explained by each factor and their associated eigenvectors.
6) The tool generates the summary statistics (Mean, Standard Deviation, Coefficient of Variation (CV), Minimum Value, Maximum Value and End Value) for bonds of each maturity.
7) The tool creates graphs for the yield curve plot and the three main factors of the PCA.
8) The tool combines all of the above into a dashboard summary. 

## Example Dashboard
Here the user has decided:
- Start date: 2021-03-19
- End date: 2021-08-05
- Graphs over the date range: 6

And the accompanying output (zoom in for a clearer image): 

![Screenshot 2022-01-04 at 11 44 29](https://user-images.githubusercontent.com/64070251/148054262-4de158d4-0704-440c-b572-edc595a4e7a2.png)
![Screenshot 2022-01-04 at 11 45 20](https://user-images.githubusercontent.com/64070251/148054334-6bb33280-3a16-417a-8b2a-194c9f4483f4.png)
![Screenshot 2022-01-04 at 11 47 56](https://user-images.githubusercontent.com/64070251/148054623-b87732c3-f105-4105-b36d-28427bb53598.png)

## Tips for Using The Tool
1) Input data in the correct format, make sure to only enter weekday (Mon - Fri) dates for the dates and a number of graphs <= interval length (I have not yet implemented Try Except into the inputs).
2) Deselect graphs in the yield curve plot to help build an understanding of how the yield curve has evolved over time. In this example the user has deselected the 2nd, 3rd and 5th graphs:
![Screenshot 2022-01-04 at 11 54 36](https://user-images.githubusercontent.com/64070251/148055412-95a53a2e-a516-4ac8-a0cb-31d83de59d5e.png)
3) Zoom in around the short end of the yield curve.

## Ideas for Further Development
1) Make it so that the user can input the date range via the dashboard rather than in Jupyter notebook.
2) Make the user input process error free such that it only accepts: dates for which there is data (e.g. it would not accept weekend dates since there is no data available for weekends) and a number of graphs <= size of the date interval.
3) Create another dashboard section consisting of an animation of the yield curve over the _entire_ period.
4) Model a theoretical (expectations implied) yield curve and contrast it with the actual yield curve for different dates - also include some summary statistics (e.g. difference between theoretical and actual yield for bonds of all the different maturities).
