#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

# file path
yml_file_path = '/opt/tomcat/roles/deploy_tomcat/vars/main.yml'
old_file_path = '/opt/tomcat/roles/deploy_tomcat/file/'
new_file_path = '/opt/tomcat/file/'
nginx_config_file_path = '/opt/tomcat/roles/copy_nginx_conf/template/nginx.conf'

# command
reload_nginx = 'ansible-playbook /opt/tomcat/reload_nginx.yml'
copy_nginx_conf = 'ansible-playbook /opt/tomcat/copy_nginx_conf.yml'

first_lv = ['1.block IP',
            '2.deploy tomcat',
            '3.restart tomcat']

nginx_lv = ['1.block IP 10.29.220.238',
            '2.block IP 10.29.221.8',
            '3.Disable block IP 10.29.220.238',
            '4.Disable block IP 10.29.221.8']
tomcat_lv = ['1.deploy first tomcat',
             '2.deploy second tomcat']
restart_lv = ['1.restart first tomcat',
              '2.restart second tomcat']

mapping1 = {'1.block IP': nginx_lv}
mapping2 = {'2.deploy tomcat': tomcat_lv}
mapping3 = {'3.restart tomcat': restart_lv}


def block_238():
    lines = open(nginx_config_file_path).readlines()
    if "        # server 10.29.220.238:18080 weight=100 max_fails=3 fail_timeout=5s;\n" not in lines:
        fp = open(nginx_config_file_path, 'w')
        for s in lines:
            fp.write(s.replace('server 10.29.220.238:18080 weight=100 max_fails=3 fail_timeout=5s;',
                               '# server 10.29.220.238:18080 weight=100 max_fails=3 fail_timeout=5s;'))
        fp.close()
        print("block 10.29.220.238 success!")
        print("reloading nginx service....")
        os.system(copy_nginx_conf)
        os.system(reload_nginx)
    else:
        print("has blocked")
        choise_num = input("need continue?\n1.yes\n2.no")
        if choise_num == '1':
            print("reloading nginx service....")
            os.system(copy_nginx_conf)
            os.system(reload_nginx)
        elif choise_num == '2':
            exit(-1)
        else:
            print("input error!")
            exit(-1)


def block_8():
    lines = open(nginx_config_file_path).readlines()
    if "        # server 10.29.221.8:18080 weight=100 max_fails=3 fail_timeout=5s;\n" not in lines:
        fp = open(nginx_config_file_path, 'w')
        for s in lines:
            fp.write(s.replace('server 10.29.221.8:18080 weight=100 max_fails=3 fail_timeout=5s;',
                               '# server 10.29.221.8:18080 weight=100 max_fails=3 fail_timeout=5s;'))
        fp.close()
        print("block 10.29.221.8 success!")
        print("reloading nginx service....")
        os.system(copy_nginx_conf)
        os.system(reload_nginx)
    else:
        print("has blocked")
        choise_num = input("need continue?\n1.yes\n2.no")
        if choise_num == '1':
            print("reloading nginx service....")
            os.system(copy_nginx_conf)
            os.system(reload_nginx)
        elif choise_num == '2':
            exit(-1)
        else:
            print("input error!")
            exit(-1)


def dis_block_238():
    lines = open(nginx_config_file_path).readlines()
    if "        # server 10.29.220.238:18080 weight=100 max_fails=3 fail_timeout=5s;\n" in lines:
        lines = open(nginx_config_file_path).readlines()
        fp = open(nginx_config_file_path, 'w')
        for s in lines:
            fp.write(s.replace('# server 10.29.220.238:18080 weight=100 max_fails=3 fail_timeout=5s;',
                               'server 10.29.220.238:18080 weight=100 max_fails=3 fail_timeout=5s;'))
        fp.close()
        print("disable block 10.29.220.238 success!")
        print("reloading nginx service....")
        os.system(copy_nginx_conf)
        os.system(reload_nginx)
    else:
        print("has disable blocked")
        choise_num = input("need continue?\n1.yes\n2.no")
        if choise_num == '1':
            print("reloading nginx service....")
            os.system(copy_nginx_conf)
            os.system(reload_nginx)
        elif choise_num == '2':
            exit(-1)
        else:
            print("input error!")
            exit(-1)


