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
