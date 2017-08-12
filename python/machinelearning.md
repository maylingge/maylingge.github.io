机器学习系统设计(Willi Richert) 读书笔记


# 1. 分类： （监督学习）
### 阈值分类器（二类分类器）
### 最邻近分类器
### 逻辑回归(二类)？
     让步比： Pi/(1 - Pi)
     log(Pi/(1-Pi)) 可以用来拟合二分类问题 （0-1）
     log(Pi/(1-Pi)) = C0 + C1*X
     Pi = 1/(1 + exp(-(C0 + C1*x))
     模型拟合出目标属于某类的概率
     C1 是个数组，每个特征对应的系数，正直越大，对分为正类的影响大，负值数值越大对分为负类的影响越大
      
### 朴素贝叶斯分类器 
     P(A)(B|A) = P(B)P(A|B)
     P(F1,F2)*P(C|F1,F2) = P(C)*P(F1,F2|C)
     P(C|F1,F2) = P(C)*P(F1,F2|C)/P(F1,F2)
     假设所有的特征相互独立
     P(F1,F2|C) = P(F1|C)*P(F2|C)
     P(C|F1,F2) = P(C)*P(F1|C)*P(F2|C)/P(F1,F2)
     根据给定的证据估算哪个类别更有可能
     加法平滑 拉普拉斯算子平滑 Lidstone平滑 （在所有计数上加一）
     Cbest = argmaxcC(logP(C=c) + Sum(logP(Fk|C))

### 评估分类器的性能
     欠拟合 
     过拟合
     偏差&方差
          高偏差:    模型太简单，需要引入复杂模型，更多的特征
          高方差:    模型太复杂，需要降低模型复杂度，删减特征
     测试误差和训练误差接近 说明是低方差 误差都很大说明偏差大 模型简单

     交叉验证
          标准差
     准确率 和 召回率
          准确率 = 真正例/（真正例 + 假正例)
          召回率 = 真正例/（真正例 + 假负例)
    

# 2. 聚类： （数据不带标签）
### 扁平聚类
    k均值
       
### 层次聚类

# 主题模型


# 3. 回归
     OLS Ordinary Least Squares 最小二乘法 （均方误差最小的线性拟合）
     numpy.linalg.lstsq 
     RMSE: Root Mean Squared Error, 真实值和预测值之差的平方和除以总数（均方根误差）
     RMSE 与 标准差相似

     大多数数据和它们的均值之间的偏移量最多是两个标准差

     交叉验证
     from sklearn.cross_validation import KFold
     kf = KFold(len(x), n_folds=10)
     for train, test in kf:
     
     
### 惩罚式回归
     如果对训练数据过去信任，就会过拟合，需要加一个惩罚项*惩罚力度
     L1惩罚: Lasso 法 惩罚项是系数的绝对值之和*惩罚力度
     L2惩罚：岭回归法 惩罚项是系数的平方和
     二者的结合是弹性网（elastic net）

     惩罚回归比非惩罚回归拟合的系数要小，甚至是稀疏的，也就是有些特征在拟合的时候不会用到
     模型把特征选择和回归一起做了

     from sklearn.linear_model import ElasticNet
     en = Elastic_net(fit_intercept=True, alpha=0.5)
   
### 特征数多于样本
     OSLS可以得到0误差的训练模型，但模型泛化很差
     加惩罚项
     惩罚力度过大 就会造成欠拟合，很多特征的系数会是0
     惩罚力度太小 接近0就会变成OLS，过拟合
     
     两层交叉验证
     第一层验证 选择最优的参数（惩罚力度）
     第二层验证 评估模型的泛化能力
     
# 4. 深度学习
# 5. 数据预处理 
# 6. 练习


# numpy
### numpy.ndarray
    dtype
    shape
    operations:
      * ~
    ravel() ?

    ways to create ndarray:
      numpy.zeros
      numpy.empty
      numpy.ones
      numpy.array

# matplotlib
    figure
    subplot
    plot
    scatter
  
  
# sklearn
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=n)
    km.fit(...)
    km.predict(...)
    
    from sklearn import neighbors
    knn = neighbors.KNeighborsClassifier(n_neighbors=2)
    knn.fit()
    knn.predict
    knn.predict.proba
    
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.pipline import Pipeline
    from sklearn.cross_validation import ShuffleSplit
    from sklearn.metrics import precision_recall_curve, auc
