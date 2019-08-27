# 优化一个web项目的方法有哪些
    后端给返回的数据加缓存
    网页缓存 CDN
    集群 负载均衡
    数据库查询优化


# MySQL查询优化
    打开慢查询log
    mysqldumpslow 打印log统计信息 或者直接查看log
    优化SQL
    
## 优化SQL
### 重写SQL语句
    SELECT count(*) FROM tbl_xxx WHERE XXXX ===》
    SELECT id FROM tbl_xxx WHERE XXXX LIMIT 1
    
    
### 创建索引
    explain + SQL 分析慢查询
   [MySQL索引原理及慢查询优化](https://tech.meituan.com/2014/06/30/mysql-index.html)
   
    索引：
    B+树， 三层高度的B+树可以存储百万数据？ 真实数据存储在叶子节点，高度决定了IO的次数， 
           对于复合数据项使用最左匹配原则， 数据项越小 树的高度越小，所以索引字段越小越好
    
