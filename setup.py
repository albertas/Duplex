from setuptools import setup, find_packages

setup(
    name = "eVirtuve",
    version = "1.0",
    url = 'http://github.com/albertas/Duplex',
    license = 'BSD',
    description = "Cooking recipe catalog",
    author = 'Albertas Gimbutas',
    packages = find_packages(''),
    package_dir = {'': ''},
    install_requires = ['setuptools'],
)
