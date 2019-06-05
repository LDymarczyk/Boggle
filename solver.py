"""
Solves a "Boggle" game board by finding all solutions.
See http://www.python.org/doc/essays/graphs.html
"""
import operator
import sys
# from collections import Counter
from collections import defaultdict


points = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11, 9: 11, 10: 11, 11: 11, 12: 11, 13: 11, 14: 11, 15: 11, 16: 11}


def get_words(inputFile, norm=None):
    words = []
    with open(inputFile, "r") as f:
        for line in f:
            if norm:
                line = norm(line)
            words.append(line)

    return words


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    # import pdb; pdb.set_trace()
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def path_to_word(board, path):
    return "".join(board[pos[0]][pos[1]] for pos in path)


def nodes_from_board(board):
    nodes = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            nodes.append((i, j))

    return nodes


def graph_from_board(board):
    neighborOffsets = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1),
    )

    graph = {}
    nodes = nodes_from_board(board)
    for node in nodes:
        graph[node] = []

        for dn in neighborOffsets:
            if dn == (0, 0):
                continue
            neighbor = node[0] + dn[0], node[1] + dn[1]
            if (neighbor[0] >= 0 and neighbor[0] < len(board) and neighbor[1] >= 0 and neighbor[1] < len(board[0])):
                graph[node].append(neighbor)

    return graph


def normalize(s):
    return s.strip().lower()


def summarize_results(result):
    points_counter = 0
    for word in list(result.keys()):
        points_counter += points[len(word)]
    return points_counter


def boggle_solver(file_path):
    words = get_words(file_path, norm=normalize)
    words = dict((w, None) for w in words)

    board = [['a', 'l', 'o', 'j'],
             ['v', 'u', 't', 's'],
             ['l', 'c', 'h', 'e'],
             ['g', 'k', 'r', 'x']]


    nodes = nodes_from_board(board)
    graph = graph_from_board(board)

    solutionDetails = defaultdict(list)
    numNodes = len(nodes)

    for i in range(numNodes):
        for j in range(numNodes):
            if i == j:
                continue
            start, end = nodes[i], nodes[j]

            for path in find_all_paths(graph, start, end):
                candidateWord = normalize(path_to_word(board, path))
                if candidateWord in words:
                    solutionDetails[candidateWord].append(path)

    return summarize_results(solutionDetails)


print (boggle_solver("slowa.txt"))