def dis_block_8():
    lines = open(nginx_config_file_path).readlines()
    if "        # server 10.29.221.8:18080 weight=100 max_fails=3 fail_timeout=5s;\n" in lines:
        lines = open(nginx_config_file_path).readlines()
        fp = open(nginx_config_file_path, 'w')
        for s in lines:
            fp.write(s.replace('# server 10.29.221.8:18080 weight=100 max_fails=3 fail_timeout=5s;',
                               'server 10.29.221.8:18080 weight=100 max_fails=3 fail_timeout=5s;'))
        fp.close()
        print("disable block 10.29.221.8 success!")
        print("reloading nginx service....")
        os.system(copy_nginx_conf)
        os.system(reload_nginx)
    else:
        print("has disable blocked")
        choise_num = input("need continue?\n1.yes\n2.no")
        if choise_num == '1':
            print("reloading nginx service....")
            os.system(copy_nginx_conf)
            os.system(reload_nginx)
        elif choise_num == '2':
            exit(-1)
        else:
            print("input error!")
            exit(-1)


def deploy_tomcat():
    check_path_war = new_file_path + os.listdir(new_file_path)[0]
    if os.path.isfile(check_path_war) is True:
        file_path_name = os.listdir(old_file_path)[0]
        os.system("rm -rf  /opt/tomcat/roles/deploy_tomcat/file/*")
        os.system("cp -rp /opt/tomcat/file/* /opt/tomcat/roles/deploy_tomcat/file/ ")
        match_code = "local_file_src: file/"
        lines = open(yml_file_path).readlines()
        fp = open(yml_file_path, 'w')
        for s in lines:
            fp.write(s.replace(match_code + file_path_name, match_code + file_path_name))
        fp.close()
        print("copy tomcat finish....")
        os.system("ansible-playbook -t 192.168.74.129 /opt/tomcat/deploy_tomcat.yml")
    else:
        print("tomcat war file is not exist")
        exit(-1)


def restart_tomcat():
    print("restart tomcat")
    os.system('ansible-playbook -t 192.168.74.129 /opt/tomcat/restart_tomcat.yml')


def loop():
    print('exit')


break_flag = False
while True:
    if break_flag:
        break
    print(first_lv)
    first_choice = input('input.q，b\n')
    if first_choice == 'q' or first_choice == 'b':
        loop()
        break
    if first_choice == '1':
        while True:
            sec_lv = mapping1[first_lv[int(first_choice) - 1]]
            if break_flag:
                break
            print(sec_lv)
            nginx_choice = input('input，q，b\n')
            if nginx_choice == 'b':
                break
            if nginx_choice == 'q':
                loop()
                break_flag = True
                break
            if nginx_choice == '1':
                block_238()
                break
            if nginx_choice == '2':
                block_8()
                break
            if nginx_choice == '3':
                dis_block_238()
                break
            if nginx_choice == '4':
                dis_block_8()
                break
        break
    if first_choice == '2':
        while True:
            sec_lv = mapping2[first_lv[int(first_choice) - 1]]
            if break_flag:
                break
            print(sec_lv)
            tomcat_choice = input('inpu，q，b\n')
            if tomcat_choice == 'b':
                break
            if tomcat_choice == 'q':
                loop()
                break_flag = True
                break
            if tomcat_choice == '1':
                deploy_tomcat()
            if tomcat_choice == '2':
                deploy_tomcat()
        break
    if first_choice == '3':
        while True:
            sec_lv = mapping3[first_lv[int(first_choice) - 1]]
            if break_flag:
                break
            print(sec_lv)
            restart_tomcat_choice = input('input，q，b\n')
            if restart_tomcat_choice == 'b':
                break
            if restart_tomcat_choice == 'q':
                loop()
                break_flag = True
                break
            if restart_tomcat_choice == '1':
                restart_tomcat()
            if restart_tomcat_choice == '2':
                restart_tomcat()
        break