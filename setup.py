from setuptools import setup, find_packages

setup(
    name='onedecimaloutput',
    version='1.0.0',
    description='Converts all float numbers in the output of a Python script to one decimal place',
    packages=find_packages(),
    install_requires=[
        'setuptools>=58.0.4',
    ],
    python_requires='>=3.6',
)
