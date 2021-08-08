from setuptools import setup
setup(
    name = 'python-cli',
    version = '0.1.0',
    packages = ['helloworld'],
    entry_points = {
        'console_scripts': [
            'helloworld = helloworld.__main__:main'
        ]
    })
    #yum install python-typing
    #pip3 install packagename
    #python setup.py sdist bdist_wheel