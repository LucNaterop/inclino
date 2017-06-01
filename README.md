# Usage (Windows)
In a terminal, having installed numpy and scipy, run
```
python inclino.py
```
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
