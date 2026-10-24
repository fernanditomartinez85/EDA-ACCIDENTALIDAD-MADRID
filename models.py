import pickle as pkl
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import PrecisionRecallDisplay
import seaborn as sns
import matplotlib.pyplot as plt

class AlcoholLogisticModel:
    def __init__(self,X_train,X_test, y_train, y_test):
        self.X_train = X_train 
        self.X_test = X_test
        self.y_train =  y_train 
        self.y_test = y_test
        self.model = Pipeline([
            ('codificacion', OneHotEncoder(handle_unknown='ignore')),
            ('regresion', LogisticRegression(class_weight='balanced', max_iter=1000))
        ])
    def fit(self):
        self.model.fit(self.X_train, self.y_train)
    def predict(self):
        return self.model.predict(self.X_test)
    def evaluate(self):
        y_predict = self.predict()
        accuracy = accuracy_score(self.y_test, y_predict)
        matriz_confusión = confusion_matrix(self.y_test, y_predict)
        print(f'Accuracy: {accuracy}')
        print(classification_report(self.y_test, y_predict))
        plt.figure(figsize=(8,6))
        sns.heatmap(matriz_confusión, annot=True, fmt="d", linewidths=.5, square = True, cmap = 'Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        plt.title('Matriz de confusión', size = 15)
        plt.show()
        RocCurveDisplay.from_estimator(self.model, self.X_test, self.y_test)
        plt.title('Curva ROC')
        plt.show()
        PrecisionRecallDisplay.from_estimator(self.model, self.X_test, self.y_test)
        plt.title('Curva precisión-recall')
        plt.show()
    def save_model(self, save_path):
        with open(save_path, 'wb') as fp:
            pkl.dump(self.model, fp)
    def load_model(self, load_path):
        with open(load_path, 'rb') as fp:
            self.model = pkl.load(fp)
