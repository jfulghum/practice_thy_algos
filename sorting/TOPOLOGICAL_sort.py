"""
CONCEPT DRILL: TOPOLOGICAL SORT

 Identifying the next possible sort. It could be different. The important thing is that it is done before X. 
It doesn’t matter if we chop the potatoes before the onions. 

Dependency graph. It’s a graph that represents the dependencies between things. 

DAG - Direct Acyclic Graph

We can’t do a topological sort if the graph has cycles. It would cause an infinite loop. If we have to clean the kitchen before putting the oven 

TOPOLOGICAL SORT IS  a strategy for traversing a DAG in an ordered way.


We always have to start with a node that has no depencenies.
That has to go first. 

vertex_list = [
    "Prepare kitchen", "Mix flour", "Mix wet ingredients", "Combine", "Put in oven", "Clean kitchen"
]
edge_list = [
    ("Prepare kitchen", "Mix wet ingredients"),
    ("Prepare kitchen", "Mix flour"),
    ("Mix flour", "Combine"),
    ("Mix wet ingredients", "Combine"),
    ("Combine", "Put in oven"),
    ("Combine", "Clean kitchen"),
]

        Prepare Kitchen
            /     \
     Mix flour   Mix wet ingredients
              \ /
             Combine
              /     \
     Put in oven   Clean kitchen
          
"""
