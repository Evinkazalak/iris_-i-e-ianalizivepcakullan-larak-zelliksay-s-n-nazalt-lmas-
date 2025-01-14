# -*- coding: utf-8 -*-
"""IRIS_ÇiçeğiAnaliziVePCAKullanılarakÖzellikSayısınınAzaltılması.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ywdx455vdeKGVq1OOVtq_ZwXZJ9rVrC6
"""

import pandas as pd
import matplotlib.pyplot as plt
#bağımsız değişkenleri belli bir aynı scale içine dahil ediyor. yoksa pca algoritması yanlış çalışıyor.
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url='pca_iris.data'
df=pd.read_csv(url,names=['sepal length','sepal width','petal length','petal width','target'])

df

features=['sepal length','sepal width','petal length','petal width']
#çiçeğin hangi türe ait olduğunu tahmin ediyor.
#featureleri x olarak ,targeti y olarak ayıralım

x=df[features]
y=df[['target']]

#featureler çok farklı boyutlarda ve bunların yapay zeka tarafından eşit ağırlıklarda dengelenmesi gerekiyor.
#bu yüzden standart scaler kullanarak tüm verileri mean=0 and variance=1 olacak şekilde değiştiriyoruz.

x=StandardScaler().fit_transform(x)

x

#orjinal verilerimiz 4 boyutlu. bunları pca yaparak 2 boyuta indirgeyeceğiz.

#boyutunu 2 olarak ayarlıyoruz.
pca=PCA(n_components=2)
#x  parametresi yani futureleri ver
principalComponents=pca.fit_transform(x)
principalDF=pd.DataFrame(data=principalComponents,columns=['principal component 1','principal component 2'])

principalDF #bunlar sıkıştırma sonucu elde ettiğim değerler bir anlam ifade etmiyor.

#target sütununa da PCA dataframeyi ekleyelim

final_dataframe=pd.concat([principalDF,df[['target']]],axis=1)

final_dataframe.head()

#final dataframemizi görselleştirelim.
#dataframeyi 3 e bölelim.

dfsetosa=final_dataframe[df.target=='Irıs-setosa']
dfvirginica=final_dataframe[df.target=='Irıs-virginica']
dfversicolor=final_dataframe[df.target=='Irıs-versicolor']

plt.xlabel('Principal component 1')
plt.ylabel('Principal component 2')


plt.scatter(dfsetosa['principal component 1'], dfsetosa['principal component 2'],color='green')
plt.scatter(dfvirginica['principal component 1'], dfvirginica['principal component 2'],color='red')
plt.scatter(dfversicolor['principal component 1'], dfversicolor['principal component 2'],color='blue')

pca.explained_variance_ratio_

#pca yaptığım halde veri setimin %95 ini korumuşum
pca.explained_variance_ratio_.sum()