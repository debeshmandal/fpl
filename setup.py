import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="fpl",
    version="0.1.0",
    author="Debesh Mandal",
    description="Fantasy API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['*test*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'tensorflow',
        'softnanotools'
    ],
    include_package_data = True
)
