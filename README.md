# autocheck

## 项目说明
- 用于主机及软件资源的实时监控, 邮件预警及信息统计

## 功能说明
### 实时监控功能
1. 系统资源进行监控记录
  - 服务器启动时间, CPU, 内存, 磁盘, Swap
2. Tomcat资源进行监控记录
  - Pid, 启动时间, 内存使用, 连接数, 线程数, 启动参数, Jvm内存回收
3. Redis资源进行监控记录
  - Pid, 启动时间, 内存使用, 连接数, 线程数, 主从集群信息, Sentinel监控信息
4. MySQL资源进行监控记录
  - Pid, 启动时间, 内存使用, 连接数, 线程数, 主从集群信息
5. Oracle资源进行监控记录
  - 表空间
6. 备份目录进行监控记录
  - 备份文件, 文件大小, 创建时间
7. 用户资源限制监控记录
  - nofile, nproc

### 实时邮件预警功能
1. 系统资源预警
  - CPU使用率, 内存使用率, 磁盘使用率
2. Tomcat预警
  - 是否运行, YGC和FGC的平均时间
3. Redis预警
  - 是否运行, 主从连接状态
4. MySQL预警
  - 是否运行, 主从连接状态, 主从延迟时间
5. Oracle预警
  - 表空间使用率
6. 备份预警
  - 未备份, 备份大小异常
7. 用户资源限制预警
  - nofile, nproc限制小于5000

### 定时资源统计并邮件发送功能
1. 系统资源统计
  - 服务器启动时间, CPU, 内存, 磁盘, Swap
2. Tomcat资源统计
  - Pid, 启动时间, 内存使用, 连接数, 线程数, 启动参数, Jvm内存回收, Java版本
3. Redis资源统计
  - Pid, 启动时间, 内存使用, 连接数, 线程数, 主从集群信息, Sentinel监控信息
4. MySQL资源统计
  - Pid, 启动时间, 内存使用, 连接数, 线程数, 主从集群信息, 慢日志文件及分析文件
5. Oracle资源统计
  - 表空间, awr报告
6. 备份目录资源统计
  - 备份文件, 文件大小, 创建时间

### 更多功能
- 请查看下方配置文件内的功能说明

## 安装使用
### 说明
- 该项目已在Centos7版本上测试
- 该项目只支持Python3环境
- 安装使用的操作必须使用root用户
- 若要使用tomcat的jvm监控预警, 则root用户下的环境变量中须有jstat命令路径
### 在线
- 安装Python3环境和开发工具
```
# yum install python3 python3-devel git -y
```

- 下载autocheck
```
# cd /opt/
# git clone https://github.com/xhsky/autocheck.git
```

- 下载依赖包
```
# cd /opt/autocheck
# pip3 install -r whl/requirements.txt
```

### 离线
- 安装Python3环境和开发工具
```
# 在相同系统版本上编译python3后安装到服务器上
# 配置python3环境变量
```

- 下载autocheck
```
# 从https://github.com/xhsky/autocheck/archive/master.zip下载autocheck程序
# 解压后放到服务器上
```

- 下载依赖包
```
# cd autocheck
# pip3 install -r whl/*.whl
# pip3 install -r whl/*.tar.gz
```

### 使用
1. 进入autocheck目录, 并编辑conf/autocheck.conf配置文件以定义监控的项目  
  *配置文件中`#`是注释符号, 注释必须单独占一行, 不能写到配置项后面*  
  *只有当前主机安装了软件, 该软件下的check才可置为1*
