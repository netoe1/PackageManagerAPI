import os

__MANAGER_DIRS = {
    "apk": {
        "config": "/etc/apk",
        "database": "/var/lib/apk"
    },
    "zypper": {
        "config": "/etc/zypp/zypp.conf",
        "database": "/var/lib/zypp"
    },
    "dnf": {
        "config": "/etc/dnf",
        "database": "/var/lib/dnf"
    },
    "apt": {
        "config": "/etc/apt",
        "database": "/var/lib/apt"
    },
    "pacman": {
        "config": "/etc/pacman.conf",
        "database": "/var/lib/pacman"
    }
}


def detect_package_manager():
  try:

    vector = ['apk','apt','pacman','dnf','zypper']

    for element in vector:
        if(os.path.exists(__MANAGER_DIRS[element]['config'])):
           return element
        
    raise Exception('Your package manager doesn\'t exist o isn\'t supported yet.')
  except Exception as e:
    return f"[PackageManager-err]: {e}"

def valid_buf(buffer):
    try:
        buffer = str(buffer)
        if(buffer == None or buffer == ''):
           raise Exception(' You didn\'t set a valid buffer for usage!')
    except Exception as e:
        print(f'[internal-package-manager-err]:{e}')