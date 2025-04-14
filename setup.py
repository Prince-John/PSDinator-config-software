from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='chipboard_configuration_software',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src/', include=['chipboard_configuration_software.uart_link']),   # Automatically discover all packages
    install_requires=[
    ],
    description='Test 2 PSD config software package',
    author='prince',
    author_email='johnp@wustl.edu',
)

