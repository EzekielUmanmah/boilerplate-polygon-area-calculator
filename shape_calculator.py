class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        combo = str(self.width) +' '+ str(self.height)
        return combo

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50: return 'Too big for picture.'

        str = ''
        for i in range(self.height):
            str+='*'+'{}'.format('*'*(self.width-1)) + '\n'
        return str

    def get_amount_inside(self, shape):
        self = repr(self).split(' ')
        shape = repr(shape).split(' ')

        containerWidth = int(self[0])
        containerHeight = int(self[1])
        shapeWidth = int(shape[0])
        shapeHeight = int(shape[1])
        fits = 0

        while containerHeight >= shapeHeight:

            while containerWidth >= shapeWidth:
                fits+=1
                containerWidth-=shapeWidth

            containerHeight-=shapeHeight
            containerWidth = int(self[0])
        return fits

class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)