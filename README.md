# Installation
``` sh
$ pip install hypergz
```

-----------

<h1> Try the algorithm </h1>

To run your own example clock [here](http://amitsheer.pythonanywhere.com/)

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

| Clossness | Betweeness |
| ------------- | ------------- |
| <p align="center"><img src="https://github.com/itay-rafee/Mathematical-Model-of-Malaria/blob/main/images/plot_1.png"/></p>  | <p align="center"><img src="https://github.com/itay-rafee/Mathematical-Model-of-Malaria/blob/main/images/plot_2.png"/></p>  |
 
  
