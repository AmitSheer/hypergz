# Installation
``` sh
$ pip install hypergz
```

-----------

<h1> Try the algorithm </h1>

To run your own example click [here](http://amitsheer.pythonanywhere.com/)

-----------

<h1> Introuction </h1>
This repository is an implementation of two algorithms:
<h2> Force-Directed Graph Drawing Using Social Gravity and Scaling </h2>
This algorithm creates a pleasant drawing of a **graph** in a shape of a circle using attraction and rejection forces as well as social.

This algorithm offers 3 methods of social gravity:

  - _Centrality by clossness:_ The closer a vertex is to other vertices the more central it will be.
  - _Centrality by betweeness:_ Vertex who is part of more shortest paths will be more central.
  - _Centrality by degree:_ Vertex with higher degree will be more central.
 
 <h3> Example of different centralities in tree graph </h3>

| Networkx | Clossness |
| ------------- | ------------- |
| <p align="center"><img src="https://user-images.githubusercontent.com/69470263/173134761-2e94912a-471b-4ed2-9f76-f09bfb31cff8.png"/></p>  | <p align="center"><img src="https://user-images.githubusercontent.com/69470263/173134856-da240d0e-fa77-4545-bfcb-4d68d932e88a.png"/></p>  |

| Betweeness | Degree |
| ------------- | ------------- |
| <p align="center"><img src="https://user-images.githubusercontent.com/69470263/173134909-6a92e31e-6ca3-4c01-9c58-264f64ee2077.png"/></p>  | <p align="center"><img src="https://user-images.githubusercontent.com/69470263/173134954-3b4820a2-ac2d-4a7d-94c2-e7febfa6cbeb.png"/></p>  |
