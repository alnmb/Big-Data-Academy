
def prompt():

    while True:
        print("Hi!\nI will calculate the perimeter of a polygon\n")
        response = int(input("\nPlease press \n1 for triangle\n2 for square\n3 for quit\n"))

        try:
            if response == 1:

                perimeter("triangle")
            
            elif response == 2:
                
                perimeter("square")
                
            elif response == 3:
                break
        
        except:
            print("Please provide valid character")

def perimeter(polygon):

    if polygon == "triangle":
        side1 = int(input("Side 1: "))
        side2 = int(input("Side 2: "))
        side3 = int(input("Side 3: "))

        perimeter = side1 + side2 + side3
        print('The perimeter is: ', perimeter)

        area = (side1 * side2) / 2
        print("The area is: ", str(area))

    elif polygon == "square":
        side1 = int(input("Side 1: "))

        perimeter = side1 * 4
        print('The perimeter is: ', perimeter)

        area = side1 ** 2
        print("The area is: ",str(area))

bla = prompt()


