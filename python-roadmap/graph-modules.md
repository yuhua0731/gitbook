# Graph Modules

{% hint style="success" %}
To play with graph, we can take advantage of the [networkx](https://networkx.org/) and [pygraphviz](https://pygraphviz.github.io/) libraries, as well as the widely used [DOT](https://en.wikipedia.org/wiki/DOT\_\(graph\_description\_language\)) graph description language.

* [https://networkx.org/](https://networkx.org/)
  * gallery: [https://networkx.org/documentation/latest/auto\_examples/index.html](https://networkx.org/documentation/latest/auto\_examples/index.html)
* [https://pygraphviz.github.io/](https://pygraphviz.github.io/)
  * gallery: [https://pygraphviz.github.io/documentation/stable/auto\_examples/index.html](https://pygraphviz.github.io/documentation/stable/auto\_examples/index.html)
{% endhint %}

## Installation

```shell
$ brew install graphviz
$ pip install pygraphviz

# if you got this ERROR: fatal error: 'graphviz/cgraph.h' file not found
# try to install with the following command, with all path specified
# https://github.com/pygraphviz/pygraphviz/issues/11
$ python -m pip install \
    --global-option=build_ext \
    --global-option="-I$(brew --prefix graphviz)/include/" \
    --global-option="-L$(brew --prefix graphviz)/lib/" \
    pygraphviz
```

{% file src="../.gitbook/assets/materials-queue (1).zip" %}
source code package from real python
{% endfile %}

<pre class="language-shell"><code class="lang-shell"><strong>$ dot -Tpng roadmap.dot -o my_graph.png # generate image from dot file
</strong></code></pre>

## Networkx module

### Define a node class

> example node class implementation ↓
>
> node must be <mark style="color:yellow;">**hashable**</mark>, required by networkx

<pre class="language-python"><code class="lang-python"><strong># example node City class
</strong><strong># extend from NamedTuple, which makes it hashable
</strong><strong>class City(NamedTuple):
</strong>    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None, # If the conversion is successful, it will store the integer value in year; otherwise, it will assign None.
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )
        
    def __repr__(self) -> str:
        return f"City: {self.name} ({self.country})\nYear: {self.year}\nPosition: {self.latitude}, {self.longitude}"
</code></pre>

### Load graph from a dot file

```python
# read from dot file
graph = nx.nx_agraph.read_dot("roadmap.dot")

# convert from dot graph to nxgraph
# node: customize hashable class
# edge: (node_name1, node_name2, edge_weight)
network = nx.Graph(
    (nodes[name1], nodes[name2], weights) 
    for name1, name2, weights in graph.edges(data=True))
    
# usually we will generate a dict of nodes as well
# a node object is needed as the argument in further applications
def load_graph(file_name, node_factory):
    graph = nx.nx_agraph.read_dot(file_name)
    # <class 'dict'> 
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    # <class 'networkx.classes.graph.Graph'>
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )

nodes, network = load_graph("roadmap.dot", City.from_dict)
```

### Get neighbors and weights

```python
# get neighbors of a specific node
# network.neighbors(argument1), where argument1 is a node object
# <dict_keyiterator object at 0x100b16b10>
neighbor = network.neighbors(nodes["london"])
for i in neighbor: print(i.name)

# get neighbor and distance information from network
# print them in the order of distance to 'london'
def sort_by(items, strategy):
    return sorted(items, key=lambda x: strategy(x[1]))

def by_distance(item):
    return int(item["distance"])
    
for neighbor, weights in sort_by(network[nodes["london"]].items(), by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
```

### Built-in search algorithms

```python
# bfs
for node in nx.bfs_tree(network, nodes["edinburgh"], sort_neighbors=order)):
    print("📍", node.name)

# dfs
for node in nx.dfs_tree(network, nodes["edinburgh"]):
    print("📍", node.name)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

# shortest path, first one
built_in_shortest_paths = " → ".join([i.name for i in nx.shortest_path(network, city1, city2)])

# all shortest paths, if not unique
for i, path in enumerate(nx.all_shortest_paths(network, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))
```

The breadth-first traversal is also the foundation for finding the <mark style="color:yellow;">**shortest path**</mark> between two nodes in <mark style="color:yellow;">**an undirected and unweighted graph**</mark>.

## Practice

[https://github.com/yuhua0731/python-roadmap](https://github.com/yuhua0731/python-roadmap)

