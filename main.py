#主入口程序

def main_config(): #配置文件读取
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='UTF-8')

    main_controller = config.get('config_name','config-name')
    print(f"已读取文件:{main_controller}")

def main_help(): #基础帮助
    print("-----------------------------------")
    print("[help]帮助界面")
    print("[1]读取配置")
    print("[2]应用配置文件")
    print("[0]退出程序")
    print("-----------------------------------")
def main_help_shell(): #help帮助
    print("-----------------------------------")
    print("这是帮助界面")
if __name__ == "__main__": #用户交互
    while True:
        main_help()
        user_Input = input(">>>")
        if user_Input == ("1"):
            main_config()
        elif user_Input == ("help"):
            main_help_shell()
        elif user_Input == ("2"):
            print("-----------------------------------")
            print("[1]系统服务控制")
            print("[2]组策略修改")
            print("[3]防火墙规则管理")
            print("[0]上一级")
            print("-----------------------------------")
            while True:
                user_Input_2 = input(">>>")
                if user_Input_2 == ("1"):
                    import core.service_controller
                    core.service_controller.test()
                elif user_Input_2 == ("2"):
                    import core.group_policy
                elif user_Input_2 == ("3"):
                    import core.firewall_controller
                elif user_Input_2 == ("0"):
                    break
        elif user_Input == ("0"):
            break


