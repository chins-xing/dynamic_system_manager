#防火墙规则管理
import win32com.client
import cmd

class shell(cmd.Cmd):
        prompt = (">>>@FW:")
        intro = ("防火墙规则修改模块已启动")
    
        def do_run(self,arg):
            try:
                fw_policy = win32com.client.Dispatch("HNetCfg.FwPolicy2")
                fw_rules = fw_policy.Rules
                print("已获取防火墙控制")
            except Exception as e:
                print(f"无法获取防火墙控制，错误信息为{e}")

        def do_exit(self,arg):
             return True

def test():
     shell().cmdloop()