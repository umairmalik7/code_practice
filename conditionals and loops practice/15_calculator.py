class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        #code here
        if operator == 1:
            add = a + b
            print(add,end="")
        elif operator == 2:
            sub = b -a
            print(sub,end="")
        elif operator == 3:
            multiple = a * b
            print(multiple,end="")
        else:
            print("Invalid Input")