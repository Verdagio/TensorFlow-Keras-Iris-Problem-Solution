import csv
import numpy as np
import keras as kr

#load the Iris dataset
iris = list(csv.reader(open("IRIS.csv")))[1:]

# 4 inputs sepal length & width, petal length & width
inputs = np.array(iris)[:,:4].astype(np.float)

# outputs are initially strings , setosa, versicolor, virginica
outputs = np.array(iris)[:,4]

#convert the out strings to ints
output_val, output_ints = np.unique(outputs, return_inverse=True)

# endocde the category integers as binary categorial vairables.
output_cats = kr.utils.to_categorical(output_ints)

# split the input & output data sets into training and test subsets
inds = np.random.permutation(len(inputs))

train_inds, test_inds = np.array_split(inds, 2)

input_train, outputs_train = inputs[train_inds], output_cats[train_inds]
input_test, output_test = inputs[test_inds], output_cats[test_inds]

#creats a neral network
model = kr.models.Sequential()

# add an initial layer with 4 inputs nodes, and a hidden layer wiht 16 nodes
model.add(kr.layers.Dense(16, input_shape=(4,)))

#appy the signoid activation function to that layer
model.add(kr.layers.Activation("sigmoid"))

#add another layer connected to the layet with 16 nodes containing 3 output nodes
model.add(kr.layers.Dense(3))

#use the softmax activation function there
model.add(kr.layers.Activation("softmax"))

# configure the model for training
# uses the adam optimizer and categorialcross entropy as the loss function
# add in some extra metrics, accuracy being the only one.
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

#fit the model using our training data
model.fit(input_train, outputs_train, epochs=100, batch_size=1, verbose=1)

#evaluate the model using the test data set
loss, accuracy = model.evaluate(input_test, output_test, verbose=1)


print("\n\nloss: %6.4f\nAccuracy: %6.4f"% (loss, accuracy))

prediction = np.around(model.predict(np.expand_dims(input_test[0], axis=0))).astype(np.int)[0]
print("actual: %4.f\testimated: %s"  %(output_test[0].astype(np.int), prediction))
print("that means it is a %s" % output_val[prediction.astype(np.bool)][0])

model.save('iris-nn.h5')