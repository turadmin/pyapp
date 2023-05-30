from setuptools import setup

setup(
    name='hello_tur',
    version='1.0',
    py_modules=['hello_tur'],
    entry_points={
        'console_scripts': [
            'hello_tur = hello_tur:main',
        ],
    },
)
