class User_Room_Detail:
    def __init__(self,length,width,height,area,gallon,price):
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)
        self.area = float(area)
        self.gallon = float(gallon)
        self.price = float(price)
    def computeRoomArea(self):
        room_shape = input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom (more or less than 4 walls, all square or rectangles)\n")
        area = User_Room_Detail(0,0,0,0,0,0)
        if room_shape == '1':
            room_area = float(area.computeRectangleWallsArea())
        elif room_shape == '2':
            room_area = float(area.computeSquareWallsArea())
        elif room_shape == '3':
            room_area = float(area.computeCustomWallsArea())
        window_area = float(area.computeWindowsDoorsArea())
        self.area = room_area - window_area
        paint = User_Room_Detail(0,0,0,self.area,0,0)
        self.gallon = float(paint.computeGallons())
        price_paint = paint.computePaintPrice(self.gallon)
        self.price = float(price_paint)
    def calculateRectangleArea(self):
        area = 2*(self.length*self.height) + 2*(self.height*self.width)
        return area
    def computeRectangleWallsArea(self):
        room_length = input("Enter the length of the room in feet:\n")
        room_width =input("Enter the width of the room in feet:\n")
        room_height = input("Enter the height of the room in feet:\n")
        further = User_Room_Detail(room_length,room_width,room_height,0,0,0)
        area_surface = further.calculateRectangleArea()
        return area_surface
    def computeSquareArea(self):
        area = 4*(self.length**2)
        return area
    def computeSquareWallsArea(self):
        room_length = float(input("Enter the length of one side of the room: \n"))
        total_area = User_Room_Detail(room_length,0,0,0,0,0)
        square_area = total_area.computeSquareArea()
        return square_area
    def computeCustomWallsArea(self):
        nbr_room = int(input("How many walls are there in the room\n"))
        total_area = 0
        for a in range(1,nbr_room+1):
            height = float(input(f'Enter the height of wall {a} in feet\n'))
            length = float(input(f'Enter the length of wall {a} in feet\n'))
            total_area += (height*length)
        return total_area
    def computeWindowsDoorsArea(self):
        window_nmbr = int(input("How many windows and doors does the room contain? \n"))
        total_area = 0
        for b in range(1,window_nmbr+1):
            window_length = float(input(f'Enter window/door length for window/door {b} in feet\n'))
            window_width = float(input(f'Enter window/door width for window/door {b} in feet\n'))
            total_area += (window_length * window_width)
        return total_area
    def computeGallons(self):
        gallon = self.area / 350
        return gallon 
    def computePaintPrice(self,gallon):
        price = (gallon * 42)
        return price
print("Welcome to Shiny Paint Company for indoor painting!\n")
room_number = input("How many Rooms do you want to paint:\n")
if room_number.isdigit():
    room_nbr = int(room_number)
    print("Thank you!\n")
    for a in range(1,room_nbr+1):
        print(f'Room: {a}')
        result = User_Room_Detail(0,0,0,0,0,0)
        result.computeRoomArea()
        print(f'For Room: {a}, the area to be painted is {result.area:.1f} square ft and will require {result.gallon:.2f} gallons to paint. This will cost the customer ${result.price:.2f}')
else:
    print("Invalid input! \nTry again")