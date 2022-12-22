from setuptools import setup

setup(
    name="soccershooters",
    version="1.0.0",
    packages=["src"],
    install_requires=["pygame"],
    entry_points={"console_scripts": ["soccershooters=src.main:main"]},
)