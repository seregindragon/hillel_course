def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {} and I'm {} years old".format(name, age)



if __name__ == "__main__":
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
    assert say_hi("Sergey", 35) == 'Hi. My name is Sergey and I\'m 35 years old'
    print('ОК')
