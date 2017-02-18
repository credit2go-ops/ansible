#!/usr/bin/python3
import os

yml_file_path= '/opt/tomcat/roles/deploy_tomcat/vars/main.yml'
old_file_path= '/opt/tomcat/roles/deploy_tomcat/file/'
new_file_path= '/opt/tomcat/file/'

input_num=input("请输入需要的操作：\n 1.发布tomcat（不要忘记在file文件夹下复制新的war包）\n 2.重启tomcat服务\n 请输入选项： ")
if input_num == "1":
    print("发布tomcat ing....")
    check_path = new_file_path + os.listdir(new_file_path)[0]
    if os.path.isfile(check_path) == True:
        file_path_name = os.listdir(old_file_path)[0]
        os.system("rm -rf  /opt/tomcat/roles/deploy_tomcat/file/*")
        os.system("cp -rp /opt/tomcat/file/* /opt/tomcat/roles/deploy_tomcat/file/ ")
        match_code = "local_file_src: file/"
        lines = open(yml_file_path).readlines()
        fp = open(yml_file_path, 'w')
        for s in lines:
            fp.write(s.replace(match_code + file_path_name, match_code+file_path_name))
        fp.close()
        os.system("ansible-playbook push_tomcat.yml -k")
    else:
        print("请把文件放在file文件夹中")
        exit(-1)
elif input_num == "2":
    print("重启tomcat服务ing....")
    os.system("ansible-playbook restart_tomcat.yml -k")
else:
    print("输入错误!!!")

