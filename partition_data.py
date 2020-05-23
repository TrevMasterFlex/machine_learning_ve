# This program creates the training, validation, and test set folders. 
# It then populates these three set-folders with four bird-type-folders.
# The four bird types of interest are sparrows, vireos, warblers, and wrens.
# All image data is taken from the Caltech-UCSD Birds 200 dataset.
# All image data is padded to a standard size.

# Import packages this program uses
import os
import shutil
import random
from PIL import Image, ImageOps

# What to shrink the image size to
downsize = 128, 128

img_dir = 'images/'

# Data partition percentages
data_sets = [{"dir": "training_set/", "percent": .6}, {"dir": "validation_set/", "percent": .2}, {"dir": "test_set/", "percent": .2}]

# This will be used to create the sub folders within each data set as well as filter the Caltech-UCSD Birds 200 dataset
classifications = ['wren', 'warbler', 'vireo', 'sparrow']

# Throw an error if the sum of the data partition ratios does not equal 1
if sum(data_set["percent"] for data_set in data_sets) != 1:
	raise ValueError('Data partition ratios must equal 1')

# Iterate over the data sets, creating four classification folders within each (wren, warbler, vireo, and sparrow)
for data_set in data_sets:
	data_type_dir_name = data_set["dir"]
	if os.path.isdir(data_type_dir_name):
		shutil.rmtree(data_type_dir_name)
	os.mkdir(data_type_dir_name)
	for classification in classifications:
		class_folder = data_type_dir_name + "/" + classification
		if not os.path.isdir(class_folder):
			os.mkdir(class_folder)

# Get the max width and height among the images of interest
max_height = 0
max_width = 0

for class_directory in os.listdir(img_dir):
	class_found = False
	class_index = 0
	number_of_classifications = len(classifications)
	while not class_found and class_index < number_of_classifications:
		classification = classifications[class_index]
		# Check that the folder contains a substring that matches one of the four classifications of interest (wren, warbler, vireo, or sparrow)
		# Make everything lowercase for simplified matching
		if classification in class_directory.lower():
			class_found = True
			class_path = img_dir + class_directory
			# Iterate over all files within a bird classification folder
			for file_name in os.listdir(class_path):
				file_path = class_path + "/" + file_name
				im = Image.open(file_path)
				width, height = im.size
				if width > max_width:
					# A new maximum width has been found, update
					max_width = width
				if height > max_height:
					# A new maximum height has been found, update
					max_height = height
		else:
			class_index+=1

max_dimension = max(max_height, max_width)

# Resize the images to the maximum possible while retaining the aspect ratio
# Then pad to the maximum dimensions found among the images of interest
for class_directory in os.listdir(img_dir):
	class_found = False
	class_index = 0
	number_of_classifications = len(classifications)
	while not class_found and class_index < number_of_classifications:
		classification = classifications[class_index]
		# Check that the folder contains a substring that matches one of the four classifications of interest (wren, warbler, vireo, or sparrow)
		# Make everything lowercase for simplified matching
		if classification in class_directory.lower():
			class_found = True
			class_path = img_dir + class_directory
			# Iterate over all files within a bird classification folder
			for file_name in os.listdir(class_path):
				# randomly assign the images to data sets in proportion to the partition percentages of each
				random_number = random.uniform(0, 1)
				cumulative_ratio = 0
				data_set_index = 0
				data_set_found = False
				while not data_set_found:
					data_set = data_sets[data_set_index]
					cumulative_ratio += data_set["percent"]
					if random_number < cumulative_ratio:
						data_set_found = True
					else:
						data_set_index+=1
				img = Image.open(class_path + "/" + file_name)
				# Resize the image to the maximum possible, while retaining the aspect ratio
				original_size = img.size
				ratio = float(max_dimension)/max(original_size)
				new_size = tuple([int(x*ratio) for x in original_size])
				img = img.resize(new_size, Image.ANTIALIAS)
				standardized_img = Image.new("RGB", (max_dimension, max_dimension))
				standardized_img.paste(img, ((max_dimension-new_size[0])//2, (max_dimension-new_size[1])//2))
				# Determine how much padding is needed to fill the maximum dimension standard
				delta_width = max_dimension - new_size[0]
				delta_height = max_dimension - new_size[1]
				padding = (delta_width//2, delta_height//2, delta_width-(delta_width//2), delta_height-(delta_height//2))
				# Apply the padding
				padded_img = ImageOps.expand(img, padding)
				# Downsize image
				padded_img.thumbnail(downsize, Image.ANTIALIAS)
				# Save the image
				padded_img.save(data_set["dir"] + classification + "/" + file_name)
		else:
			class_index+=1
