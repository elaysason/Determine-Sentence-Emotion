# Mask-Wearing-With-Deep-Learning


Detrimane the emotion of a tweet using deep learning.
1. [General](#General)
    - [Background](#background)
    - [More About The Task In Hand](#More-About-The-Task-In-Hand)
3. [Program Structure](#Program-Structure)
    - [Network Structure](#Network-Structure)
5. [Installation](#Installation)
6. [Footnote](#footnote)
## General
The goal is to use deep learning and recurrent neural networks in particular to predict to emotion of a tweet. We used LSTM model to comply with that goal.
### Background
LSTM is an advanced kind of recurrent neural network capable of handling long-term dependencies and information
<img src="https://i.imgur.com/xt19dlR.png" width = 70% height=70%>
where the following definitions hold:
<img src="https://i.imgur.com/xt19dlR.png" width = 70% height=70%>


## Program Structure
The first part is specific functions for the dataset. The second part is the implementaions of the algorithms:
* model.py - Creation of the network and evlautes its performance and visualize on the test set. 
* predict.py - Uses the model created to, given a path to new pictures outputs a csv file with the prections on those images.

### Network-Structure
The model is a 4 layers CNN that includes (on this order):  

4 layers in the following structure: 

Convolution with number of in channels is [3- RGB,16,32,64] (every i'th entry in the vector represent the in channel number of the i'th layer) and the number of out channels is [16,32,64,128] (every i'th entry in the vector represent the out channel number of the i'th layer). We can see that the in size of the i+1's layer equals the i's layer out size. 

The batches are being normalized by the size of the out channels. 

Then, it uses ReLu as an activation function and maxpooling the result with kernel of 2. 

 

drops out 80% for regularization (more about it in Regularization section). 

 

fc layer - The fully connected layer is a layer where each input is connected to all neurons. This layer helps provide and optimize the classification. 

 

Finally, the model computes log soft max. 

We saw that compared to other methods, it has the best impact on the result.  


## Installation
1. Open the terminal

2. Clone the project by:
```
    $ git clone https://github.com/elaysason/Mask-Wearing-With-Deep-Learning.git
```
3. Run the predict.py file by:
```
    $ python predict.py /path/to/folder
```
## Footnote
The folder used as an input from predcit.py should hold images in the following format XXXXXX_Y.jpg:  XXXXXX is an identificator for the image and Y is the label 0 for no mask and 1 for mask.
