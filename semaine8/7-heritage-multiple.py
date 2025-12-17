class B():
    def __init__(self) -> None:
        super().__init__() # 
        print("B")

class A():
    def __init__(self) -> None:
        super().__init__() # 
        print("A")

class D():
    def __init__(self) -> None:
        super().__init__() # 
        print("D")


# De gauche à droite le init de A va s'executer en premier et son super va référencer au parent suivant
class C(A, B, D):
    def __init__(self) -> None:
        super().__init__() # executer le init du A
        print("C")

c = C()

# Method resolution order (de gauche à droite)
print(C.mro())