from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import resample
import pandas as pd


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class ChangeSize(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        
        class0 = data[data.PERFIL == "EXCELENTE"]
        class1 = data[data.PERFIL == "MUITO_BOM"]
        class2 = data[data.PERFIL == "HUMANAS"]
        class3 = data[data.PERFIL == "EXATAS"]
        class4 = data[data.PERFIL == "DIFICULDADE"]
        
        class0_upsampled = resample(class0, replace=True, n_samples=c0, random_state=337)
        class1_upsampled = resample(class1, replace=True, n_samples=c0, random_state=337)
        class2_upsampled = resample(class2, replace=True, n_samples=c0, random_state=337)
        class3_downsampled = resample(class3, replace=False, n_samples=c0, random_state=337)
        class4_downsampled = resample(class4, replace=False, n_samples=c0, random_state=337)

        data = pd.concat([class0_upsampled, class1_upsampled, class2_upsampled, class3_downsampled, class4_downsampled, ])
        return data

