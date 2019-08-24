# Graph-Project
School project- Shortest path

The algorithm finds the shortest way to escape from a burning high-rise building using a modified A* + PRM algorithm.
Allows you to compare it agaisnt other algorithms, such Dijkstra and Dijkstra + PRM and A* and shows the difference.

How to use the code in our project:
Eveything you need to change is found in a file called `main.py`. Now as an end user you can choose which algorithm you want to execute. In order to choose/change your desired algorithm, go to line 21 and change the constant variable, e.g. - 
```python
RUNNING_ALGORITHM = "our_algorithm"
```
to the one you want. Your options are 
1. our_algorithm
2. prm_dijkstra
3. dijkstra
4. a_star

Make sure you pick only one out of these four, otherwise you will receive an excpetion.

Later you will need to choose on which building sizes you would like the algorithm to run. You have 3 options, all which include a range of sizes, in meters. 
1. LARGE (90, 100, 110, 120, 130, 140, 150, 160, 170, 180)
2. MEDIUM (50, 60, 70, 80, 90)
3. SMALL (10, 20, 30, 40)

In order to pick the sizes, go to line 20 and change the following: 
```python
GRAPH_SIZE = Size.MEDIUM
```
Size is of class Enum which holdes three sizes. Your options are:
1. `Size.LARGE`
2. `Size.MEDIUM`
3. `Size.SMALL`

Now You're going to want to pick the amount of buildings on which you're going to test the algorithm on.

You can range from 1 - How much you want. Go to line 22 and change the following constant:
```python
AMOUNT_OF_GRAPHS = 50
```
This shows I picked to test my algorithm on 50 buildings.

Last you have the options to choose whether or not to show the result of your path in a 2D/3D model, by changing the boolean const on line 26: `SHOW_ANIMATION = True` True stands for show graphic graphs, False for the opposite.

All of the algorithm's output will be saved to a log file in the project's directory under the name <algorithm name+amount of graphs>.log, for example `"our_algorithm_50.log"`
You are now ready to start the execution of your test.
