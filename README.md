This is my first MACHIN LEARNING project.

# Loan Prediiction
By using the Fannie Mae dataset (Q4 2016 data - https://loanperformancedata.fanniemae.com) I'll try to predict whether a loan will be foreclosed on in the future by only using information that was available when the loan was acquired. In effect, I'll create a "score" for any mortgage that will tell us if Fannie Mae should buy it or not.


While doing this project I followed Dataquest blog - https://www.dataquest.io/blog/data-science-portfolio-machine-learning/

# Installation
## Download the data
+ Clone this repo to your computer.
+ Get into the folder using cd loan-prediction.
+ Run mkdir data.
+ Switch into the data directory using cd data.
+ Download the data files from Fannie Mae into the data directory. 
++ You can find the data here: https://loanperformancedata.fanniemae.com.
++ You'll need to register with Fannie Mae to download the data.
It's recommended to download all the data from Q4 2013 - Q4 2016.
+ Extract all of the .zip files you downloaded. 

## Install the requirements
+ Install the requirements using pip install -r requirements.txt. 
++ Make sure you use Python 2.
++ You may want to use a virtual environment for this.

## Usage
+ Run mkdir processed to create a directory for our processed datasets.
+ Run python assemble.py to combine the Acquisition and Performance datasets. 
++ This will create Acquisition.txt and Performance.txt in the processed folder.
+ Run python annotate.py. 
++ This will create training data from Acquisition.txt and Performance.txt.
++ It will add a file called train.csv to the processed folder.
+ Run python predict.py. 
++ This will run cross validation across the training set, using #logistic regression# and print the accuracy score (and false negatives and false positive rates).
+ Run python predict_tree.py.
++ This will run cross validation across the training set, using #AdaBoost algorithm# and print the accuracy score (and false negatives and false positive rates).

As you can see the AdaBoost Algorithm did much better on predicting the loans outcomes.

Enjoy!
Shnooz