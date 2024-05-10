import joblib

nb_deprector = joblib.load('naive_bayes_deprector.pkl')


def booleanize(int_repr):
    if int_repr == 0:
        return False
    elif int_repr == 1:
        return True


def deprect(phrase):
    return booleanize(nb_deprector.predict([phrase])[0])