# Usage (Windows)

Download [inclino.exe](https://www.dl.dropboxusercontent.com/s/u19pco0bwyio1qn/inclino.exe) and save it for example on your desktop. 

Run `inclino.exe`. It might take 20-30 seconds before the script runs in the command line. 

It will ask for a csv-file which has the following structure:
 - First column: The *depth* of inclination measurements
 - Second column: The *inclination* measurements

An example of such a file can be viewed in `example.csv`.

The script will ask for a bunch of parameters which are defined in the figure below. It will then go on to compute A(t) which is the distance from the instrument axis to the borehole wall. A pdf with the resulting graphs are saved in the same location as the csv file. The two resulting lines represent the distance for both sides. 

![Inclino Parameter Definition Sketch](parameter_definitions.png)

# Usage (Mac/Linux)
0. Open a terminal
1. Clone this repo 
```
git clone https://github.com/LucNaterop/inclino
```

2. Make sure you have numpy and scipy installed:
```
pip install numpy scipy
```

3. cd into the directory and run the script 
```
cd inclino/sourcecode
python inclino.py
```

# About

	Inclino v0.6
	Written by Luca Naterop
	Zürich, 2017
	Questions, suggestions and comments to luca@naterop.net
