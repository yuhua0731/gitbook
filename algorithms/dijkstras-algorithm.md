---
description: find the minimum distance path between two nodes in a graph
---

# Dijkstra's algorithm

## Pseudo code

<pre class="language-python"><code class="lang-python">function Dijkstra(Graph, source):
    for each vertex v in Graph.Vertices:
<strong>        dist[v] ← INFINITY
</strong>        prev[v] ← UNDEFINED
        add v to Q
        dist[source] ← 0
        
        while Q is not empty:
            u ← vertex in Q with min dist[u]
            remove u from Q
            for each neighbor v of u still in Q:
                alt ← dist[u] + Graph.Edges(u, v)
                if alt &#x3C; dist[v]:
                    dist[v] ← alt
                    prev[v] ← u
                    
        return dist[], prev[]
</code></pre>

