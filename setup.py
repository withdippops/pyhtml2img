from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="pyhtml2img",
    version="0.0.1",
    author="Odilon Koutou",
    author_email="odilon@withdipp.com",
    description="A package to convert your HTML to Image",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pyhtml2img/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)