from setuptools import setup, find_packages

setup(
    name='chipboard_config_software',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),   # Automatically discover all packages
    install_requires=[
    ],
    description='Test PSD config software package',
    author='prince',
    author_email='johnp@wustl.edu',
)