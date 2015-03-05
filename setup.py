from setuptools import setup, find_packages


install_requires = [
    'ujson==1.33',
    'pandas==0.15.2',
    'requests==2.5.3',
    'beautifulsoup4==4.3.2',
    'ipython==3.0.0',
    'scrapy==0.24.5',
]


setup(
    name = 'dmenergy',
    version = '0.1.0',
    description = 'DMEnergy: Data Mining in energy',
    author = 'Gabor Nagy',
    author_email = "nagy.gabor.i@gmail.com",
    url = "https://github.com/enbritely/logragate",
    packages = find_packages(),
    install_requires = install_requires,
    include_package_data=True,
)
