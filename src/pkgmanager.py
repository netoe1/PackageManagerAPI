import apt_pkg
import dnf
import os

  
class PackageManager:

    __osPkgMgr = ""

    def __init__(self):
        self.__osPkgMgr = self.__detect_package_manager()

    def __detect_package_manager():
        try:
            package_managers = {
                "apt": "/usr/bin/apt-get",
                "dnf": "/usr/bin/dnf",
                "yum": "/usr/bin/yum",
                "pacman": "/usr/bin/pacman",
                "zypper": "/usr/bin/zypper",
                "apk": "/sbin/apk"
            }

            for manager, path in package_managers.items():
                if os.path.exists(path):
                    return manager

        except Exception as e:
            print("PackageManagerAPI:An error occurred during package manager detection:", e)

        return None
    
    def getPkgMgr(self):
        return self.__osPkgMgr
    
    def setPkgMgr(self,label): # Careful with this code, uses valid labels, else the class can't work properly.
        if(label != None):
            self.__osPkgMgr = str(label).strip().lower()
    
    def installPkg(self,pkg_name):
        if(self.__osPkgMgr == "dnf"):
            base = dnf.Base()
            base.fill_sack()
            try:
                base.install(pkg_name)
                base.resolve()
                base.do_transaction()
                print(f"The package {pkg_name} was installed successfully!")
            except dnf.exceptions.Error as e:
                print(f"Error to install package {pkg_name}: {e}")
        
        elif(self.__osPkgMgr == "apt"):
            cache = apt_pkg.Cache()
            if cache.get_pkg(pkg_name) is None:
                print(f"Package \'{pkg_name}\'wasn't found. ")
                return
            
            pkg = cache[pkg_name]
            if pkg.current_state != apt_pkg.CURSTATE_NOT_INSTALLED:
                print(f"Package {pkg_name} is already installed.")
                return
            
            apt_pkg.init_system()
            cache.update()
            cache.open()
            
            try:
                pkg.mark_install()
                cache.commit()
                print(f"Package {pkg_name} installed with success.")
            except SystemError as e:
                print(f"Error to install package {pkg_name}: {e}")
        else:
            try:
                raise Exception("Your package manager isn't supported yet.")
            except Exception as error:
                print("PackageManagerAPI:" + str(error))
        
        """
        elif(self.__osPkgMgr == "yum"):
        elif(self.__osPkgMgr == "pacman"):
        elif(self.__osPkgMgr == "zypper"):
        """

    def removePkg(self,pkg_name):
        if(self.__osPkgMgr == 'dnf'):
            try:
                base = dnf.Base()
                base.read_all_repos()
                base.remove(pkg_name)
                base.resolve()
                base.download_packages(base.transaction.install_set)
                base.do_transaction()

            except dnf.exceptions.Error as e:
                print("An error occurred when finalizing the transaction.", e)

            finally:
                if base:
                    base.close()

        elif(self.__osPkgMgr == 'apt'):  
            try:
                apt_pkg.init()
                cache = apt_pkg.Cache()
                if cache[pkg_name].is_installed:
                    cache[pkg_name].mark_delete()
                    cache.commit()
                    print(f'The package "{pkg_name}" was removed successfully.')
                else:
                    print(f'The package "{pkg_name}" is not installed.')
            except Exception as e:
                print("An error occurred while removing the package", e)
            finally:
                apt_pkg.cleanup()

    def searchPkg(self,pkg_name = None):
        if(pkg_name != None):
            if(self.__osPkgMgr == 'apt'):
                try:
                    apt_pkg.init_config()
                    apt_pkg.init_system()

                    cache = apt_pkg.Cache()
                    cache.open()
                    package_list = []

                    for pkg in cache.packages:
                        if pkg_name in pkg.name:
                            package_list.append(pkg)

                    cache.close()
                    return package_list
                except Exception as e:
                    return f"Error: {e}"
            elif(self.__osPkgMgr == 'dnf'):
                try:
                    base = dnf.Base()
                    base.read_all_repos()
                    base.fill_sack(load_system_repo=True, load_available_repos=True)
                    package_list = []
                    for package in base.sack.query().filter(name=pkg_name):
                        package_list.append(package)
                    base.close()
                    return package_list
                except Exception as e:
                    return f"Error: {e}"
        
