import setuptools

with open('README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name='decorators-LOUIS-NAVARRO',
    version="0.01a1",
    author='Louis Navarro',
    description='Function decorators I made',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Louis-Navarro/decorators",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Natural Language:: English",
    ],
    python_requires='>=3.6',
)
