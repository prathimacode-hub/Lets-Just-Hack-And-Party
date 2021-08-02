
import tensorflow as tf
# Load and prepare the MNIST dataset. Convert the samples from integers to floating-point numbers:


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the tf.keras.Sequential model by stacking layers. Choose an optimizer and loss function for training:
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# For each example the model returns a vector of "logits" or "log-odds" scores, one for each class.
predictions = model(x_train[:1]).numpy()
predictions

# array([[ 8.1478250e-01, -4.9710822e-01, -4.4540316e-04,  8.0338269e-02,
#         -1.2498328e-01, -2.8269893e-01,  4.8158792e-01, -2.3113336e-01,
#         -6.4444810e-02,  2.9273060e-01]], dtype=float32)
# The tf.nn.softmax function converts these logits to "probabilities" for each class:


tf.nn.softmax(predictions).numpy()

# array([[0.2003022 , 0.05394346, 0.08864142, 0.09609938, 0.07826194,
#         0.06684294, 0.14354272, 0.07038016, 0.08314615, 0.11883967]],
#       dtype=float32)

# Note: It is possible to bake this tf.nn.softmax in as the activation function for the last layer of the network. While this can make the model output more directly interpretable, this approach is discouraged as it's impossible to provide an exact and numerically stable loss calculation for all models when using a softmax output.
# The losses.SparseCategoricalCrossentropy loss takes a vector of logits and a True index and returns a scalar loss for each example.


loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# This loss is equal to the negative log probability of the true class: It is zero if the model is sure of the correct class.

# This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to -tf.math.log(1/10) ~= 2.3.


loss_fn(y_train[:1], predictions).numpy()

# 2.7054095

model.compile(optimizer='adam',
            loss=loss_fn,
            metrics=['accuracy'])

# The Model.fit method adjusts the model parameters to minimize the loss:
model.fit(x_train, y_train, epochs=5)

# Epoch 1/5
# 1875/1875 [==============================] - 3s 1ms/step - loss: 0.2913 - accuracy: 0.9147
# Epoch 2/5
# 1875/1875 [==============================] - 3s 1ms/step - loss: 0.1418 - accuracy: 0.9584
# Epoch 3/5
# 1875/1875 [==============================] - 3s 1ms/step - loss: 0.1058 - accuracy: 0.9681
# Epoch 4/5
# 1875/1875 [==============================] - 3s 1ms/step - loss: 0.0879 - accuracy: 0.9730
# Epoch 5/5
# 1875/1875 [==============================] - 3s 1ms/step - loss: 0.0744 - accuracy: 0.9765
# <tensorflow.python.keras.callbacks.History at 0x7fc99a051290>
# The Model.evaluate method checks the models performance, usually on a "Validation-set" or "Test-set".

model.evaluate(x_test,  y_test, verbose=2)
