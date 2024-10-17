import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import os
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

data_path = r'G:\ML\aclImdb'

def load_data(data_path, subset):
    data = []
    labels = []
    for sentiment in ['pos', 'neg']:
        path = os.path.join(data_path, subset, sentiment)
        for file_name in os.listdir(path):
            with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
                data.append(file.read())
                labels.append(1 if sentiment == 'pos' else 0)
    return data, labels

train_data, train_labels = load_data(data_path, 'train')
test_data, test_labels = load_data(data_path, 'test')

vectorizer = CountVectorizer(stop_words=stopwords.words('english'))

X_train = vectorizer.fit_transform(train_data)
X_test = vectorizer.transform(test_data)

y_train = np.array(train_labels)
y_test = np.array(test_labels)

model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

joblib.dump(model, 'model_svm.pkl')
joblib.dump(vectorizer, 'vectorizer_smv.pkl')