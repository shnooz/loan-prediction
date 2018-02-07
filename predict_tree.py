import os
import settings
import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics

def cross_validate(train):
	#creates a logistic regression classifier, taking under consideration the imbalanced data we have
    clf = AdaBoostClassifier(n_estimators=100)
    #creats a list of columns that we want to use to train the model on, removing id and foreclosure_status
    predictors = train.columns.tolist()
    predictors = [p for p in predictors if p not in settings.NON_PREDICTORS]
    #Run cross validation across the train DataFrame.
    predictions = cross_validation.cross_val_predict(clf, train[predictors], train[settings.TARGET], cv=settings.CV_FOLDS)
    #Return the predictions
    return predictions

def compute_error(target, predictions):
	'''Uses scikit-learn to compute a simple accuracy score 
	(the percentage of predictions that matched the actual foreclosure_status values).'''
	return metrics.accuracy_score(target, predictions)

def compute_false_negatives(target, predictions):
	'''Combines the target and the predictions into a DataFrame for convenience.
	Finds the false negative rate.'''
	temp_dict = {"target": target, "predictions": predictions}
	df = pd.DataFrame.from_dict(temp_dict)
	return float(df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0]) / float(df[(df["target"] == 1)].shape[0] + 1)

def compute_false_positives(target, predictions):
	'''Finds the false positive rate. i.e. the number of loans that weren't foreclosed 
	on that the model predicted would be foreclosed on.'''
	#Combines the target and the predictions into a DataFrame for convenience.
	temp_dict = {"target": target, "predictions": predictions}
	df = pd.DataFrame.from_dict(temp_dict)
	return float(df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0]) / float(df[(df["target"] == 0)].shape[0] + 1)

def read():
	'''Read the dataset'''
	train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "train.csv"))
	return train
    
if __name__ == "__main__":
	train = read()
	#compute cross validated predictions
	predictions = cross_validate(train)
    #compute the three error metrics:
	error = compute_error(train[settings.TARGET], predictions)
	fn = compute_false_negatives(train[settings.TARGET], predictions)
	fp = compute_false_positives(train[settings.TARGET], predictions)
    #print:
	print("Accuracy Score: {}".format(error))
	print("False Negatives: {}".format(fn))
	print("False Positives: {}".format(fp))