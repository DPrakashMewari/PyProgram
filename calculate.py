# Python Program to find Area of Particular Property

class Property:
	def __init__(self,width,length):
		self.width = width
		self.length = length
	def calculatearea(self):
		area = self.length * self.width
		return f" The area is:- {area}" 

def main():
    # In real State 
    bathroom = Property(int(input("Enter width")),int(input("Enter length")))
    bedroom = Property(int(input("Enter width")),int(input("Enter length")))
    print("\n")
    print("bathroom area will be: ",bathroom.calculatearea())
    print("bedroom area will be :",bedroom.calculatearea())




if __name__ == '__main__':
	main()