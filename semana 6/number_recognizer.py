import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


mnist = tf.keras.datasets.mnist  # Object of the MNIST dataset
(x_train, y_train),(x_test, y_test) = mnist.load_data()  # Load data
plt.imshow(x_train[0], cmap="gray")  # Import the image
plt.show()  # Plot the image

# Normalize the train dataset
x_train = tf.keras.utils.normalize(x_train, axis=1)
# Normalize the test dataset
x_test = tf.keras.utils.normalize(x_test, axis=1)

#Build the model object
model = tf.keras.models.Sequential()
# Add the Flatten Layer
model.add(tf.keras.layers.Flatten())
# Build the input and the hidden layers
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
# Build the output layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x=x_train, y=y_train, epochs=5) # Start training process

# Evaluate the model performance
test_loss, test_acc = model.evaluate(x=x_test, y=y_test)
print('\nTest accuracy:', test_acc)     # Presición con la que trabaja el algoritmo

# Hace una predicción de acuerdo al modelo entrenado
# Selecciona la imagen número 1000 del banco de impagene spara hacer la prueba
predictions = model.predict([x_test])  # Hace la predicción
print(np.argmax(predictions[1000]))    # Imprime el número identificado

plt.imshow(x_test[1000], cmap="gray")  # Muestra la imagen la imagen del banco de imágenes
plt.show()                             # para asegurarse que el algoritmo funciona