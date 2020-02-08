import numpy as np;
import numpy.linalg as npl;#Linear algebra;
import matplotlib.pyplot as plt;
#from numpy import *; Use this to avoid adding the prefix np.;

#The same as list(range(10));
'''
a = np.arange(10);
print(a);
'''

#Print all the types and the corresponding letter;
'''
for key, value in np.sctypeDict.items():
    print(key, value);
'''

#Types in np;
'''
print(np.int8(34.5));
print(np.bool(34.5));
print(np.arange(10, dtype = np.uint8));
y = np.arange(7, dtype = "u2");
print(y.itemsize);
print(y.dtype);
'''

#Creating a struct 
'''
t = np.dtype([("name", np.str_, 40), ("age", "u8"), ("math", np.uint8)]);
x = np.array([("liming", 35, 78), ("yangmi", 31, 58)], dtype = t);
print(x);
print(x[0]["name"]);
print(x[1]["math"]);
print(x["age"]);
'''

#Indexing
'''
a = np.arange(24);
b = a.reshape(2 , 3 , 4);#Alter the dimension of this array without changing itself;
print(b);
print(b[0][0][1]);
print(b[0, 0, 1]);
print("*" * 20);#Print 20 "*"s;
print(b[1, 1:2, 1:]);
print(b.shape);#Check the dimesionality of b;
c = np.copy(a);
c.shape = (3, 8);#Alter the dimension with changing itself;
print(c);
c.resize([2, 12]);#Alter the dimension with changing itself;
print(c);
d = c.ravel();
e = a.flatten();
print("*" * 20);
print(a);
print(c);
print(d);
print(e);
print("*" * 20);
print(c.transpose());
print(c);
'''

#Comnination of arrays
'''
a = np.arange(9).reshape([3, 3]);
print(a);
b = a * 2;
print(b);
c = np.hstack((a, b, a));
print(c);
d = np.concatenate((a, b, a), axis = 1);#The same as hstack;
print(d);
print("*" * 20);
e = np.vstack((a, b, a));
print(e);
f = np.concatenate((a, b, a), axis = 0);#The same as vstack;
print(f);
print("*" * 20);
print(a);
print(b);
g = np.dstack((a, b, a));#Dimension expanded, g[][][0] == a; g[][][1] ==  b; g[][][2] == a;
print(g);
print("*" * 20);
x = np.arange(9);
y = x * 2;
h = np.column_stack((x, y, x));#Combine as columns;
i = np.column_stack((a, b, a));#View the n-1 D as one D;
j = np.row_stack((x, y, x));#Combine as rows
k = np.row_stack((a, b, a));
print(h);
print(i);
print(j);
print(k);
'''

#Split of arrays;
'''
a = np.arange(24).reshape((4, 6));
print(a);
b = np.hsplit(a, 3);#Split a[][] into a[][0-2] and a[][3-5];
for x in b:
    print("*" * 20);
    print(x);
print(b);
c = np.vsplit(a, 2);#Split a[][] into a[0-1][] and [2-3][];
for x in c:
    print("*" * 20);
    print(x);
print(c);
a = np.arange(24).reshape([2, 3, 4]);
print(a);
b = np.dsplit(a, 2);#Split a[][][] into a[][][0-1] and a[][][2-3];
for x in b:
    print("*" * 20);
    print(x);
print(b);
print("*" * 20);
print(a);
b = np.split(a, 4, axis = 2);#axis == 0 -> a[x][][]; axis == 1 -> a[][x][];
print(b);
'''
#Read and save CSV file;
'''
a = np.loadtxt("iris.data", dtype = np.float64, delimiter = ',', usecols = list(range(4)));#dtype default is float
print(a);
b = np.loadtxt("iris.data", dtype = "S", delimiter = ',', usecols = [4]);
print(b);
for x in range(len(b)):
    print(a[x], "is", b[x]);
'''
#Another way
'''
t = np.dtype([('sepal_length', 'f4'),('sepal_width', 'f4'),('petal_length', 'f4'),('petal_width', 'f'),('class', 'S20')])
a = np.loadtxt("iris.data", dtype = t, delimiter = ',')
r = np.savetxt("iris.csv", a, fmt = "%03.3lf:%03.3lf:%03.3lf:%03.3lf:%s");
'''

