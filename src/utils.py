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
    
    for manager, path in __MANAGER_DIRS.items():
      if os.path.exists(path):
        return manager
  except Exception as e:
    return f"[PackageManager-err]: {e}"
