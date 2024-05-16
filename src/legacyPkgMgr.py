import os
import sys
import traceback
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)
import subprocess
import utils



class LegacyPackageMgr: 
    __legacy_support_dict = {
    "apk":{
        "install_packages"  :   "sudo apk add"          ,
        "remove_packages"   :   "sudo apk del"          ,
        "search_packages"   :   "sudo apk search"       ,
        "update_packages"   :   "sudo apk update"       ,
        "upgrade_packages"  :   "sudo apk upgrade"      ,
        "clear_cache"       :   "sudo apk cache clean"
    },
    "zypper":{
        "install_packages"  :   "sudo zypper install",
        "remove_packages"   :   "sudo zypper remove",
        "search_packages"   :   "sudo zypper search",
        "update_packages"   :   "sudo zypper update ",
        "upgrade_packages"  :   "sudo zypper upgrade ",
        "clear_cache"       :   "sudo zypper autoremove "
    },
    "pacman":{
        "install_packages"  :   "sudo pacman -S",
        "remove_packages"   :   "sudo pacman -Rns",
        "search_packages"   :   "sudo pacman -Ss",
        "update_packages"   :   "sudo pacman -U",
        "upgrade_packages"  :   "sudo pacman -Syu ",
        "clear_cache"       :   "sudo pacman -Scc"
    }
}

    __packageManager = 'undefined'
    def __init__(self):
        try:
            self.__packageManager = utils.detect_package_manager()
        except Exception as e:
            traceback.print_exc()
            sys.exit(1)

    def __exec_cmd(self,command):
        try:
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            if(output.returncode != 0):
                raise Exception(f'Error occured while running script in shell:{output.stderr}')
        except Exception as e:
            traceback.print_exc()
            sys.exit(1)

    def install_packages(self,packageList):    
        try:
            utils.valid_list(packageList)
            packages = ' '.join(packageList)
            if(not (self.__packageManager in self.__legacy_support_dict)):
                raise Exception('Your package manager isn\'t for legacy support , please use the modern class.')
            command = self.__legacy_support_dict[self.__packageManager]['install_package']
            command = command + ' ' + packages
            print(command)
        except Exception as e:
            traceback.print_exc()
            sys.exit(1)




   