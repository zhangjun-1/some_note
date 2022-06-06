#mysql数据库备份脚本
import os
import pymysql
import time

#定义变量
databases = ['test']            #要备份的数据库名
sql_host = 'localhost'
sql_user = 'root'              #数据库登录用户
sql_pwd = '123456'          #登录密码
bak_dir = '/root/sql_bak'           #存放sql文件的地址

#创建备份文件的目录
if not os.path.exists(bak_dir):         #判断如果没有目录
    os.mkdir(bak_dir)           #创建
print('创建目录成功：',os.path.abspath(bak_dir))           #打印创建成功

#开始备份到指定文件夹
os.chdir(bak_dir)           #改变当前工作目录到指定的路径
for database_name in databases:         #循环要备份的数据库列表
    today_sql = time.strftime('%Y%m%d') + '_' + database_name + '.sql'          #定义备份文件名变量
    sql_comm = 'mysqldump -u%s -p%s %s > %s' % (sql_user,sql_pwd,database_name,today_sql)       #编写备份命令
    if os.system(sql_comm) == 0:        #执行结果等于0表示成功
        print(database_name,' is backup successfully!')         #打印成功信息
        print('备份文件地址:',os.path.abspath('./')+today_sql)
    else:
        print(database_name,' is backup fail!')     #打印失败信息
