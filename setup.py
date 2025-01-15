# setup.py

from setuptools import setup, find_packages

setup(
    name='aruco_stl',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'numpy-stl',
    ],
    description='A module to generate ArUco markers and convert them into STL files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lorenzo Capponi',
    author_email='your.email@example.com',
    url='https://github.com/LolloCappo/aruco_stl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
