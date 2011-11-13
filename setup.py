#  author:renlu.xu@xiaoqianboa.com
# 
from distutils.core import setup,Extension
module = Extension('procname',sources = ['procnamemodule.c'])
setup (name = 'procname', version = '1.0', description = 'You can setup  name of the process;', ext_modules = [module])
