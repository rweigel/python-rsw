import tensorflow as tf

# Use CPU by setting GPU to empty list

# On Mac M3 Max (16 CPU cores, 128 GB RAM and 40 GPU cores) and TensorFlow 2.18.0
#   CPU is ~600 ms/step but starts faster
#   GPU is ~400 ms/step
# On JHU/APL's mollie RedHat AMD Epic 7262 (8 CPU cores, 32 GB RAM) with TensorFlow 2.13.1
#   CPU is ~1500 ms/step
#   GPU - was not able to run

#Default is CPU
#tf.config.set_visible_devices([], "GPU")

cifar = tf.keras.datasets.cifar100
(x_train, y_train), (x_test, y_test) = cifar.load_data()
model = tf.keras.applications.ResNet50(
    include_top=True,
    weights=None,
    input_shape=(32, 32, 3),
    classes=100,)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64)
