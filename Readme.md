# Graph Theory

![Builds](https://github.com/project-chip/connectedhomeip/workflows/Builds/badge.svg)

#### A part of a university assignment

</br>

## Project Overview

Implementing weighted graph data structure alongside some known graph algorithms and a simple GUI with pygame


</br>

## How To Run
    In pycharm run the gui file inside the ui package Or run the main file




</br>

## How To Use The GUI
`'G' for graph operations`

`'A' for graph algorithms operations`

`'C' load new graph`


- `Add Node` click anywhere on the canvase and enter a node key 
- `Remove Node :` click `G` on the keyboard `'G' -> remove node`
- `Add Edge :` ` 'G' -> add edge`
- `Remove Edge :` `'G' -> remove edge`
- To excute an algorithm `'A'`
- `Save graph :` `'G'-> Save`
- `Open :` `'C' -> filename -> Load Graph`
- `New Graph :` `'C' -> New Graph`

</br>
</br>


## What has been done ?

- ### Graph

    - Add node
    - Delete node
    - Add edge
    - Delete edge
    - iterate through all the nodes
    - iterate through all the edges


- ### Algorithms

    - Shortest path between two nodes
    - The center node
    - Travelling salesman problem
    - Strongly connected


- ### Json

    - Load json graph
    - Save graph as json

</br>

## Algorithms Implementation

- `Dijkstra Algorithm` for the shortest path between two nodes O(|V|*|V|)
- `center` algorithm using the shortest path O(|V| * |V| * |V|)
- `TSP` back-tracking algorithm N*(E+V*Log(V))

</br>


# Running Times Comparison

    tested on windows : cpu i7 9700k , 16g

<br/>



#### 1000 Node Graph & 20 Edges

| Algorithm        |      JAVA        |    PYTHON     |
| -------------    | -------------    | ------------- |
| Build graph      |       7ms        |      7ms      |
| Shortest path    |       3ms        |      0.311ms  |
| TSP              |       97ms       |     5ms       |
| Center           |         *        |     *         |

 <br/>

#### 10000 Node Graph & 20 Edges

| Algorithm        |      JAVA        |    PYTHON     |
| -------------    | -------------    | ------------- |
| Build graph      |       8ms        |      83ms     |
| Shortest path    |       7ms        |       2ms     |
| TSP              |       393ms      |      54ms     |
| Center           |         *        |     *         |


  <br/>


#### 100000 Node Graph & 20 Edges

| Algorithm        |      JAVA        |    PYTHON     |
| -------------    | -------------    | ------------- |
| Build graph      |      49ms         |     810ms     |
| Shortest path    |       53ms        |     30ms      |
| TSP              |       513ms       |     561ms     |
| Center           |         *        |     *         |


<br/>

#### 1000000 Node Graph & 20 Edges

| Algorithm        |      JAVA        |    PYTHON     |
| -------------    | -------------    | ------------- |
| Build graph      |       412ms      |      8463ms   |
| Shortest path    |        *         |      308ms    |
| TSP              |         *        |     5585ms    |
| Center           |         *        |     *         |



  </br>

## Authors

* **Tarik Husin**  - linkedin -> https://www.linkedin.com/in/tarik-husin-706754184/
* **Wissam Kabha**  - github -> https://github.com/Wissam111

</br>

## References

https://en.wikipedia.org/wiki/Graph_center

https://en.wikipedia.org/wiki/Travelling_salesman_problem

https://www.youtube.com/watch?v=XB4MIexjvY0&t=484s

https://www.youtube.com/watch?v=XaXsJJh-Q5Y&t=600s
