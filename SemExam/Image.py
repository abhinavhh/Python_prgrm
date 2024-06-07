from images import Image:
def blackwhite(image):
    black=(0,0,0)
    white=(255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b)=image.getPixels(x,y)
            average=(r+g+b)//2
            if average<128:
                image.setPixel(x,y,black)
            else:
                image.setPixel(x,y,white)
def main(filename="smokey.gif"):
    image=Image(filename)
    print("Close image window to continue")
    image.draw()
    blackwhite(image)
    print("Close the image window to quit")
    image.draw()

    image.save("smokey81.gif")
if __name__=="__main__":
    main()
#Converting to gray Scale
    
def gray(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b)=image.getPixel(x,y)
            r=int(r*0.299)
            g=int(g*0.587)
            b=int(b*0.114)
            lum=r+g+b
            image.setPixel(x,y,(lum,lum,lum))
def main(filename="smokey.gif"):
    image=Image(filename)
    print("Close image window to continue")
    image.draw()
    gray(image)
    print("close image window to uit")
    image.draw()
if __name__=="__main__":
    main()