from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier#create dummy data
X,y = make_classification(n_samples=200,n_features= 10,random_state=42)
#define the grid of hyperparameters to try
param_grid = {
    'n_estimators': [50,100], # try 50 and 100 trees
    'max_depth': [5,10], # try max depth of 5 and 10
}

#create gridSearch object
gs = GridSearchCV(RandomForestClassifier(random_state=42),param_grid,cv=3)
#cv=  3 fold validation
#estimator- the model to tune
#param_grid= the grid define above


#run the search (train 2*2*3 models)
gs.fit(X,y)
#print the best hyperparameters
print("best params",gs.best_params_)
print("best accuracy",gs.best_score_)

# Objective :- to find best n_estimators and max_depth for random forest on dummy data
