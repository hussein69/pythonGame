import random
import cv2

bag1 = 10
bag2 = 10
bag3 = 10
img1 = cv2.imread("you_win.jpg", 1)
img2 = cv2.imread("game_over.jpg", 1)
print(bag1, bag2, bag3)


def bags():
    global bag1, bag2, bag3
    if bagSelection == 1:
        bag1 = bag1 - objectRemove
    elif bagSelection == 2:
        bag2 = bag2 - objectRemove
    else:
        bag3 = bag3 - objectRemove


def imageShow(image, message, window_name):
    if bag1 == 0 and bag2 == 0 and bag3 == 0:
        print(message)
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


while bag1 != 0 or bag2 != 0 or bag3 != 0:
    bagSelection = int(input("Select a bag: "))
    objectRemove = int(input("Select number of objects: "))
    while bagSelection < 1 or bagSelection > 3:
        print("Please select a correct bag\n")
        bagSelection = int(input("Select a bag: "))
        objectRemove = int(input("Select number of objects: "))
    while objectRemove < 1 or objectRemove > 5:
        print("Please enter a valid number\n")
        bagSelection = int(input("Select a bag: "))
        objectRemove = int(input("Select number of objects: "))
    while (
        (bagSelection == 1 and bag1 == 0)
        or (bagSelection == 2 and bag2 == 0)
        or (bagSelection == 3 and bag3 == 0)
    ):
        print("You can't remove this number\n")
        bagSelection = int(input("Select a number: "))
        objectRemove = int(input("Select number of objects: "))

    while bagSelection == 1 and (objectRemove > bag1 and bag1 > 0):
        print("Please enter a valid number\n")
        bagSelection = int(input("Select a number: "))
        objectRemove = int(input("Select number of objects: "))
    while bagSelection == 2 and (objectRemove > bag2 and bag2 > 0):
        print("Please enter a valid number\n")
        bagSelection = int(input("Select a number: "))
        objectRemove = int(input("Select number of objects: "))
    while bagSelection == 3 and (objectRemove > bag3 and bag3 > 0):
        print("Please enter a valid number\n")
        bagSelection = int(input("Select a number: "))
        objectRemove = int(input("Select number of objects: "))

    bags()

    print("You took:", objectRemove, "objects from bag:", bagSelection)

    print(bag1, bag2, bag3, "\n")

    imageShow(img1, "Congrats you won!", "YOU WIN!")

    bagSelection = random.randint(1, 3)
    objectRemove = random.randint(1, 5)
    while (
        (bagSelection == 1 and bag1 == 0)
        or (bagSelection == 2 and bag2 == 0)
        or (bagSelection == 3 and bag3 == 0)
    ):
        bagSelection = random.randint(1, 3)
    while bagSelection == 1 and (objectRemove > bag1 and bag1 > 0):
        objectRemove = random.randint(1, 5)
    while bagSelection == 2 and (objectRemove > bag2 and bag2 > 0):
        objectRemove = random.randint(1, 5)
    while bagSelection == 3 and (objectRemove > bag3 and bag3 > 0):
        objectRemove = random.randint(1, 5)

    bags()

    print("Computer took:", objectRemove, "objects from bag:", bagSelection)
    print(bag1, bag2, bag3, "\n")
    imageShow(img2, "you lost.", "GAME OVER!")
