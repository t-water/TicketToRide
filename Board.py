import csv
import heapq
from DestinationCards import generate_destination_cards

def build_board():
    adj_list = {}

    with open('Board.csv', newline='') as csv_file:
        board_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for row in board_reader:
            entries = row[0].split(',')
            v1 = entries[0]
            v2 = entries[1]
            score = int(entries[3])

            if v1 not in adj_list: adj_list[v1] = {}
            if v2 not in adj_list: adj_list[v2] = {}

            adj_list[v1][v2] = score
            adj_list[v2][v1] = score
    
    return adj_list

def find_shortest_path(adj_list, v1, v2):
    path_length = {}
    heap = [(0, v1)]

    while heap:
        score, edge = heapq.heappop(heap)

        if edge not in path_length:
            path_length[edge] = score

            for neighbor, distance in adj_list[edge].items():
                heapq.heappush(heap, (score + distance, neighbor))

    return path_length[v2]