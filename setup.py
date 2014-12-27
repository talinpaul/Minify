try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'It is supposed to carry out few optimizations on a CSS, Javascript Files.',
    'author': 'Talin Paul',
    'url': 'Not yet...',
    'download_url': 'Not yet...',
    'author_email': 'talinpaul@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Minify'],
    'scripts': [],
    'name': 'Minify'
}

setup(**config)
