#主入口程序
import cmd
import configparser
import core.service_controller
import core.group_policy
import core.firewall_controller

class shell(cmd.Cmd):
    prompt = ">>>"
    intro = "主程序启动"
    
    def do_config(self,arg):    #配置文件读取
        config = configparser.ConfigParser()
        config.read('config.ini',encoding='UTF-8')
        main_controller = config.get('config_name','config-name')
        print(f"已读取文件:{main_controller}")    

    def do_DSC(self,arg):
        if arg == (""):
            print("请指定一个需要使用的模块。如需帮助，请输入DSC help")

        if arg == ("FWM"):
            core.firewall_controller.test()

        if arg == ("GPM"):
            core.group_policy.test()

        if arg == ("SCM"):
             core.service_controller.test()

        if arg ==("help"):
            print("DSC(动态安全控制类,包含三个基本模块)")
            print("FWM(基本模块,防火墙规则管理)")
            print("GPM(基本模块,组策略修改)")
            print("SCM(基本模块,系统服务控制)")
            print("")

    def do_help(self,arg):
        return super().do_help(arg)
    
    def do_test(self,arg):
        print(f"用户输入测试内容为:{arg}")

    def do_exit(self,arg):
        return True
if __name__ == "__main__": #用户交互
    shell().cmdloop()