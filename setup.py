from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flask_session_azure',
    version='0.4.1',
    packages=['flask_session_azure'],
    url='https://github.com/claasd/FlaskAzureTableSession',
    license='MIT',
    author='Claas Diederichs',
    author_email='',
    description='Flask Session using Azure Table Storage or CosmosDB table API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "azure.storage==0.36.0",
        "pycryptodomex~=3.9.7",
        "flask"
    ]
)
