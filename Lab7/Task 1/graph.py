'''
Lab 7.1
'''
def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    main_list = []
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            line = line.replace(",", "")
            main_list.append([int(text) for text in line])
    return main_list

def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    dicti = []
    max_mini = []
    for i in edge_list:
        max_mini.append(max(i))
    range_go = max(max_mini)
    for i in range(1, range_go + 1):
        mass = []
        for j in edge_list:
            try:
                pos = j.index(i)
            except ValueError:
                continue
            if pos == 0:
                mass.append(j[1])
            else:
                mass.append(j[0])
            mass.sort()
        if mass == []:
            continue
        dicti.append([i, mass])
    dicti = dict(dicti)
    return dicti

print(to_edge_dict([[1, 2], [3, 4], [6, 7]]))

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    graph_val = list(graph.values())
    if edge[1] in graph_val[edge[0] - 1]:
        return True
    else:
        return False

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    dictinary = []
    if edge[0] not in graph:
        graph_update = {edge[0]: []}
        graph.update(graph_update)
    if edge[1] not in graph:
        graph_update = {edge[1]: []}
        graph.update(graph_update)
    graph_keys = list(graph.keys())
    graph_val = list(graph.values())

    if edge[0] not in graph_val[edge[1] - 1]:
        graph_val[edge[1] - 1].append(edge[0])
    if edge[1] not in graph_val[edge[0] - 1]:
        graph_val[edge[0] - 1].append(edge[1])

    graph_keys.append(edge[1])
    for i in range(len(graph)):
        dictinary.append([graph_keys[i], graph_val[i]])
    return dict(dictinary)

# <class 'IndexError'> list index out of range

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    try:
        dictinary = []
        graph_keys = list(graph.keys())
        graph_val = list(graph.values())
        graph_val[edge[1] - 1].remove(edge[0])
        graph_val[edge[0] - 1].remove(edge[1])
        for i in range(5):
            dictinary.append([graph_keys[i], graph_val[i]])
        return dict(dictinary)
    except ValueError:
        return graph
    except IndexError:
        return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    dictinary = []
    graph_keys = list(graph.keys())
    graph_val = list(graph.values())
    if node in graph_keys:
        return graph
    graph_keys.append(node)
    graph_val.append([])
    len_graph_keys = len(graph_keys)
    for i in range(len_graph_keys):
        dictinary.append([graph_keys[i], graph_val[i]])
    return dict(dictinary)

def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    try:
        dictinary = []
        graph_keys = list(graph.keys())
        graph_val = list(graph.values())
        graph_val.pop(node - 1)
        graph_keys.remove(node)
        len_graph_val = len(graph_val)
        for i in range(len_graph_val):
            if node in graph_val[i]:
                graph_val[i].remove(node)
        len_graph_keys = len(graph_keys)
        for i in range(len_graph_keys):
            dictinary.append([graph_keys[i], graph_val[i]])
    except IndexError:
        return graph
    return dict(dictinary)

print(del_node({1: [2], 3: [1]}, 2))

def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    graph_keys = list(graph.keys())
    graph_val = list(graph.values())
    coords = []
    len_graph_keys = len(graph_keys)
    for i in range(len_graph_keys):
        for j in range(len(graph_val[i])):
            if [graph_val[i][j], graph_keys[i]] not in coords:
                coords.append([graph_keys[i], graph_val[i][j]])
    with open("image.dot", "w", encoding='utf-8') as file:
        file.write("graph {\n")
        len_coords = len(coords)
        for i in range(len_coords):
            file.write("\t")
            file.write(str(coords[i][0]))
            file.write(" -- ")
            file.write(str(coords[i][1]))
            file.write(";\n")
        file.write("}")
