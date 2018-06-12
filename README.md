# cube_test


### 简介 
    使用使用Python mechanize库对百度和谷歌做周期性地模拟点击
    通过Python evenlet库克服mechanize连接失败时、程序无法退出的问题
    通过Python email库，在连接失败时发送邮件到指定邮箱

### 使用条件
    Python Library:
        mechanize
        eventlet
        email
        smtplib
        
### 文件介绍
     combine.py  : 加载english.txt中的单词进行模拟点击及邮件发送
     english.txt ：combine.py需要加载的单词脚本
     
### 运行程序  
    python combine.py

### 运行结果    

    一次查询结果
![image](https://github.com/scu-igroup/cube_test/blob/master/Images/3.png) 

    模拟点击失败后通过Python email库发送邮件通知
![image](https://github.com/scu-igroup/cube_test/blob/master/Images/1.png)
