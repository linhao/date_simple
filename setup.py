from setuptools import setup

setup( name='date_simple',
       version='0.1',
       description='This module plays with datetime()',
       url='',                # usually a github URL
       author='Hao Lin',
       author_email='linhao@yahoo.com',
       license='MIT',
       packages=['date_simple'],
       install_requires=[ ],
       test_suite='pytest',
       setup_requires=['pytest-runner'],
       tests_require=['pytest'],
       zip_safe=False )