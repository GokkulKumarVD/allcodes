import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits

digit = load_digits()

dir(digit)

# df = pd.DataFrame(digit.data, columns=digit.feature_names)

# digit['target']=digit.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =train_test_split(digit.data, digit.target, train_size=0.7)

from sklearn.model_selection import cross_val_score

# For small datasets, ‘liblinear’ is a good choice, whereas ‘sag’ and ‘saga’ are faster for large ones.
cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'), X_test, y_test, cv=3)

# if gamma='scale' (default) is passed then it uses 1 / (n_features * X.var()) as value of gamma,
# if ‘auto’, uses 1 / n_features.
cross_val_score(SVC(gamma='auto'), X_test, y_test, cv=3)


cross_val_score(RandomForestClassifier(n_estimators=40), X_test, y_test, cv=3)




