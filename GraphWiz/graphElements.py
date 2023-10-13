class ElementBase:
    def __init__(self) -> None:
        self.__label:str|int=""
        self.__weight:int=1
    
    @property
    def label(self) -> str:
        return self.__label
    
    @label.setter
    def label(self, label:str) -> None:
        self.__label = label
    
    @property
    def weight(self) -> int:
        return self.__weight
    
    @weight.setter
    def weight(self, weight:int) -> None:
        self.__weight = weight
    
class Vertex(ElementBase):
    def __init__(self) -> None:
        super().__init__()

class Edge(ElementBase):
    def __init__(self) -> None:
        super().__init__()
        self.__source:Vertex|None=None
        self.__target:Vertex|None=None
    
    @property
    def source(self) -> Vertex:
        return self.__source
    
    @source.setter
    def source(self, vertex:Vertex) -> None:
        self.__source = vertex
    
    @property
    def target(self) -> Vertex:
        return self.__target

    @target.setter
    def target(self, vertex:Vertex) -> None:
        self.__target = vertex