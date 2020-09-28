from tello_edu_py.fly_tello import FlyTello

my_tellos = ["sn"]





with FlyTello(my_tellos) as fly:
    fly.takeoff()

