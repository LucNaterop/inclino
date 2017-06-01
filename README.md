# Usage (Windows)

Download [inclino.exe](https://www.dl.dropboxusercontent.com/s/u19pco0bwyio1qn/inclino.exe) and save it for example on your desktop. 

Run `inclino.exe`. It might take 20-30 seconds before the script runs in the command line. 

It will ask for a file `example.csv` which is a csv file containing inclination measurement series as columns, just as can be seen in `example.csv`. Make sure that the csv files are in the same folder as `inclino.exe`. 

The script will ask for a bunch of parameters which are defined in the figure below. It will then go on to compute A(t) and save resulting graphs in the working directory. 

![Inclino Parameter Definition Sketch](parameter_definitions.png)

# Usage (Mac/Linux)
Make sure you have numpy and scipy installed:
```
pip install numpy scipy
```
Then simply run 
```
python inclino.py
```

# About

	Inclino v0.5
	Written by Luca Naterop
	Zürich, 2017
	Questions, suggestions and comments to luca@naterop.net
