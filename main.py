#主入口程序

def main_config(): #配置文件读取
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='UTF-8')

    main_controller = config.get('config_name','config-name')
    print(f"已读取文件:{main_controller}")

if __name__ == "__main__":
    print("[1]读取配置")
    print("[0]退出程序")
    while True:
        user_Input = input(">>>")
        if user_Input == ("1"):
            main_config()
        elif user_Input == ("0"):
            break


