# 1.脚本共有3个文件夹及1个main脚本入口 #
    ConfigDir配置文件夹
    Core核心代码文件夹
    Log日志目录
# 2.配置文件： #
	SMTP：邮件配置相关信息
    database:为数据库配置
# 3.运行方式： #
    ①执行main.py脚本即可
    ②或者通过执行YunServices.py文件做成服务的方式
    （
      安装：python YunServices.py install
      启动：python YunServices.py start
      开机启动：python YunServices.py --startup auto install
      重启：python YunServices.py restart
      停止：python YunServices.py stop
      卸载：python YunServices.py remove
      ）