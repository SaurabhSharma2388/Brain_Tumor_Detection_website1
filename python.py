import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.decomposition import PCA

# Load data
path_no_tumor = 'https://braintumordetectionwebsite1.saurabhsharma72.repl.co/no_tumor'
path_pituitary_tumor = 'https://braintumordetectionwebsite1.saurabhsharma72.repl.co/pituitary_tumor'
path_meningioma_tumor = 'https://braintumordetectionwebsite1.saurabhsharma72.repl.co/meningioma_tumor'
path_glioma_tumor = 'https://braintumordetectionwebsite1.saurabhsharma72.repl.co/glioma_tumor'
tumor_check = {'no_tumor': 0, 'pituitary_tumor': 1, 'meningioma_tumor': 2, 'glioma_tumor': 3}

x = []
y = []
for cls in tumor_check:
    if cls == 'no_tumor':
        path = path_no_tumor
    elif cls == 'pituitary_tumor':
        path = path_pituitary_tumor
    elif cls == 'meningioma_tumor':
        path = path_meningioma_tumor
    elif cls == 'glioma_tumor':
        path = path_glioma_tumor
    for j in os.listdir(path):
        image = cv2.imread(path+'/'+j, 0)
        image = cv2.resize(image, (200, 200))
        x.append(image)
        y.append(tumor_check[cls])

x = np.array(x)
y = np.array(y)

pd.Series(y).value_counts()

# Prepare data
x_update = x.reshape(len(x), -1)
x_train, x_test, y_train, y_test = train_test_split(x_update, y, random_state=10, test_size=0.3)

x_train = x_train / 255
x_test = x_test / 255

pca = PCA(.98)
pca_train = pca.fit_transform(x_train)
pca_test = pca.transform(x_test)

logistic = LogisticRegression(C=0.1)
logistic.fit(pca_train, y_train)

sv = SVC()
sv.fit(pca_train, y_train)

# Execute function
@app.route("/execute_python_function", methods=["POST"])
def execute_python_function():
    # Get the uploaded file
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img, (200, 200))
    img1 = img1.reshape(1, -1) / 255
    p = sv.predict(pca.transform(img1))
    dec = {0: 'no_tumor', 1: 'pituitary_tumor', 2: 'meningioma_tumor', 3: 'glioma_tumor'}
    tumor_type = dec[p[0]]
    return tumor_type

