from setuptools import setup, find_packages

setup(
    name="jcds",
    version="0.2.1",
    author="Jun Clemente",
    description="Jun Clemente’s Data Science helper library for EDA, visualization, and analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically finds all jcds submodules
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "ipython", 
        "scikit-learn"
    ],
    extras_require={
        'aws': [
        "boto3", 
        "botocore"

        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
