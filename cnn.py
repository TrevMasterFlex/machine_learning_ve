# This program predicts what type of bird is in an image.

# Import packages this program uses
import os
import numpy as np
from PIL import Image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

# Parameters
epochs = 1
filters = 9
batch_size = 32
validation_steps = 2000
steps_per_epoch_numerator = 8000
shear_range = .2
zoom_range = .2

test_path = "test_set/"

classifications = [classification for classification in os.listdir(test_path) if not classification.startswith('.')]
number_of_classifications = len(classifications)
# Get the standardized width and height
first_class_test_path = test_path + classifications[0]
file_path = first_class_test_path + "/" + os.listdir(first_class_test_path)[0]
im = Image.open(file_path)
width, height = im.size

# Initialising the CNN
classifier = Sequential()

# Convolution
# Make 32 feature detectors with a size of 3x3   CHANGE 32!!!!!
# Choose the input-image's format to be 500x500 with 3 channels
classifier.add(Conv2D(filters, (3, 3), input_shape=(width, height, 3), activation="relu"))

# Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(filters, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Flattening
classifier.add(Flatten())

classifier.add(Dense(activation="relu", units=width))
classifier.add(Dense(activation="softmax", units=number_of_classifications))

# Compiling the CNN
classifier.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Color values within each pixel of the image are between 0 and 255
# We need to rescale this to between 0 and 1
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = shear_range, zoom_range = zoom_range, horizontal_flip = True)
validation_datagen = ImageDataGenerator(rescale = 1./255)

# Prepare training data
training_data = train_datagen.flow_from_directory('training_set', target_size = (width, height), batch_size = batch_size, class_mode = 'categorical')

# Prepare Validation data
validation_data = validation_datagen.flow_from_directory('validation_set', target_size = (width, height), batch_size = batch_size, class_mode = 'categorical')

# Computation
classifier.fit_generator(training_data, steps_per_epoch = (steps_per_epoch_numerator / batch_size), epochs = epochs, validation_data = validation_data, validation_steps = validation_steps)

# Make predictions using the thus far unused test set to evaluate the model's performance
test_image = image.load_img('test_set/sparrow/Baird_Sparrow_0002_2537220789.jpg', target_size = (width, height))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
print(result)

def predict_classification(img_path):
    test_image = image.load_img(img_path, target_size = (width, height))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    for i in range(number_of_classifications):
        if result[0][i]: #==1
            return classifications[i]

for classification in classifications:





# # Training data class indices
# if result[0][0] == 1:
#     prediction = 'sparrow'
# elif result[0][1] == 1:
#     prediction = 'vireo'
# elif result[0][2] == 1:
#     prediction = 'warbler'
# elif result[0][3] == 1:
#     prediction = 'wren'

# print(prediction)
