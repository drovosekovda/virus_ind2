from main import chek
from joblib import load
import pandas as pd
import os
model_file=r"C:\Users\Данил\test\GaussianNB.joblib"
model = load(model_file)
rez=[]
for root,dirs,files in os.walk(r"C:\Users\Данил\Desktop\Вирусы проги"):
    for filename in files:
        mas=chek(root + '\\' + filename)

        print(filename,mas)
        rez.append(mas)
x = model.predict(rez)
print(x)