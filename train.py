#import all the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
import pickle


#These are the Hyperparameters to tune for RandomForest Model
n_estimators=260, 
max_depth=18,
min_samples_leaf=1

#The file to save for final trained model
output_file = f'./model/model.bin'

#loading the data
df = pd.read_csv("./data/water_potability.csv")

# Creating the copy of the original data
df_copy = df.copy()

#Standardizing the names of the columns to small case letters 

df_copy.columns = df_copy.columns.str.lower().str.replace(' ', '_')

#Filling the missing values of each columns
df_copy = df_copy.fillna(method='pad')

#Fill the missing value of ph column by 7.08 i.e the mean of the same
df_copy.ph = df_copy.ph.fillna(7.08)


#Here we use 80% data for training, 20% for test 

df_full_train, df_test = train_test_split(df_copy, test_size=0.2, random_state=1)

#Training function
def train(df_train, y_train, n_estimators=260, max_depth=18, min_samples_leaf=1):
    dv = DictVectorizer(sparse=False)
    
    train_dict = df_train.to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)
    model = RandomForestClassifier(n_estimators=n_estimators,
                            max_depth=max_depth,
                            min_samples_leaf=min_samples_leaf,
                            random_state=1)
    model.fit(X_train, y_train)
    return model, dv
    
#Predict Function
def predict(df, dv, model):
    dicts_test = df.to_dict(orient='records')
    X_test = dv.transform(dicts_test)
    y_pred = model.predict_proba(X_test)[:, 1]
    return y_pred



# Selecting the train+validation=full_train_dataset dataset
df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# getting the target values for complete dataset
y_full_train = df_full_train.potability.values
y_test = df_test.potability.values

# delete the target variable from the dataset 
del df_full_train['potability']
# del y_test['potability']


# Training of the model
print("Start Training the Model .....")
model, dv = train(df_full_train, y_full_train)

#Prediction from the model
y_pred = predict(df_test, dv, model)

#AUC of the model for test dataset(unseen)
auc = roc_auc_score(y_test, y_pred)
print(f"The AUC of the model is --> {auc}")



#Saving The Model
with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

print(f"The model is saved in --> {output_file}")