#Math functions 1;
'''
a, b = np.loadtxt("iris.data", delimiter = ',', usecols = [0, 1], unpack = True);
#To use the a, b = np.loadtxt... form ,unpack needs to be True;
print(a);
print(b);
print(np.sqrt(a));
print("*" * 20);
y = np.random.normal(2, 0.1, 200);#Mean, standard deviation, how many;
x = list(range(200));
plt.title("Normal Distribution", fontsize = 24);
plt.plot(x, y, linewidth = 2);
plt.savefig("NormalDistribution.png");
'''

#Math function 2;
'''
a = np.arange(10);
print(a);
print(np.average(a));
print(np.mean(a));
print(np.max(a));
print(np.min(a));
print(np.ptp(a));#max - min;
print(np.std(a));#Standard deviation;
print(np.median(a));
print(np.rint(a));#round 4 5 ;
print(np.gradient(a));
'''

#Math function 3 --- Linear algebra;
'''
a = np.arange(9).reshape(3, 3);
qq, rr =npl.qr(a);
print(qq);
print(rr); 
print(qq.dot(rr));#Multiply two matrix;
b = [[1, 2], [2, 3]];
Inv = npl.inv(b);
print(Inv);
print(Inv.dot(b)); 
'''
'''
a = np.eye(5, dtype = int);#Create identity matrix;
print(a);
print(npl.matrix_rank(a));
b = np.arange(5).reshape(5, 1);
x = npl.solve(a, b);
y = np.dot(npl.inv(a), b);
z = np.matmul(npl.inv(a), b);
u = np.inner(npl.inv(a), np.transpose(b));#inner(a, b) == a*Transpose(b);
#outer(a, b) == Transpose(a)*b;
print(np.allclose(x, v));#Compare if two matrix are equal with tolerance;
'''

#Broadcasting mechanism;
'''
a = np.array([1, 2, 3]);
print(a);
print(a.shape);
print(a.ndim);
b = np.arange(0, 10).reshape(2, 5);
print(b);
print(b.shape);#[] x []
print(b.ndim);#Dimensionality
'''
'''
a = np.arange(9).reshape(3, 3);
b = np.arange(10, 19).reshape(3, 3);
print(a / b);#Calculate in corresponding position;
c = np.arange(3);
print(a + c);#When doing the broadcasting mechanism, we make copis of c;
#Two rules for broadcasting mechanism, please refer to the website;
'''

#Norms;
'''
x = np.array([1, 0, -2]);
n0 = npl.norm(x, ord = 0);#0-norm, to calculate the number of 1s;
n1 = npl.norm(x, ord = 1);#1-norm;
n2 = npl.norm(x, ord = 2);
nn = npl.norm(x, ord = np.inf);#to select the maximum(in absolute);
y =np.array([[-1, 1, 0], [-4, 3, 0], [1, 0, 2]]);
N1 = npl.norm(y, ord = 1);#For each column vector, we calculate its 1-norm, and select the maximum of them as the 1-norm of the matrix;
NN = npl.norm(y, ord = np.inf);#For each row vector, we calculate its 1-norm, and select the maximum of them as the 1-norm of the matrix;
N2 = npl.norm(y, ord = 2);
yty = np.dot(y.T, y);
print(npl.eigvals(yty), N2 * N2);#The same;2-norm;
'''

#Matrix and array;
'''
a = np.arange(12).reshape((3, 4));
b = np.arange(12).reshape((4, 3));
print(a);
print(b);
print(a * b.T, type(a));#position-wise multiply;
print("*" * 20);
print(np.matmul(a, b));#Matrix multiplization;
print("*" * 20);
x = np.matrix([[1, 3, 5], [2, 4, 6]]);
y = np.matrix("7, 9, 11; 8, 10, 12");#Another way to create a matrix;
print(x, x.shape, type(x));
print(x * y.T);#Matrix mul;
print(np.matmul(x, y.T));#Matrix mul;
print(np.multiply(x, y));#position-wise mul;
'''

#Matrix rotation;
'''
a = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]]);
print(np.rot90(a, 1));#Rotate for one time;
print(np.rot90(a, -1));
print(np.rot90(a, 3));
'''





