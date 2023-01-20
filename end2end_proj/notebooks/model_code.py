import pandas as pd
import numpy as np

import seaborn as sns

import neattext.functions as nfx

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# Transformers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


df = pd.read_csv("https://raw.githubusercontent.com/Jcharis/end2end-nlp-project/main/notebooks/data/emotion_dataset_raw.csv")

df.head()
df['Emotion'].value_counts()

sns.countplot(x='Emotion',data=df)

dir(nfx)

df['Clean_Text'] = df['Text'].apply(nfx.remove_userhandles)
df['Clean_Text'] = df['Clean_Text'].apply(nfx.remove_stopwords)
df


Xfeatures = df['Clean_Text']
ylabels = df['Emotion']

x_train,x_test,y_train,y_test = train_test_split(Xfeatures,ylabels,test_size=0.3,random_state=42)

from sklearn.pipeline import Pipeline

pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])

pipe_lr.fit(x_train,y_train)

pipe_lr.score(x_test,y_test)

ex1 = "This book was so interesting it made me happy"

pipe_lr.predict([ex1])


pipe_lr.predict_proba([ex1])

pipe_lr.classes_

# Save Model & Pipeline
import joblib
pipeline_file = open("emotion_classifier_pipe_lr.pkl","wb")
joblib.dump(pipe_lr,pipeline_file)
pipeline_file.close()


