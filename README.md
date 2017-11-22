# Tensorflow problem sheet solution

## Introduction
The following is a 4th year in-class assignment for Emerging technologies. These problems relate to the Python package Tensorflow & Keras. We will use the famous iris data set, & using Jupyter notebook to build a visual representation of the data.

### What is the IRIS data set?

The IRIS data set consists of 50 samples from each of 3 species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

For more info see : [IRIS](https://archive.ics.uci.edu/ml/datasets/iris)

### What are Tensorflow & Keras?

###### [Tensorflow](https://www.tensorflow.org/)

TensorFlow™ is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API.

###### [Keras](https://keras.io/)

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

Use Keras if you need a deep learning library that:

1. Allows for easy and fast prototyping (through user friendliness, modularity, and extensibility).
2. Supports both convolutional networks and recurrent networks, as well as combinations of the two.
3. Runs seamlessly on CPU and GPU.
4. Read the documentation at Keras.io.

Keras is compatible with: Python 2.7-3.6.

## Getting started

To be able to run these scripts we have a bit of setup to do first. Firstly we will need to have python installed you can get it here:

[Python](https://www.python.org/downloads/)

Once the download & installation of Python is finished we are ready to go!

You might need to install some dependencies.

Open a CMD / Terminal window on your system and type in the following:

##### Installing Jupyter Notebook

First, ensure that you have the latest pip; older versions may have trouble with some dependencies:

```pip3 install --upgrade pip```

Then install the Jupyter Notebook using:

```pip3 install jupyter```

For more informaton about Jupyter Notebook, you can find it [HERE](http://jupyter.org/install.html)

##### Install Tensorflow

To install TensorFlow, start a terminal. Then issue the appropriate pip3 install command in that terminal. To install the CPU-only version of TensorFlow, enter the following command:

```pip3 install --upgrade tensorflow```

To install the GPU version of TensorFlow, enter the following command:

```pip3 install --upgrade tensorflow-gpu```

For more informaton about Tensorflow installation, you can find it [HERE](https://www.tensorflow.org/install/install_windows)


##### Other dependencies

1. Numpy -> ```pip install numpy```
2. Keras -> ```pip install keras```
3. h5py -> ```pip install h5py```

##### Running the program

With that out of the way we can go to the directory of the project

```cd path/to/directory```

Once in the project directory we will use the following commands to run the scripts

To run the python prototype script: 

```python prototype.py```

This will run the program from our Command line / terminal, otherwise we can use Jupyter Notebook

##### Run in Jupyter Notebook

We can view this using Jupyter Notebook

First:

```cd path/to/directory```

Then:

```jupyter notebook```

This will open a webpage where you can then view the tensor.ipynb file

## Assignment Specification

### 1. Use Tensorflow to create model

Use Tensorflow to create a model to predict the species of Iris from a flower’s sepal width, sepal length, petal width, and petal length.

### 2. Split the data into training and testing

Split the data set into a training set and a testing set. You should investigate the best way to do this, and list any online references used in your notebook. If you wish to, you can write some code to randomly separate the data on the fly.

### 3. Train the model

Use the testing set to train your model.

### 4. Test the model

Use the testing set to test your model, clearly calculating and displaying the error rate.