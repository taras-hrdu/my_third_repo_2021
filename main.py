from Lab_01 import Camera 

def main():   
    object1 = Camera("Canon", 128000)
    print(object1.__str__())
    print(f"Best camera ever: : {object1.best_camera()} \n")
    
    object2 = Camera("Nikon", 64000, 65,"Green",90,"Japan")
    print(object2.__str__())
    print(f"Best camera ever: : {object2.best_camera()} \n")

    object3 = Camera()
    print(object3.__str__())
    print(f"Best camera ever: : {object2.best_camera()} \n")

if __name__ == '__main__':
        main()
