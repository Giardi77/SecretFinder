from setuptools import setup, find_packages

setup(
    name="secretfinder",
    version="1.0.0",
    author="m4ll0k",
    author_email="m4ll0k@example.com",
    description="Tool to discover API keys, access tokens, and sensitive data in JS files",
    long_description=open('README.md').read(),  # Include a README.md for detailed description
    long_description_content_type='text/markdown',
    url="https://github.com/m4ll0k/SecretFinder",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jsbeautifier',
        'requests',
        'requests-file',
        'lxml',
    ],
    entry_points={
        'console_scripts': [
            'secretfinder=secretfinder:main',  # Replace with your script's main function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
