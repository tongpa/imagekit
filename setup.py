from distutils.core import setup

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys
 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(name='imagekit',
      version='1.01.0',
      description="extend from pdfkit(0.5.0",
      
      author="Tong",
      #package_dir={'' : 'src'},
      #package_dir={'survey': ''},
     #packages=['logsurvey'],
     packages=find_packages(exclude=['ez_setup']),
     package_dir={'imagekit': 'imagekit'
                  },
      #py_modules=['logsurvey'],
      #packages=find_packages(exclude=['ez_setup']),
       
      include_package_data=True,
    
       
      zip_safe=True
      )