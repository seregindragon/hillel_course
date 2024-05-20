def division(x: int,y: int):
    try:
        z =  x/y
    except ZeroDivisionError:
        print("Zero")
    else:
        print(f"Result: {z}")
    finally: #always
        print("Finally")

division(1,0)