```
# cd autocheck
# vim conf/autocheck.conf
  [autocheck]
  # 定义当前主机的名称
  hostname=dream
  # 预警百分比
  warning_percent=95
  # 预警间隔, 单位分钟
  warning_interval=30
  # 分析间隔, 单位秒. 建议在3-8秒之间
  analysis_interval=5
  # 数据保留天数
  keep_days=3
  
  [logs]
  # 日志文件
  log_file=./logs/autocheck.log
  # 日志级别
  log_level=info
  
  [host]
  # 扫描间隔时间, 单位为秒, 最低值为10
  # 磁盘
  disk_interval=300
  # CPU
  cpu_interval=20
  # 内存
  memory_interval=20
  # Swap
  swap_interval=300
  # 查看用户下的资源限制, 多个用户以逗号分隔(该用户需为可登陆用户)
  users_limit=root, user1, user2
  
  [tomcat]
  # 是否统计Tomcat
  check=0
  # 扫描间隔时间, 单位为秒, 最低值为10
  tomcat_interval=15
  # 指定Tomcat的端口, 多个Tomcat以逗号分隔
  tomcat_port=8080, 8081
  
  [redis]
  # 是否统计Redis
  check=0
  # 扫描间隔时间, 单位为秒, 最低值为10
  redis_interval=15
  # redis的密码
  password=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  # redis端口
  redis_port=6379
  # 若未安装sentinel, 则注释掉下面两项
  # sentinel端口
  sentinel_port=26379
  # sentinel监控的集群名称
  sentinel_name=mymaster
  
  [mysql]
  # 是否统计MySQL
  check=0
  # 扫描间隔时间, 单位为秒, 最低值为10
  mysql_interval=15
  # 指定MySQL端口
  mysql_port=3306
  # 指定MySQL的root密码
  mysql_password=xxxxxxxxxx
  # 指定MySQL主从延迟预警时间, 单位秒
  seconds_behind_master=5
  
  [oracle]
  # 是否统计Oracle
  check=0
  # 扫描间隔时间, 单位为秒, 最低值为10
  oracle_interval=300
  # 生成前N个小时的awr报告
  awr_hours=24
  
  [backup]
  # 是否统计备份
  check=0
  # 指定备份文件的目录. 可设置多个, 以,分隔
  dir=/data, /data2, /data3
  # 指定备份文件的通用结尾, 多个目录以,分隔
  regular=tar.gz, tar.gz, tar.gz
  # 指定每个目录统计的时间(备份完成后的时间), 多个时间以,分隔
  cron_time=22:05, 23:55, 19:20
  
  [send]
  # 是否发送24小时的统计信息
  check=1
  # 每天定时发送邮件的时间
  send_time=18:05
  # 发送统计信息的粒度级别, 单位分钟, 默认以10分钟为间隔, 范围1-60
  granularity_level=30
  
  [mail]
  # 发送者的名称
  sender=xxx
  # 收件人的邮箱地址, 多个邮箱以,分隔
  receive=xxx@dreamdt.cn, yyy@dreamdt.cn
  # 邮件标题
  subject=xx项目巡检
```

2. 配置完成后执行main.py文件
```
# ./main.py start
```

3. 查看运行日志, 无报错信息
```
# cat logs/autocheck.log
2019-11-28 10:35:14, 607 - INFO: 程序启动...
2019-11-28 10:35:14, 620 - INFO: Main Pid: 24993
2019-11-28 10:35:14, 682 - INFO: 开始采集资源信息...
2019-11-28 10:35:14, 696 - INFO: 开始采集主机资源信息...
2019-11-28 10:35:14, 696 - INFO: 开始采集磁盘资源信息...
2019-11-28 10:35:14, 734 - INFO: 开始采集CPU资源信息...
2019-11-28 10:35:14, 734 - INFO: 开始采集内存资源信息...
2019-11-28 10:35:14, 734 - INFO: 开始采集Swap资源信息...
2019-11-28 10:35:14, 734 - INFO: 开始采集启动时间资源信息...
2019-11-28 10:35:14, 736 - INFO: 开始采集MySQL资源信息...
2019-12-28 10:35:14, 737 - INFO: 开始记录用户限制信息...
2019-11-28 10:35:14, 746 - INFO: 开始分析资源信息...
2019-11-28 10:35:14, 747 - INFO: 开始分析主机资源信息...
2019-11-28 10:35:14, 749 - INFO: 开始分析MySQL资源信息...
2019-11-28 10:35:14, 751 - INFO: 清理程序启动...
```

## 报告示例:
### 预警报告示例(将显示在邮件正文)
- 用户资源限制示例:
```
主机: dream
用户资源限制预警:
用户(sky)的nofile参数值(1024)过低.
请在root用户下执行命令: echo 'sky - nofile 65536' >> /etc/security/limits.conf,  然后重启登录该用户再重启该用户下相应软件
```

