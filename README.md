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
The padded image is then downsized for memory/time considerations.

Network Architecture:
A cnn, or convolutional neural network was chosen for this project's network architecture. 
They are commonly used for analyzing visual imagery and image classification. 
Examples of their application include self driving cars and facebook's photo tagging. 
They are also a fast and efficient solution for image classification. 
The CNN has Convolutional layers, ReLu layers, Pooling layers, and a Fully connected layer.

Evaluation Metric:
A portion of data (roughly 20%) was set aside as test data in order to judge how well the model classifies. 
This test data was not used as training or validation data. 
It was therefore unseen by the model during fitting. 
The percentage of correct classification based off this test data is a good metric by which to judge the model.
Success rate within each type of bird classification is also given in addition to overall success.

Next steps:
This project can be extended in a number of ways. All of the parameters that make up the fitting of the model and even the meta structure of the project itself (train, validate, test split for example) can be iteratively tweaked via grid search.

Summary:
The model correctly classified 107 out of 132 sparrows (81.06%)
The model correctly classified 4 out of 47 vireos (8.51%)
The model correctly classified 113 out of 147 warblers (76.87%)
The model correctly classified 11 out of 46 wrens (23.91%)
The model had an overall successful classification rate of 63.17%

Suggestions:
I would suggest Bird Trackr either collect more bird image data or look into synthetic data. Synthetic data is a great tool to supplement any machine learning pipeline. It often takes pre-existing data and alters it (while preserving the object of interest) to create additional data from which to better inform the model. Companies like ai.reverie specialise in this.