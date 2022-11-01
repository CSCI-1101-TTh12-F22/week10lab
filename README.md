# Week 10 Section Activities

Use numpy and matplotlib to learn more about meteor strikes. The file `meteors.csv` is a list of all the meteorite strikes since 1800. The fields are `mass in grams`, `year`, `latitude`, and `longitude`.

You will need to install numpy (which most of you should have done last week in class) and matplotlib. If you don't remember how to install libraries, ask the TA, who will instruct you in using `pip3` or `pip`.

1. Use ` np.loadtxt()` to read in the included file `meteors.csv`. Remember to skip the first row, which is the header row. **It's okay if you get warnings! You can ignore them.*

2. Print out the following information:

* The mass of the heaviest meteorite.
* The mass of the lightest meteorite.
* The average mass of meteorites.
* The percentage of meteorites heavier than 1kg.

3. Print out the following information:

* The percent of meteorite strikes in the northern hemisphere.
* The percent of meteorite strikes in the western hemisphere.

*Note: negative latitudes represent the southern hemisphere, and negative longitudes represent the western hemisphere.* Why do you think meteorites are more common in the northern hemisphere than the southern hemisphere?

4. Print out the number of meteorite strikes per year. (Use `np.unique()` with `return_counts=True`.) 

5. Plot the number of meteorite strikes per year using `plot()` function in `matplotlib.pyplot`. Have meteorite strikes become more common over time? What could explain the sudden increase in frequency in the 1950s?

6. Plot a histogram of meteorite masses using the `hist()` in `matplotlib.pyplot`, with 10 bins and within the range `(0,1000)`. Are most meteorites small or big?

7. Scatter plot every meteorite strike by its longitude (as the x variable) and latitude (as the y variable). Does this visualization help understand why meteorite strikes are more common in the northern hemisphere?



