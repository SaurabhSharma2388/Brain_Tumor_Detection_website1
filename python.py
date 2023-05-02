import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

path=os.listdir('https://braintumordetectionwebsite1.saurabhsharma72.repl.co/no_tumor')
tumor_check={'no_tumor':0,'pituitary_tumor':1}