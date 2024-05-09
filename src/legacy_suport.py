import subprocess

class __PacmanMgr:
    def list_packages(self):
        command = ["pacman", "-Q"]
        return self._execute_command(command)

    def add_package(self, package_name):
        command = ["pacman", "-S", package_name]
        return self._execute_command(command)

    def remove_package(self, package_name):
        command = ["pacman", "-R", package_name]
        return self._execute_command(command)

    def update_packages(self):
        command = ["pacman", "-Syu"]
        return self._execute_command(command)

    def _execute_command(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return None
        
class __ApkMgr:
    def list_packages(self):
        command = ["apk", "info"]
        return self._execute_command(command)

    def add_package(self, package_name):
        command = ["apk", "add", package_name]
        return self._execute_command(command)

    def remove_package(self, package_name):
        command = ["apk", "del", package_name]
        return self._execute_command(command)

    def update_packages(self):
        command = ["apk", "upgrade"]
        return self._execute_command(command)

    def _execute_command(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return None
        
class __ZypperMgr:
    def list_packages(self):
        command = ["zypper", "search", "--installed-only"]
        return self._execute_command(command)

    def add_package(self, package_name):
        command = ["zypper", "install", package_name]
        return self._execute_command(command)

    def remove_package(self, package_name):
        command = ["zypper", "remove", package_name]
        return self._execute_command(command)

    def update_packages(self):
        command = ["zypper", "update"]
        return self._execute_command(command)

    def _execute_command(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return None

