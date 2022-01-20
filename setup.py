from setuptools import setup, find_packages

setup(
    name='kyb',
    version=open('VERSION').read().strip(),
    author='ShellSlau',
    install_requires=[
        'zerog@git+https://github.com/tiptapinc/zerog.git@0.0.37#egg=zerog',
        'marshmallow-jsonschema',
        'pytest',
        'pytest-cov',
        'pytest-tornado'
    ],
    packages=find_packages(exclude=["tests"])
)
