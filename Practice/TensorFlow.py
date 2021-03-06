import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC()
clf = svm.SVC(gamma=0.001, C=100)

X,y = digits.data[:-10], digits.target[:-10]
clf.fit(X,y)

print(clf.predict(digits.data[-9:-8]))

plt.imshow(digits.images[-9], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

