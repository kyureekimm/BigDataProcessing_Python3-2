import math

class Shape:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        self.type = "Circle"

    def get_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        self.type = "Rectangle"

    def get_area(self):
        return self.width * self.height

shapes = []

while True:
    shape_type = input("도형을 입력하세요 (circle/rectangle, 종료하려면 q): ")

    if shape_type == 'q':
        break
    
    if shape_type == 'circle':
        name = input("도형 이름을 입력하세요: ")
        radius = int(input("반지름을 입력하세요: "))
        shape = Circle(name, radius)
        shapes.append(shape)
        
    elif shape_type == 'rectangle':
        name = input("도형 이름을 입력하세요: ")
        width = int(input("가로 길이를 입력하세요: "))
        height = int(input("세로 길이를 입력하세요: "))
        shape = Rectangle(name, width, height)
        shapes.append(shape)
    
    else:
        print("잘못된 입력입니다.")

print("\n[도형별 면적 출력]")

for shape in shapes:
    print(f"{shape.name} ({shape.type})의 면적: {shape.get_area():.2f}")