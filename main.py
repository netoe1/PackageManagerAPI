import sys
import os

# Obtenha o diretório atual do scrip
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)
import utils


ret = utils.detect_package_manager()
print(ret)