- 主机资源CPU预警:
```
主机: web1
CPU预警:
CPU使用率当前已达到97.1%
```

- Tomcat未运行预警
```
主机: web1
Tomcat预警:
Tomcat(8080)未运行
```

- Jvm内存预警
```
主机: web2
Tomcat预警:
Tomcat(8080)YGC平均时间为2
```

- Oracle表空间预警
```
主机: oracle
Oracle表空间预警:
SYSTEM表空间已使用99.38%
```

- MySQL主从连接预警
```
主机: db1
MySQL预警:
MySQL主从连接:
Slave_IO_Running: Connecting
Slave_SQL_Running: Yes
Slave_IO_State: Connecting to master
Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
Seconds_Behind_Master: NULL
```

### 资源统计报告示例(将显示在邮件附件)
```
统计开始时间: 2019-11-28 10:18:00
主机名: test
----------------------------------------------------------------------------------------------------
系统启动时间: 2019-08-14 11:03:57
****************************************************************************************************
磁盘统计:
/磁盘统计:
+---------------------+--------+-----------+----------+------------+--------------+--------+
|       记录时间      | 挂载点 |  磁盘名称 | 磁盘大小 | 已使用大小 | 已使用百分比 |  可用  |
+---------------------+--------+-----------+----------+------------+--------------+--------+
| 2019-11-27 16:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-27 17:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.7%     | 31.74G |
| 2019-11-27 18:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-27 19:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.7%     | 31.74G |
| 2019-11-27 20:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
| 2019-11-27 21:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-27 22:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
| 2019-11-27 23:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-28 00:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
| 2019-11-28 01:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
| 2019-11-28 02:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
| 2019-11-28 03:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-28 04:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.7%     | 31.74G |
| 2019-11-28 05:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.74G |
| 2019-11-28 06:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-28 07:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
| 2019-11-28 08:28:13 |   /    | /dev/vda1 |  39.25G  |   5.49G    |    14.8%     | 31.74G |
| 2019-11-28 09:28:13 |   /    | /dev/vda1 |  39.25G  |   5.50G    |    14.8%     | 31.73G |
+---------------------+--------+-----------+----------+------------+--------------+--------+
****************************************************************************************************
/data磁盘统计:
+---------------------+--------+-----------+----------+------------+--------------+---------+
|       记录时间      | 挂载点 |  磁盘名称 | 磁盘大小 | 已使用大小 | 已使用百分比 |   可用  |
+---------------------+--------+-----------+----------+------------+--------------+---------+
| 2019-11-27 16:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.94G   |     3.4%     | 482.82G |
| 2019-11-27 17:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.94G   |     3.4%     | 482.81G |
| 2019-11-27 18:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.98G   |     3.4%     | 482.78G |
| 2019-11-27 19:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.73G   |     3.3%     | 483.03G |
| 2019-11-27 20:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.70G   |     3.3%     | 483.06G |
| 2019-11-27 21:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.95G   |     3.4%     | 482.80G |
| 2019-11-27 22:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.95G   |     3.4%     | 482.80G |
| 2019-11-27 23:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.70G   |     3.3%     | 483.05G |
| 2019-11-28 00:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.96G   |     3.4%     | 482.80G |
| 2019-11-28 01:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.96G   |     3.4%     | 482.80G |
| 2019-11-28 02:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.93G   |     3.4%     | 482.83G |
| 2019-11-28 03:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.96G   |     3.4%     | 482.79G |
| 2019-11-28 04:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.97G   |     3.4%     | 482.79G |
| 2019-11-28 05:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.97G   |     3.4%     | 482.78G |
| 2019-11-28 06:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.97G   |     3.4%     | 482.78G |
| 2019-11-28 07:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.69G   |     3.3%     | 483.06G |
| 2019-11-28 08:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.70G   |     3.3%     | 483.05G |
| 2019-11-28 09:28:13 | /data  | /dev/vdb1 | 499.75G  |   16.99G   |     3.4%     | 482.77G |
+---------------------+--------+-----------+----------+------------+--------------+---------+
****************************************************************************************************
CPU统计:
+---------------------+-----------+-----------+
|       记录时间      | CPU核心数 | CPU使用率 |
+---------------------+-----------+-----------+
| 2019-11-27 16:28:13 |     8     |    1.5%   |
| 2019-11-27 17:28:13 |     8     |    1.6%   |
| 2019-11-27 18:28:13 |     8     |    1.4%   |
| 2019-11-27 19:28:13 |     8     |    1.4%   |
| 2019-11-27 20:28:13 |     8     |    1.6%   |
| 2019-11-27 21:28:13 |     8     |    1.5%   |
| 2019-11-27 22:28:13 |     8     |    1.7%   |
| 2019-11-27 23:28:13 |     8     |    1.5%   |
| 2019-11-28 00:28:13 |     8     |    1.7%   |
| 2019-11-28 01:28:13 |     8     |    1.7%   |
| 2019-11-28 02:28:13 |     8     |    1.5%   |
| 2019-11-28 03:28:13 |     8     |    1.6%   |
| 2019-11-28 04:28:13 |     8     |    1.6%   |
| 2019-11-28 05:28:13 |     8     |    1.9%   |
| 2019-11-28 06:28:13 |     8     |    1.4%   |
| 2019-11-28 07:28:13 |     8     |    1.5%   |
| 2019-11-28 08:28:13 |     8     |    1.5%   |
| 2019-11-28 09:28:13 |     8     |    1.4%   |
+---------------------+-----------+-----------+
****************************************************************************************************
内存统计:
+---------------------+----------+-------------+--------+--------------+------------+
|       记录时间      | 内存大小 | 可用(avail) | 已使用 | 已使用百分比 | 剩余(free) |
+---------------------+----------+-------------+--------+--------------+------------+
| 2019-11-27 16:28:13 |  15.51G  |    8.01G    | 7.18G  |    48.4%     |  226.98M   |
| 2019-11-27 17:28:13 |  15.51G  |    7.99G    | 7.20G  |    48.5%     |  267.40M   |
| 2019-11-27 18:28:13 |  15.51G  |    7.98G    | 7.21G  |    48.5%     |  276.99M   |
| 2019-11-27 19:28:13 |  15.51G  |    7.97G    | 7.22G  |    48.6%     |  271.43M   |
| 2019-11-27 20:28:13 |  15.51G  |    7.97G    | 7.22G  |    48.6%     |  258.41M   |
| 2019-11-27 21:28:13 |  15.51G  |    7.95G    | 7.24G  |    48.8%     |  273.27M   |
| 2019-11-27 22:28:13 |  15.51G  |    7.94G    | 7.25G  |    48.8%     |  256.52M   |
| 2019-11-27 23:28:13 |  15.51G  |    7.94G    | 7.25G  |    48.8%     |  267.79M   |
| 2019-11-28 00:28:13 |  15.51G  |    7.94G    | 7.25G  |    48.8%     |  255.68M   |
| 2019-11-28 01:28:13 |  15.51G  |    7.93G    | 7.26G  |    48.9%     |  253.53M   |
| 2019-11-28 02:28:13 |  15.51G  |    7.92G    | 7.27G  |    48.9%     |  281.97M   |
| 2019-11-28 03:28:13 |  15.51G  |    7.91G    | 7.28G  |     49%      |  278.00M   |
| 2019-11-28 04:28:13 |  15.51G  |    7.90G    | 7.29G  |    49.1%     |  269.05M   |
| 2019-11-28 05:28:13 |  15.51G  |    7.90G    | 7.29G  |    49.1%     |  256.34M   |
| 2019-11-28 06:28:13 |  15.51G  |    7.89G    | 7.30G  |    49.1%     |  256.90M   |
| 2019-11-28 07:28:13 |  15.51G  |    7.88G    | 7.31G  |    49.2%     |  272.40M   |
| 2019-11-28 08:28:13 |  15.51G  |    7.88G    | 7.32G  |    49.2%     |  264.40M   |
| 2019-11-28 09:28:13 |  15.51G  |    7.86G    | 7.33G  |    49.3%     |  255.71M   |
+---------------------+----------+-------------+--------+--------------+------------+
****************************************************************************************************
Swap统计:
+---------------------+----------+--------+--------------+-------+
|       记录时间      | Swap大小 | 已使用 | 已使用百分比 |  剩余 |
+---------------------+----------+--------+--------------+-------+
| 2019-11-27 16:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 17:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 18:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 19:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 20:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 21:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 22:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-27 23:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 00:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 01:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 02:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 03:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 04:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 05:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 06:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 07:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 08:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
| 2019-11-28 09:28:13 |  0.00k   | 0.00k  |      0%      | 0.00k |
+---------------------+----------+--------+--------------+-------+
****************************************************************************************************
Tomcat统计:
Java版本: 8
****************************************************************************************************
Tomcat(8080)统计信息:
启动信息:
+---------------------+-------+------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       记录时间      |  Pid  | 端口 |       启动时间      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      启动参数                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+---------------------+-------+------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2019-11-28 10:17:47 | 24682 | 8080 | 2019-11-12 21:37:12 | /data/jdk/bin/java,-Djava.util.logging.config.file=/data/tomcat//conf/logging.properties,-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager,-server,-XX:+AggressiveOpts,-XX:+UseBiasedLocking,-XX:+DisableExplicitGC,-XX:+UseConcMarkSweepGC,-XX:+UseParNewGC,-XX:+CMSParallelRemarkEnabled,-XX:+UseFastAccessorMethods,-XX:+UseCMSInitiatingOccupancyOnly,-Djava.security.egd=file:/dev/./urandom,-Djava.awt.headless=true,-Xms8092M,-Xmx8092M,-Xss512k,-XX:LargePageSizeInBytes=128M,-XX:MaxTenuringThreshold=11,-XX:MetaspaceSize=200m,-XX:MaxMetaspaceSize=256m,-XX:MaxNewSize=256m,-Djdk.tls.ephemeralDHKeySize=2048,-Djava.protocol.handler.pkgs=org.apache.catalina.webresources,-Dorg.apache.catalina.security.SecurityListener.UMASK=0027,-Dignore.endorsed.dirs=,-classpath,/data/tomcat//bin/bootstrap.jar:/data/tomcat//bin/tomcat-juli.jar,-Dcatalina.base=/data/tomcat/,-Dcatalina.home=/data/tomcat/,-Djava.io.tmpdir=/data/tomcat//temp,org.apache.catalina.startup.Bootstrap,start |
+---------------------+-------+------+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
运行信息:
+---------------------+-------+----------+------------+--------+--------+
|       记录时间      |  Pid  | 内存使用 | 内存使用率 | 连接数 | 线程数 |
+---------------------+-------+----------+------------+--------+--------+
| 2019-11-27 16:28:13 | 24682 |  5.70G   |   36.73%   |   16   |  517   |
| 2019-11-27 17:28:13 | 24682 |  5.71G   |   36.80%   |   15   |  517   |
| 2019-11-27 18:28:13 | 24682 |  5.72G   |   36.87%   |   15   |  517   |
| 2019-11-27 19:28:13 | 24682 |  5.73G   |   36.94%   |   15   |  517   |
| 2019-11-27 20:28:13 | 24682 |  5.74G   |   36.99%   |   15   |  517   |
| 2019-11-27 21:28:13 | 24682 |  5.75G   |   37.03%   |   15   |  517   |
| 2019-11-27 22:28:13 | 24682 |  5.75G   |   37.08%   |   13   |  517   |
| 2019-11-27 23:28:13 | 24682 |  5.76G   |   37.15%   |   15   |  517   |
| 2019-11-28 00:28:13 | 24682 |  5.77G   |   37.19%   |   15   |  517   |
| 2019-11-28 01:28:13 | 24682 |  5.78G   |   37.24%   |   15   |  517   |
| 2019-11-28 02:28:13 | 24682 |  5.78G   |   37.28%   |   13   |  517   |
| 2019-11-28 03:28:13 | 24682 |  5.79G   |   37.33%   |   12   |  517   |
| 2019-11-28 04:28:13 | 24682 |  5.80G   |   37.38%   |   13   |  517   |
| 2019-11-28 05:28:13 | 24682 |  5.81G   |   37.42%   |   13   |  517   |
| 2019-11-28 06:28:13 | 24682 |  5.81G   |   37.47%   |   11   |  517   |
| 2019-11-28 07:28:13 | 24682 |  5.82G   |   37.51%   |   11   |  517   |
| 2019-11-28 08:28:13 | 24682 |  5.83G   |   37.57%   |   13   |  517   |
| 2019-11-28 09:28:13 | 24682 |  5.84G   |   37.64%   |   15   |  517   |
+---------------------+-------+----------+------------+--------+--------+
Jvm内存信息:
+---------------------+-------+-------+-------+-------+-------+-------+-------+---------+-----+------+---------+
|       记录时间      |   S0  |   S1  |   E   |   O   |   M   |  CCS  |  YGC  |   YGCT  | FGC | FGCT |   GCT   |
+---------------------+-------+-------+-------+-------+-------+-------+-------+---------+-----+------+---------+
| 2019-11-27 16:28:13 |  0.0  | 14.43 | 41.45 | 59.42 | 95.96 | 93.43 | 38415 | 614.954 |  0  | 0.0  | 614.954 |
| 2019-11-27 17:28:13 |  0.0  | 11.19 | 29.53 | 59.57 | 95.96 | 93.43 | 38517 | 616.434 |  0  | 0.0  | 616.434 |
| 2019-11-27 18:28:13 |  11.2 |  0.0  | 38.92 |  59.7 | 95.97 | 93.43 | 38616 | 617.902 |  0  | 0.0  | 617.902 |
| 2019-11-27 19:28:13 | 10.49 |  0.0  | 28.44 | 59.85 | 95.97 | 93.43 | 38716 | 619.365 |  0  | 0.0  | 619.365 |
| 2019-11-27 20:28:13 |  0.0  | 10.53 | 49.32 | 59.94 | 95.97 | 93.43 | 38807 | 620.723 |  0  | 0.0  | 620.723 |
| 2019-11-27 21:28:13 |  0.0  | 10.54 | 66.89 | 60.04 | 95.97 | 93.43 | 38899 | 622.082 |  0  | 0.0  | 622.082 |
| 2019-11-27 22:28:13 | 11.13 |  0.0  | 98.58 | 60.14 | 95.97 | 93.43 | 38992 | 623.466 |  0  | 0.0  | 623.466 |
| 2019-11-27 23:28:13 |  10.7 |  0.0  | 21.67 | 60.26 | 95.97 | 93.43 | 39088 | 624.876 |  0  | 0.0  | 624.876 |
| 2019-11-28 00:28:13 | 11.34 |  0.0  | 86.74 | 60.35 | 95.97 | 93.43 | 39178 | 626.205 |  0  | 0.0  | 626.205 |
| 2019-11-28 01:28:13 |  0.0  |  10.3 | 91.25 | 60.45 | 95.97 | 93.43 | 39269 | 627.541 |  0  | 0.0  | 627.541 |
| 2019-11-28 02:28:13 |  0.0  |  9.87 | 36.54 | 60.54 | 95.97 | 93.43 | 39361 |  628.92 |  0  | 0.0  |  628.92 |
| 2019-11-28 03:28:13 | 10.69 |  0.0  | 46.49 | 60.64 | 95.97 | 93.43 | 39452 | 630.283 |  0  | 0.0  | 630.283 |
| 2019-11-28 04:28:13 |  0.0  | 10.68 | 71.99 | 60.73 | 95.97 | 93.43 | 39543 | 631.632 |  0  | 0.0  | 631.632 |
| 2019-11-28 05:28:13 | 10.67 |  0.0  | 91.37 | 60.82 | 95.97 | 93.43 | 39634 | 633.013 |  0  | 0.0  | 633.013 |
| 2019-11-28 06:28:13 | 10.03 |  0.0  | 24.41 | 60.92 | 95.97 | 93.43 | 39726 | 634.391 |  0  | 0.0  | 634.391 |
| 2019-11-28 07:28:13 |  0.0  | 10.53 |  4.57 | 61.01 | 95.97 | 93.43 | 39817 | 635.751 |  0  | 0.0  | 635.751 |
| 2019-11-28 08:28:13 |  0.0  | 11.19 | 35.31 | 61.11 | 95.97 | 93.43 | 39909 | 637.099 |  0  | 0.0  | 637.099 |
| 2019-11-28 09:28:13 |  0.0  | 13.81 | 81.63 | 61.26 | 95.98 | 93.43 | 40019 | 638.759 |  0  | 0.0  | 638.759 |
+---------------------+-------+-------+-------+-------+-------+-------+-------+---------+-----+------+---------+
****************************************************************************************************
备份统计:
备份(/backup)统计信息:
+---------------------+----------------------+---------+---------------------+
|       记录时间      |       备份文件       |   大小  |       创建时间      |
+---------------------+----------------------+---------+---------------------+
| 2019-11-28 02:10:00 | dsfa-20191121.sql.gz | 331.25M | 2019-11-21 02:01:13 |
| 2019-11-28 02:10:00 | dsfa-20191122.sql.gz | 331.94M | 2019-11-22 02:01:05 |
| 2019-11-28 02:10:00 | dsfa-20191123.sql.gz | 333.11M | 2019-11-23 02:01:05 |
| 2019-11-28 02:10:00 | dsfa-20191124.sql.gz | 333.33M | 2019-11-24 02:01:05 |
| 2019-11-28 02:10:00 | dsfa-20191125.sql.gz | 333.57M | 2019-11-25 02:01:05 |
| 2019-11-28 02:10:00 | dsfa-20191126.sql.gz | 334.71M | 2019-11-26 02:01:05 |
| 2019-11-28 02:10:00 | dsfa-20191127.sql.gz | 335.15M | 2019-11-27 02:01:06 |
| 2019-11-28 02:10:00 | dsfa-20191128.sql.gz | 335.75M | 2019-11-28 02:01:06 |
+---------------------+----------------------+---------+---------------------+
****************************************************************************************************
MySQL统计:
****************************************************************************************************
启动信息:
+---------------------+------+------+---------------------+
|       记录时间      | Pid  | 端口 |       启动时间      |
+---------------------+------+------+---------------------+
| 2019-11-28 10:31:55 | 9373 | 3306 | 2019-08-14 10:31:50 |
+---------------------+------+------+---------------------+
运行信息:
+---------------------+------+----------+------------+--------+--------+
|       记录时间      | Pid  | 内存使用 | 内存使用率 | 连接数 | 线程数 |
+---------------------+------+----------+------------+--------+--------+
| 2019-11-27 16:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 17:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 18:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 19:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 20:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 21:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 22:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-27 23:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 00:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 01:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 02:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 03:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 04:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 05:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 06:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 07:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 08:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
| 2019-11-28 09:33:53 | 9373 |  6.95G   |   44.83%   |   1    |   42   |
+---------------------+------+----------+------------+--------+--------+
集群信息:
当前角色: slave
+---------------------+------+----------------+------------+------------+--------------+--------------+----------------------------------+---------------+--------------------------------------------------------+--------------------------------------+------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
|       记录时间      | Pid  |   Master主机   | Master端口 | 同步数据库 | 非同步数据库 | Slave_IO线程 |           Slave_IO状态           | Slave_SQL线程 |                     Slave_SQL状态                      |             Master_UUID              |                已接收的GTID集合                |                                    已执行的GTID集合                                    | Slave落后Master的秒数 |
+---------------------+------+----------------+------------+------------+--------------+--------------+----------------------------------+---------------+--------------------------------------------------------+--------------------------------------+------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
| 2019-11-28 10:31:55 | 9373 | 10.145.132.123 |    3306    |            |              |     Yes      | Waiting for master to send event |      Yes      | Slave has read all relay log; waiting for more updates | 588708d3-b383-11e9-84b0-00163e01081b | 588708d3-b383-11e9-84b0-00163e01081b:1-1725653 | 588708d3-b383-11e9-84b0-00163e01081b:1-1725653, 6b22d90b-b383-11e9-bce5-00163e010394:1 |           0           |
+---------------------+------+----------------+------------+------------+--------------+--------------+----------------------------------+---------------+--------------------------------------------------------+--------------------------------------+------------------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
****************************************************************************************************
慢日志信息:
请查看慢日志分析文件report/slow_analysis.log及慢日志文件report/slow.log
****************************************************************************************************
----------------------------------------------------------------------------------------------------
统计结束时间: 2019-11-28 10:18:00
```
