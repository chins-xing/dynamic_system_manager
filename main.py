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

    def do_SC(self,arg):
        core.service_controller.test()

    def do_GP(self,arg):
        core.group_policy.test()
    
    def do_FC(self,arg):
        core.firewall_controller.test()

    def do_help(self,arg):
        return super().do_help(arg)
    
    def do_exit(self,arg):
        return True
if __name__ == "__main__": #用户交互
    shell().cmdloop()