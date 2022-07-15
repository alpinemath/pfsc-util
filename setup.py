import setuptools

with open("README.md", "r") as fh:
    long_description = ''.join(fh.readlines()[1:])

setuptools.setup(
    name="pfsc-util",
    version="0.22.7",
    url="https://github.com/alpinemath/pfsc-util",
    license="Apache 2.0",
    description="Proofscape Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
