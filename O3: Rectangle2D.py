class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def containsPoint(self, x, y):
        return (self.__x - self.__width / 2) <= x <= (self.__x + self.__width / 2) and (self.__y - self.__height / 2) <= y <= (self.__y + self.__height / 2)

    def contains(self, other):
        x1, y1, w1, h1 = self.__x, self.__y, self.__width, self.__height
        x2, y2, w2, h2 = other.get_x(), other.get_y(), other.get_width(), other.get_height()
        return (x1 - w1 / 2 <= x2 - w2 / 2) and (x1 + w1 / 2 >= x2 + w2 / 2) and (y1 - h1 / 2 <= y2 - h2 / 2) and (y1 + h1 / 2 >= y2 + h2 / 2)

    def overlaps(self, other):
        x1, y1, w1, h1 = self.__x, self.__y, self.__width, self.__height
        x2, y2, w2, h2 = other.get_x(), other.get_y(), other.get_width(), other.get_height()
        return (abs(x1 - x2) < (w1 + w2) / 2) and (abs(y1 - y2) < (h1 + h2) / 2)

    def __contains__(self, other):
        return self.contains(other)

    def __cmp__(self, other):
        return self.getArea() - other.getArea()

    def __lt__(self, other):
        return self.getArea() < other.getArea()

    def __le__(self, other):
        return self.getArea() <= other.getArea()

    def __eq__(self, other):
        return self.getArea() == other.getArea()

    def __ne__(self, other):
        return self.getArea() != other.getArea()

    def __gt__(self, other):
        return self.getArea() > other.getArea()

    def __ge__(self, other):
        return self.getArea() >= other.getArea()
    
def main():
    print("Enter information for Rectangle 1:")
    x1 = float(input("Enter x-coordinate for the center: "))
    y1 = float(input("Enter y-coordinate for the center: "))
    width1 = float(input("Enter width: "))
    height1 = float(input("Enter height: "))
    r1 = Rectangle2D(x1, y1, width1, height1)

    print("\nEnter information for Rectangle 2:")
    x2 = float(input("Enter x-coordinate for the center: "))
    y2 = float(input("Enter y-coordinate for the center: "))
    width2 = float(input("Enter width: "))
    height2 = float(input("Enter height: "))
    r2 = Rectangle2D(x2, y2, width2, height2)

    # Display information
    print("\nRectangle 1:")
    print("Area:", r1.area)
    print("Perimeter:", r1.perimeter)

    print("\nRectangle 2:")
    print("Area:", r2.area)
    print("Perimeter:", r2.perimeter)

    print("\nResult of r1.containsPoint(r2.x, r2.y):", r1.contains_point(r2.x, r2.y))
    print("Result of r1.contains(r2):", r1.contains(r2))
    print("Result of r1.overlaps(r2):", r1.overlaps(r2))
    print("Result of r1 < r2:", r1 < r2)

if __name__ == "__main__":
    main()