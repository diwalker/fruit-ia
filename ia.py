from sklearn import tree

X = [[148, 1], [130, 1], [150, 0], [170, 0]] #gramatura e superficie
Y = [5, 5, 10, 10] #tipo de fruta

clf = tree.DecisionTreeClassifier() #arvore de decisao
clf = clf.fit(X, Y) #treinamento]

print(clf.predict([[145, 0]])) #predicao
