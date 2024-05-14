import os
import joblib

this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl
data_path = os.path.join(this_dir, 'knn_pipeline_deprector.pkl')
nb_deprector = joblib.load(data_path)


def booleanize(int_repr):
    if int_repr == 0:
        return False
    elif int_repr == 1:
        return True


def deprect(phrase):
    return booleanize(nb_deprector.predict([phrase])[0])
