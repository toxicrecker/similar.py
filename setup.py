import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="setup.py",
    version="1.0",
    author="toxicrecker",
    description="Find similar text easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/toxicrecker/similar.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=[]
)