import os
import sys
import getopt

from beacon import core
from beacon import update
from beacon import models
from beacon import venv


def readme():
    """
    help
    """
    print
    print("OPTIONS")
    print("可选项")
    print("\t-h --help")
    print("\t     Display this help.")
    print("\t     显示这个帮助.")
    print("\t-m --main")
    print("\t-u --update")
    print
    print("AUTHOR")
    print("作者")
    print("\t52&androllen")

    sys.exit(0)


def home():
    """
    entry
    """
    current_script_path = os.path.abspath(__file__)

    # 获取当前脚本所在的目录
    current_script_dir = os.path.dirname(current_script_path)
    current_script_dir = current_script_dir.removesuffix("beacon")
    current_script_dir = current_script_dir.removesuffix("\\")

    sys.path.append(current_script_dir)
    output = os.path.join(current_script_dir, "output")
    pyd = os.path.join(current_script_dir, "mineru.cp310-win_amd64.pyd")
    main = os.path.join(current_script_dir, "main.exe")
    run = os.path.join(current_script_dir, "run.py")
    run_setIP = os.path.join(current_script_dir, "setIP.bat")
    run_setup = os.path.join(current_script_dir, "setup.bat")
    run_upgrade = os.path.join(current_script_dir, "upgrade.bat")

    if os.path.exists(pyd):
        os.remove(pyd)

    if os.path.exists(main):
        os.remove(main)

    if os.path.exists(run):
        os.remove(run)

    if os.path.exists(run_setIP):
        os.remove(run_setIP)

    if os.path.exists(run_setup):
        os.remove(run_setup)

    if os.path.exists(run_upgrade):
        os.remove(run_upgrade)

    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(
            argv,
            "hlmu:v:a:",
            ["help", "load", "models", "update=", "venv=", "address="],
        )
    except getopt.GetoptError as err:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            readme()
        elif opt in ("-l", "--load"):
            os.system(f"echo 使用期间控制台禁止关闭~")
            if not len(os.listdir(output)):
                os.system(f"echo 第一次加载，时间比较慢，请稍等~")

            core()

        elif opt in ("-u", "--update"):
            update(arg)
            os.system(f"echo 升级成功~")
            os.system("pause")
        elif opt in ("-v", "--venv"):
            venv(arg)
            os.system("pause")
        elif opt in ("-a", "--address"):
            os.system(f"echo 使用期间控制台禁止关闭~")
            if not len(os.listdir(output)):
                os.system(f"echo 第一次加载，时间比较慢，请稍等~")

            core(arg)
        elif opt in ("-m", "--models"):
            models()
            os.system("pause")
        else:
            assert False, "未知选项"


if __name__ == "__main__":
    home()
