# 分类： （监督学习）
## 阈值分类器（二类分类器）
## 最邻近分类器
## 逻辑回归
## 朴素贝叶斯分类器

## 评估分类器的性能
### 交叉验证
*标准差*

# 聚类： （数据不带标签）
## 扁平聚类
### k均值
*特征向量* 
## 层次聚类

# 主题模型


# 回归




# numpy
## numpy.ndarray
  - dtype
  - shape
  - operations:
    * ~
    
  - ways to create ndarray:
    * numpy.zeros
    * numpy.empty
    * numpy.ones
    * numpy.array

# matplotlib
  * figure
  * subplot
  * plot
  * scatter
  
# sklearn
  * from sklearn.cluster import KMeans
    > km = KMeans(n_clusters=n)
  
    > km.fit(...)
    
    > km.predict(...)
    
  * from sklearn import neighbors
    > knn = neighbors.KNeighborsClassifier(n_neighbors=2)
    
    > knn.fit()
    
    > knn.predict
    
    > knn.predict.proba
