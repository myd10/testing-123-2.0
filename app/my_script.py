#testing-123.20/my_script.py

def enlarge(i):
    return i *100


#need to remove from global scope for test

if __name__ == "__main__":
    my_number = float(input("Please input a number:"))
    n = enlarge(my_number)
    print("Enlarging the number:", n)
