# Usage (Windows)

Download this repo by pressing the green button "Clone or Download" above. Select "Download Zip".

Run `inclino.exe`. It might take 20-30 seconds before the script runs in the command line. 

It will ask for a file `example.csv` which is a csv file containing inclination measurement series as columns, just as can be seen in `example.csv`. The script will ask for a bunch of parameters which are defined in the figure below. It will then go on to compute A(t) and save resulting graphs in the working directory. 

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
