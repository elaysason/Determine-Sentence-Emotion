# Determine-Sentence-Emotion


Detrimane the emotion of a tweet using deep learning.
1. [General](#General)
    - [Background](#background)
3. [Program Structure](#Program-Structure)
    - [Network Structure](#Network-Structure)
5. [Installation](#Installation)

## General
The goal is to use deep learning and recurrent neural networks in particular to predict to emotion of a tweet. We used LSTM model to comply with that goal.
### Background
LSTM is an advanced kind of recurrent neural network capable of handling long-term dependencies and information

<img src="https://i.imgur.com/xt19dlR.png" width = 70% height=70%>

where the following definitions hold:


<img src="https://i.imgur.com/fYGPU7A.png" width = 70% height=70%>


## Program Structure
* model.py - Creation of the network and evlautes its performance and visualize on the test set. The first part is cleaning the data and embbining it to the apporiate space. The rest is the definition of the network and visualiztion.
* predict.py - Uses the model created to, given a path to new pictures outputs a csv file with the prections of the new tweets.

### Network-Structure
- After loading and preprocessing the data, the first action was embedding it using 
embedding dim of 64.  

- Next, preforming 4 layers of LSTM with hidden size of 64. Between the layers, a 10% 
dropout was selected. 

- Then again, dropping out 10% as a regularization before performing the fully 
connected layer. 

- Finally, using a fully connected network with 3 linear layers and relu as an activation 
function. 

- The last layer of the fully connected, is the classifier. It classifies the data to 3 classes 
 The places in the prediction's array is 0,1 and 2 respectively which reprenets sadness,natural and happiness.

 

## Installation
1. Open the terminal

2. Clone the project by:
```
    $ git clone https://github.com/elaysason/Determine-Sentence-Emotion.git
```
3. Run the predict.py file by:
```
    $ python predict.py /path/to/folder
```
