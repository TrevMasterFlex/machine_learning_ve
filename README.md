# machine_learning_ve

Data pre-processing:
Data is taken from the Caltech-UCSD Birds 200 dataset.
The partition_data.py program does 6 things:
- Directory creation (for the cnn)
- Filtering (based on four classifications: wren, warbler, vireo, and sparrow)
- Resizing images (to standardize them)
- Padding images
- Downsizing images
- Copying them to the created data structure from the Caltech-UCSD Birds 200 dataset
It first sets up folders to house data in a form the cnn can use. 
This includes a folder for training, validation, and testing.
Additionally, each bird classification type needs a folder in each of these data type folders.
The program begins populating these class subfolders within each data type folder once the directory structure is built.
Only birds of the following types are copied from the Caltech-UCSD Birds 200 dataset to these subfolders: wren, warbler, vireo, or sparrow.
The filtering process looks for instances of these bird types within the Caltech-UCSD Birds 200 dataset folder name after each letter is made lowercase for simplified matching.
Once a candidate image passes this filtering process it is resized to the largest dimension among all images of interest, while retaining its aspect ratio.
If, after this resizing, it still does not conform to the standardized maximum dimension, the shorter dimension is then padded.

Network Architecture:
A cnn, or convolutional neural network was chosen for this project's network architecture. 
They are commonly used for analyzing visual imagery and image classification. 
Examples of their application include self driving cars and facebook's photo tagging. 
They are also a fast and efficient solution for image classification. 
The CNN has Convolutional layers, ReLu layers, Pooling layers, and a Fully connected layer.