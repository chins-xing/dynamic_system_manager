#防火墙规则管理
import win32com.client

def run():
    try:
        fw_policy = win32com.client.Dispatch("HNetCfg.FwPolicy2")
        fw_rules = fw_policy.Rules
        print("已获取防火墙控制")
    except Exception as e:
        print(f"无法获取防火墙控制，错误信息为{e}")

def __init__(self):
    super().__init__()
    self.fw_policy = None
    self.fw_rules = None

def do_exit(self):
     return True