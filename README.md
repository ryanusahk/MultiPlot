# MultiPlot
Manage and visualize 96 well plate growth data

###Requirements
- Python 2.6+
- SciPy Libraries
- Data in ASCII format from 96 well plate reader

###Functions
* Organize entire 96 well plate growth datasets easily
* Supports replicates, and errorbars (by 1 standard deviation)
* Supports blanks
* Plot single or multiple datasets together

###Usage
ExtractData.py takes in standard ASCII formatted 96 plate reader data and outputs a .json formatted .mplot database file.

Run with `python ExtractData.py 96well-data-file`

format.txt is used by ExtractData.py to organize the 96 well plate reader data. In format.txt, the user specifies:

```
Strain Name
Growth Condition
Replicate Well Locations
Blank Location
```
For example:
```
----------------------------
GRAPH 1
E.coli
LB Broth + Cyanide
A2 B6 C11 E11
H12
----------------------------
```
The blank data will be subtracted from the replicates to properly blank the data before visualization.

PlotData.py utilizes MatPlotLib and NumPy to manipulate and generate the plot image. PlotData imports .mplot data and prompts the user for which sets of data to plot simultaneously, whether errorbars are desired (1 std) and the title of the plot.

Run with `python PlotData.py`
