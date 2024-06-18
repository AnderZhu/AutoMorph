import numpy as np
import pandas as pd
import shutil
import os


result_Eyepacs = './test_outside/results_ensemble.csv'

assert(os.path.exists('/content/drive/My Drive/'))

PATH = os.path.join('/content/drive/My Drive/', '/Results/M1/Good_quality/'
if not os.path.exists(PATH):
    os.makedirs(PATH)
# if not os.path.exists('../Results/M1/Bad_quality/'):
#     os.makedirs('../Results/M1/Bad_quality/')

result_Eyepacs_ = pd.read_csv(result_Eyepacs)

Eyepacs_pre = result_Eyepacs_['Prediction']
Eyepacs_bad_mean = result_Eyepacs_['softmax_bad']
Eyepacs_usable_sd = result_Eyepacs_['usable_sd']
name_list = result_Eyepacs_['Name']

Eye_good = 0
Eye_bad = 0

for i in range(len(name_list)):
    
    if Eyepacs_pre[i]==0:
        Eye_good+=1
        shutil.copy(name_list[i], PATH)
    elif (Eyepacs_pre[i]==1) and (Eyepacs_bad_mean[i]<0.25):
    #elif (Eyepacs_pre[i]==1) and (Eyepacs_bad_mean[i]<0.25) and (Eyepacs_usable_sd[i]<0.1):
        Eye_good+=1
        shutil.copy(name_list[i], PATH)        
    else:
        Eye_bad+=1        
        # shutil.copy(name_list[i], '../Results/M1/Bad_quality/')
        #shutil.copy(name_list[i], '../Results/M1/Good_quality/')


print('Gradable cases by EyePACS_QA is {} '.format(Eye_good))
print('Ungradable cases by EyePACS_QA is {} '.format(Eye_bad))
