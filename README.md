# Prediction_of_lung_cancer_and_breast_Cancer_using_K_Nearest_Neighbour_Algorithm

Introduction :
The Objective of the project is to implement the K- Nearest Neighbour Algorithm(Classification/Supervised Learning). 
For this implementation, the two datasets from Kaggle were taken and EDA (Exploratory Data Analysis) was done by using 
Data Visualisation in which several plots such as ScatterPlots, Swarm plots, Box plots, Violin plots, Bar plots and the 
heatPlot were drawn to collect the Information from the tabulated data. After the data being studied visually the 
algorithm is then programmed using the python language for the chosen dataset. The results (prediction value and the 
actual value) were displayed along with the accuracy of the algorithm.

Classification:
Machine Learning algorithms is primarily classified into 3 categories namely 
(i) Supervised learning
(ii) Unsupervised learning 
(iii) Reinforcement learning
The Supervised learning method otherwise called as Classification problems is used to classify (or) 
predict the results based on the dataset. The classification problem usually has a discrete values and 
here the dataset is split into training datasets and testing dataset. The probability of data goes for 
training is usually large comparatively to the testing, because in order for the algorithm to predict with
more accuracy it needs a Chunk of data to train itself. That is why mostly 70% of data goes for training and 
30% goes for testing.

In realtime the Classification algorithm is used for 
(i) Speech recognition and Facial recognition 
(ii) Bio-metric identification.
(iii) Cancer cells prediction
(iv) E-mail spam classification

There are several classification algorithms such as 
a. Naive Bayes classification
b. Support Vector Machines
c. Decision Tree
d. K Nearest Neighbour 
e. Random Forest

These algorithms are used based on the type of result and on the dataset being chosen.
K Nearest Neighbour (KNN) Algorithm:
As the name ‘Nearest’ implies, this algorithm predicts the output based on the distance between the 
two points. Usually KNN can be used for both classification and the regression predictive purpose but 
primarily it is used for the classification as it given better results when comparing with the nearest 
labels through distance. Here, the training data is used at the time of testing phase and the calculation 
time is comparatively low to other classification algorithms. The euclidean distances are calculated between 
the value to be predicted and the plotted testDataset values. Through this the algorithm determines the nearest 
neighbour of the instances.

Pseudocode - Implementation
Implementation of KNN algirithm:
1. Load the data
2. Initialise the value of k (‘k' determines the number of points to be compared with)
3. For getting the predicted class, iterate from 1 to total number of training data
points
		1. Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc.
		2. Sort the calculated distances in ascending order based on distance values
		3. Get top k rows from the sorted array
		4. Get the most frequent class of these rows
		5. Return the predicted class
