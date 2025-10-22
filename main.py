import numpy as np
import pandas as pd

def arithmeticOperations(a, b):
    

    #add array a with array b
    add=a+b
    print("Addition Result:")
    for i in range(len(add)):
        print(f"{a[i]} + {b[i]} = {add[i]}")

    #subtract array a from array b
    sub = a-b
    print("\nSubtraction Result:")
    for i in range(len(sub)):
        print(f"{a[i]} - {b[i]} = {sub[i]}")

    #multiplication array a by array b
    print("\nMultiplication Result:")

    mul = a * b
    for i in range(len(sub)):
        print(f"{a[i]} * {b[i]} = {mul[i]}")

    #divide array a by array b
    print("\nDivision Result:")

    div = a / b
    for i in range(len(sub)):
        print(f"{a[i]} / {b[i]} = {div[i]}")

def aggregationOpertions(a, b):
    mean = a.mean()
    max = a.max()
    min = a.min()
    print(f"Array a {a} Mean Value: {mean}")
    print(f"Array a {a} Mximum Value: {max}")
    print(f"Array a {a} Minimum Value: {min}")
    dot = np.dot(a, b)
    print(f"Dot product of array A {a} with array B {b} = {dot}")
    reshape_A = a.reshape(5, 1)
    print(f"Array a after reshape to 5x1 =\n {reshape_A}")

def studentData():
    data = [['Alice', 20, 'A', 85],
            ['Bob', 22, 'B', 78],
            ['Charlie', 19, 'A', 92],
            ['David', 21, 'c', 65],
            ['Eva', 20, 'B', 74]]
    df = pd.DataFrame(data, columns=['Name', 'Age', 'Grade', 'Marks'])
    print('### First 3 Students ###')
    print(df.head(3))
    print('\n### Students Names and Marks ###')
    print(df[['Name', 'Marks']])
    print('\n### Students With Grade A ###')
    gradeA = df[df['Grade']=='A']
    print(gradeA)


def main():
    print("### Welcome to Task 6 and Task 7 solution ###")
    chose = int(input("Chose 1 for Task 6 Solution OR Chose 2 for Task 7 Solution: "))
    if chose == 1:
        a = np.array([10, 20, 30, 40, 50])
        b = np.array([5, 4, 3, 2, 1])
        print("####Arrya Arithemtic Operations####\n")
        arithmeticOperations(a, b)
        print("\n \n####Arrya Aggregation Operations####\n")
        aggregationOpertions(a, b)
    elif chose == 2:
        studentData()
    
    

if __name__ == '__main__':
    main()