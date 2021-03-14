# def calculate(n, **kwards):
#     print(kwards)
#     print(type(kwards))
#     for key, value in kwards.items():
#         print(key)
#
#     print(kwards["add"])
#     print(n)
#     n += kwards["add"]
#     n *= kwards["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)
#

class Car:
    def __init__(self, **kw):
        self.color = kw["color"]
        self.model = kw["model"]  # return error if the parameter is misspell

car = Car(color="red", model="vw")

# --
class Car2:
    def __init__(self, **kw):
        self.color = kw.get("color")
        self.model = kw.get("model")  # return null if the parameter is misspell

car2 = Car2(color="red", model="vw")
