import numpy as np

input1 = np.array([[1], [1], [1], [1], 
                   [-1], [-1], [1], [1], [1], [1], [-1], [-1], [1], [1], [1]])

input2 = np.array([[1], [1], [1], [1],
                   [1], [1], [1], [-1],
                   [-1], [1], [-1], [-1],
                   [1], [-1], [-1]])

target1 = np.array([[-1, 1]])
target2 = np.array([[1, 1]])

w1 = np.dot(input1, target1)
w2 = np.dot(input2, target2)

w = w1 + w2

y_in = np.dot(input1.T, w)
print("y_in:", y_in)

def signum(y_in):
    y = []
    for i in y_in[0]:
        if i == 0:
            y.append(0)
        elif i < 0:
            y.append(-1)
        else:
            y.append(1)
    return np.array(y)

y = signum(y_in)
print("y:", y)

def tester1(y, target1):
    if np.array_equal(y, target1.flatten()):  
        print("test passed")
    else:
        print("test failed")

def tester2(y, target2):
    if np.array_equal(y, target2.flatten()):  
        print("test passed")
    else:
        print("test failed")

tester1(y, target1)

# tester2(y, target2)
