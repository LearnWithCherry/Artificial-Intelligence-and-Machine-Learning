from sklearn.datasets import make_classification
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

X,y = make_classification(n_samples=200, n_features=10, random_state=42)
param_dist={
    'n_estimators': [50,100,200],
    'max_depth': [3,5,10,None],
}

rs=RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=5,
    cv=3,
    scoring='accuracy',
    random_state=42
)

rs.fit(X,y)

print("Best params:", rs.best_params_)
print("Best score:", rs.best_score_)

!pip install autosklearn
import autosklearn.classification
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=60,   # seconds total
    per_run_time_limit=15,
    ensemble_size=3
)
automl.fit(X_train, y_train)
print("Test accuracy:", automl.score(X_test, y_test))
