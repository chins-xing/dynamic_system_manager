import cmd
class testshell(cmd.Cmd):
    prompt =">>>"
    intro ="shell测试程序已启动"

    def do_chins(self,arg):
        print(f"命令测试成功,验证数据{arg}")

    def do_xing(self,arg):
        print(f"命令测试成功,验证数据{arg}")

    def do_exit(self,arg):
        return True
    
if __name__ == "__main__":
    testshell().cmdloop()
        
    