import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)
import legacyPkgMgr


installer = legacyPkgMgr.LegacyPackageMgr()



installer.install_packages(['hehe!'])

