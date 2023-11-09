# In order to run this program WITHOUT A FLAW you need to install the matplotlib library and the flask library!! Also you need to create a folder named templates and save the HTML file there. Plus, you need to READ all the comments to help you understand the full function of the code.
# run the code "pip install matplotlib" on your command prompt or in your terminal to install the matplotlib library
# run the code "pip install flask" on your command prompt or in your terminal to install the flask library


import matplotlib.pyplot as plt #importing a library that plots coordinate points
from mpl_toolkits.mplot3d import Axes3D #importing the 3D plotter from the library as our vectors are 3D
import os #importing a routine to make it portable between different paths
from flask import Flask, request, render_template # flask is a program that enables us to run our Python code as an app between two different languages: Python & HTML
vector = Flask(__name__) #assigning a variable to be run as an app
@vector.route('/')#Decorate the view function to register it with the given URL
def index():
    return render_template('vectorsource.html') #when this function is called it returns the html file as an output or display
def vectorize():#defining a function that may come in handy in progressive calculations
    vector1 = int(request.form['vector1'])#i-component of the first vector
    vector2 = int(request.form['vector2'])#j-component of the first vector
    vector3 = int(request.form['vector3'])#k-component of the first vector
    vector4 = int(request.form['vector4'])#i-component of the second vector
    vector5 = int(request.form['vector5'])#j-component of the second vector
    vector6 = int(request.form['vector6'])#k-component of the second vector
    vector7=vector2*vector6
    vector8=vector3*vector5
    vector9=-(vector1*vector6)
    vector10=vector3*vector4
    vector11=vector1*vector5
    vector12=vector2*vector4
    vectorize=(vector7-vector8,vector9+vector10, vector11-vector12)#definition of a vector product
    return vectorize
@vector.route('/calculate-vectors', methods=['POST'])#routes to the URL calculate-vectors
def calculate_vectors():
    vector1 = int(request.form['vector1'])#i-component of the first vector
    vector2 = int(request.form['vector2'])#j-component of the first vector
    vector3 = int(request.form['vector3'])#k-component of the first vector
    vector4 = int(request.form['vector4'])#i-component of the second vector
    vector5 = int(request.form['vector5'])#j-component of the second vector
    vector6 = int(request.form['vector6'])#k-component of the second vector
    choice_1 = request.form['choice_1']#traces back what the user chose
    vector7=vector2*vector6
    vector8=vector3*vector5
    vector9=-(vector1*vector6)
    vector10=vector3*vector4
    vector11=vector1*vector5
    vector12=vector2*vector4
    if choice_1 == "sum":
        vector_sumation = (vector1 + vector4, vector2 + vector5, vector3 + vector6)#vector addition
        resultant = f'Vector Sum: {vector_sumation}'
        vectorimgdata = vector_sumation
    elif choice_1=="scalar product":
        scalar_product = vector1 * vector4+vector2 * vector5+ vector3 * vector6 #scalar product definition
        resultant = f'Scalar Product: {scalar_product}'
    else:
        vector_product =(vector7-vector8,vector9+vector10, vector11-vector12)#using simple matrix
        resultant = f'Vector Product: {vector_product}'
        vectorimgdata = vector_product#assigning the coordinates of the resulatnat so that it can be plotted
  
    img = plt.figure()# assigning a variable on which the plotting is going to be performed
    graph = img.add_subplot(111, projection='3d')# describing the rows and projection of the graph generated from the image
    graph.quiver(0, 0, 0, vectorimgdata[0], vectorimgdata[1], vectorimgdata[2], color="red" if choice_1 == "sum" else "blue")#giving the graph properties that can distinguish it from the other in the same plot
    graph.set_xlim([min(vectorimgdata), max(vectorimgdata)])#setting the maximum number assigned to the x axis
    graph.set_ylim([min(vectorimgdata), max(vectorimgdata)])#setting the maximum number assigned to the y axis
    graph.set_zlim([min(vectorimgdata), max(vectorimgdata)])#setting the maximum number assigned to the z axis
    graph.set_xlabel("X-Axis")#labelling
    graph.set_ylabel("Y-Axis")
    graph.set_zlabel("Z-Axis")
    graph.text2D(0.05, 0.95, resultant, transform=graph.transAxes) #graph properties
    plt.show()#shows the graph of the vector in an interactive way 

    vectorimg = 'static/vectorimg.png'#returns the images created by the plt as image files
    plt.savefig(vectorimg)#saves the image to the static folder
    return f'<center><h1>{resultant}</h1><img src="{vectorimg}"></center><br>'#the return value of the function
    

if __name__ == '__main__':#if the assigned name above is the app being run, it checks whether there is any static named folder created to store the images created, if there is not, it will create one
    if not os.path.exists('static'):#if there is no path by the name 'static'
        os.makedirs('static')#make a path by the name'static'
    vector.run(debug=True, port=5000, host='0.0.0.0')#it runs the app finally by enabling debugging
