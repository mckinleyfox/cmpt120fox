#this program calculates how long it takes a photo from Curiosity to reach Nasa
#distance is about 34 million miles
#traveling at the speed of light

def main():
    dist = eval(input("distance: "))
    speed = 186000
    time = dist / speed
    print(time, "seconds")
main()               
    
