class ElementBase:
    def __init__(self) -> None:
        self.__label:str=""
        self.__weight:int=0
        
    def get_label(self) -> str: return self.__label
    def get_weight(self) -> int: return self.__weight
    def set_label(self, label:str) -> None: self.__label = label; return self
    def set_weight(self, weight:int) -> None: self.__weight = weight; return self
    
class Vertex(ElementBase):
    def __init__(self, index:int) -> None:
        super().__init__()
        self.__neighbors:list[int|str]=[]
        self.__index: int = index
        
    def get_index(self) -> str: return self.__index
    def get_neighboors(self) -> list[int|str]: return self.__neighbors
    def set_neighbors(self, neighbors:list[int|str]) -> None: self.__neighbors = neighbors; return self

class Edge(ElementBase):
    def __init__(self, vertex_pair:list[int|str]) -> None:
        super().__init__()
        self.__vertex_pair:list[Vertex]=vertex_pair
        
    def get_vertex_pair(self) -> list[Vertex]: return self.__vertex_pair
    def set_vertex_pair(self, vertex_pair:list[Vertex]) -> None: self.__vertex_pair = vertex_pair; return self