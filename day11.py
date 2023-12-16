from typing import List, Set, Tuple
import time, heapq

class color:
   CYAN = '\033[96m'
   BOLD = '\033[1m'
   END = '\033[0m'

class Edge:
    def __init__(self, start, end, cost) -> None:
        self.start = start
        self.end = end
        self.cost = cost

class Vertex:
    def __init__(self, v_id, text, x, y, graph) -> None:
        self.v_id = v_id
        # self.is_start = True if text == CONST_START else False
        # self.is_end = True if text == CONST_END else False
        # if self.is_start:
        #     text = "a"
        # elif self.is_end:
        #     text = "z"

        self.text = text
        self.x = x
        self.y = y
        self.graph = graph
        self.cost_to_start = float("inf")
        self.neighbours = []

    def __str__(self) -> str:
        return self.text

    def __repr__(self) -> str:
        return self.text + " (" + str(self.x) + ", " + str(self.y) + ")"

    def __lt__(self, other) -> bool:
        return self.cost_to_start < other.cost_to_start

    def get_neighbours(self):
        return self.neighbours

    def compute_neighbours(self) -> None:
        if self.x > 0:
            self.neighbours.append((self.graph.matrix[self.y][self.x - 1], 1))

        if self.x < len(self.graph.matrix[self.y]) - 1:
            self.neighbours.append((self.graph.matrix[self.y][self.x + 1], 1))

        if self.y > 0:
            self.neighbours.append((self.graph.matrix[self.y - 1][self.x], 1))

        if self.y < len(self.graph.matrix) - 1:
            self.neighbours.append((self.graph.matrix[self.y + 1][self.x], 1))

class Graph:
    def init_map(self, lines: list[str]) -> None:
        self.map: List[List[str]] = list()
        exp_rows: Set[int] = set()
        exp_cols: Set[int] = set()
        galaxy_counter: int = 1

        # expand map
        for row, line in enumerate(lines):
            self.map.append([])
            exp_row: bool = True
            for col, char in enumerate(line):
                insert_char: str = char # if char != "#" else str(galaxy_counter)
                # print(">", insert_char, "<", len(insert_char))
                self.map[row].append(insert_char)
                if insert_char != ".":
                    exp_row = False
                    galaxy_counter += 1

            if exp_row:
                exp_rows.add(row)

        self.map_width: int = len(self.map[0])
        self.map_height: int = len(self.map)

        for col in range(self.map_width):
            exp_col: bool = True
            for row in range(self.map_height):
                if self.map[row][col] != ".":
                    exp_col = False
                    break

            if exp_col:
                exp_cols.add(col)

        for r in exp_rows:
            self.map.insert(r + 1, [])
            for c in range(self.map_width):
                self.map[r + 1].append(".")
            self.map_height += 1

        for c in exp_cols:
            for r in range(self.map_height):
                self.map[r].insert(c + 1, ".")
            self.map_width += 1
    
    def __init__(self, lines: list[str]) -> None:
        self.init_map(lines)
        self.matrix = []
        self.vertices = []

        self.galaxy_counter: int = 1
        for y in range(0, self.map_height):
            self.matrix.append([])
            for x in range(0, self.map_width):
                vertex_id = ""
                text: str = "." if self.map[y][x] == "." else str(self.galaxy_counter)
                v = Vertex(vertex_id, text, x, y, self)
                self.matrix[y].append(v)
                self.vertices.append(v)
                if (text != "."):
                    self.galaxy_counter += 1

        self.galaxy_counter -= 1

        for v in self.vertices:
            v.compute_neighbours()
    
    def print_map(self) -> None:
        for r in range(self.map_height):
            for c in range(self.map_width):
                print(self.map[r][c], end="")
            print()
        
    def print_path(self, path):
        for row in self.matrix:
            for v in row:
                found = v in path
                
                if found == False:
                    # not in path
                    output = v.text
                else:
                    # in path: print in bold
                    output = color.CYAN + v.text + color.END

                print(output, end="")
            print()

        print("->".join(p.text for p in path), " (length: ", len(path) - 1, ")")

    def dijkstra(self, source: str, target: str):
        self.reset()
        distances = {v: float("inf") for v in self.vertices}
        prev_v = {v: None for v in self.vertices}
        source_vertex: Vertex = next((v for v in self.vertices if v.text == source), None)
        dest_vertex: Vertex = next((v for v in self.vertices if v.text == target), None)
        assert source_vertex != None and dest_vertex != None

        distances[source_vertex] = 0 # set start to cost 0
        source_vertex.cost_to_start = 0
        heap = [source_vertex] # add start vertex to heap with cost 0

        while heap:
            v = heapq.heappop(heap)

            if v == dest_vertex:
                break # target reached

            curr_cost = v.cost_to_start
            if curr_cost > distances[v]: # skip vertex if it has been processed
                continue

            for neighbour, cost in v.get_neighbours():
                path_cost = curr_cost + cost
                
                if path_cost < neighbour.cost_to_start:
                    prev_v[neighbour] = v
                    neighbour.cost_to_start = path_cost
                    heapq.heappush(heap, neighbour)

        path = []
        curr_v = dest_vertex
        while prev_v[curr_v] is not None:
            path.insert(0, curr_v)
            curr_v = prev_v[curr_v]
        
        assert len(path) > 0
        path.insert(0, curr_v)

        return path

    def reset(self) -> None:
        for v in self.vertices:
            v.cost_to_start = float("inf")

input_path: str = 'inputs/day11.txt'

with open(input_path, 'r') as file:
    lines: List[str] = [line.strip() for line in file.readlines()]


start = time.time()
graph = Graph(lines)
end = time.time()
print("duration setup: " + str(end - start))

start = time.time()

paths_determined: Set[Tuple[str, str]] = set()
sum_path_length: int = 0
for galaxy in range(1, graph.galaxy_counter + 1):
    source = galaxy
    for target in range(1, graph.galaxy_counter + 1):
        if source == target or (source, target) in paths_determined or (target, source) in paths_determined:
            # print("skipped: ", source, "->", target)
            continue

        path = graph.dijkstra(str(source), str(target))
        # print(source, target, len(path) - 1)
        sum_path_length += len(path) - 1
        paths_determined.add((source, target))

# path = graph.dijkstra("1", "2")
# graph.print_path(path)
# path = graph.dijkstra("1", "3")


end = time.time()
print("duration dijkstra: " + str(end - start))

# graph.print_map()
# graph.print_path(path)
print(sum_path_length)