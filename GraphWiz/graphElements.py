class vertex:
    def __init__(self) -> None:
        self.__label:str
        self.__weight:int
        self.__neighbors:list[int|str]
    def get_label(self) -> str: return self.__label
    def get_weight(self) -> int: return self.__weight
    def get_neighboors(self) -> list[int|str]: return self.__neighbors

class edge:
    def __init__(self) -> None:
        self.__label:str
        self.__weight:int
        self.__vertex_pair:list[int|str]
    def get_label(self) -> str: return self.__label
    def get_weight(self) -> int: return self.__weight
    def get_vertex_pair(self) -> list[int|str]: return self.__vertex_pair