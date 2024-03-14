import heapq
from src.models.utils_models import Point
from src.models.tile_model import Tile
from src.utils.map_variables import TILES_GRID_COL_ROW

class Node:
    _row: int = 0
    _col: int = 0
    _g: int = 0
    """The cost of moving from the start node to this node."""
    _h: int = 0
    """The estimated cost of moving from this node to the end node."""
    _f: int = 0
    """The total cost of moving from the start node to the end node through this node."""
    _parent_node: "Node" = None
    
    def __init__(self, row: int, col: int, g: int, h: int, parent_node: "Node"):
        self._row = row
        self._col = col
        self._g = g
        self._h = h
        self._f = g + h
        self._parent_node = parent_node
    def set_cost(self, g: int, h: int):
        self._g = g
        self._h = h
        self._f = g + h
    def get_key(self):
        return Node.get_key_from_point(Point(self._col, self._row))
    def __lt__(self, other: "Node"):
        """This method is used to compare two nodes."""
        return self._f < other._f
    @staticmethod
    def get_key_from_point(point: Point):
        return f"{point.x}_{point.y}"

class PathFinder():
    _tiles_info: dict[str, Tile] = {}
    
    """Pathfinder that implements the A* search in a map."""
    def __init__(self):
        self._open_list: list[Node] = []
        self._open_map: dict[str, Node] = {}
        self._closed_map: dict[str, Node] = {}
        self._goal_point: Point = None
        self._horizontal_cost = 10
        self._diagonal_cost = 14
        self._map_cols = TILES_GRID_COL_ROW.x
        self._map_rows = TILES_GRID_COL_ROW.y
    
    def initialize(self, tiles_info: dict[str, Tile]):
        self._tiles_info = tiles_info
        
    def find_path(self, start_point: Point, goal_point: Point):
        self._goal_point = goal_point
        self._open_list = []
        self._open_map.clear()
        self._closed_map.clear()
        result: list[Point] = []
        
        cost_to_goal = self._cost_to_goal(start_point.y, start_point.x)
        start_node = Node(start_point.y, start_point.x, 0, cost_to_goal, None)
        self._add_to_open(start_node)
        
        while len(self._open_list) > 0:
            current_node = heapq.heappop(self._open_list)
            del self._open_map[current_node.get_key()]
            
            self._closed_map[current_node.get_key()] = current_node
            
            if current_node._row == goal_point.y and current_node._col == goal_point.x:
                return self._build_path(current_node)
            
            self._generate_and_process_a_neighbor_node(current_node, 0, 1)
            self._generate_and_process_a_neighbor_node(current_node, 0, -1)
            self._generate_and_process_a_neighbor_node(current_node, 1, 0)
            self._generate_and_process_a_neighbor_node(current_node, -1, 0)
            self._generate_and_process_a_neighbor_node(current_node, 1, 1)
            self._generate_and_process_a_neighbor_node(current_node, 1, -1)
            self._generate_and_process_a_neighbor_node(current_node, -1, 1)
            self._generate_and_process_a_neighbor_node(current_node, -1, -1)
            
        return result
            
    def _generate_and_process_a_neighbor_node(self, current_node: Node, delta_row: int, delta_col: int):
        neighbor_row = current_node._row + delta_row
        neighbor_col = current_node._col + delta_col
        if neighbor_row < 1 or neighbor_row > self._map_rows or neighbor_col < 1 or neighbor_col > self._map_cols:
            return
        key_of_neighbor = Node.get_key_from_point(Point(neighbor_col, neighbor_row))
        if self._tiles_info[key_of_neighbor]._blocked:
            return
        if key_of_neighbor in self._closed_map:
            return
        
        cost_to_adjacent = self._cost_to_adjacent(delta_row, delta_col) + current_node._g
        cost_to_goal = self._cost_to_goal(neighbor_row, neighbor_col)
        
        if key_of_neighbor not in self._open_map:
            neighbor_node = Node(neighbor_row, neighbor_col, cost_to_adjacent, cost_to_goal, current_node)
            self._add_to_open(neighbor_node)
            return
            
        neighbor_node = self._open_map[key_of_neighbor]
        if cost_to_adjacent < neighbor_node._g:
            neighbor_node.set_cost(cost_to_adjacent, cost_to_goal)
            neighbor_node._parent_node = current_node
            heapq.heapify(self._open_list)
        
        
    
    def _build_path(self, node: Node):
        result: list[Point] = []
        current_node: Node = node
        while current_node._parent_node is not None:
            result.append(Point(current_node._col, current_node._row))
            current_node = current_node._parent_node
            
        result.append(Point(current_node._col, current_node._row))
        result.reverse()
        return result
    
    def _cost_to_goal(self, row: int, col: int):
        return (abs(self._goal_point.x - col) + abs(self._goal_point.y - row)) * self._horizontal_cost
    
    def _cost_to_adjacent(self, delta_row: int, delta_col: int):
        if delta_row == 0 or delta_col == 0:
            return self._horizontal_cost
        return self._diagonal_cost
    
    def _add_to_open(self, node: Node):
        heapq.heappush(self._open_list, node)
        self._open_map[node.get_key()] = node
        
PATH_FINDER = PathFinder()
    