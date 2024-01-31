class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        def area_of_my_square(self):
            """ Calculate the area of the square """
            return self.width * self.height

        def perimeter_of_my_square(self):
            """ Calculate the perimeter of the square """
            return (self.width + self.height) * 2

        def __str__(self):
            """ Return a string representation of the square """
            return f"Square(width={self.width}, height={self.height})"


        if __name__ == "__main__":
            s = Square(width=12, height=9)
            print(s)
            print("Area:", s.area_of_my_square())
            print("Perimeter:", s.perimeter_of_my_square())

