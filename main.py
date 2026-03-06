#主入口程序
def main_config(): #配置文件读取
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='UTF-8')

    main_controller = config.get('main','windows-config')
    print(f"获取配置信息:{main_controller}")

if __name__ == "__main__":
    main_config

