from setuptools import setup, find_packages

setup(
    name='kasm_compiler',
    version='0.1',
    description='A simple compiler for the Kasm assembly language.',
    author='Steven Klinefelter',
    author_email='klinefelters@etown.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'attrs',
        'coloredlogs'
    ],
    entry_points={
        'console_scripts': [
            'kasm=kasm_compiler.__main__:main',
        ],
    },
)