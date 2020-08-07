from yeelight import Bulb, discover_bulbs
#bulb = Bulb("192.168.0.19") 

def main():
    print(discover_bulbs())

if __name__ == "__main__":
    main()