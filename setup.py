#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()


test_requirements = [
    "pytest>=3",
]

setup(
    author="zhangxuyi",
    author_email="fyman.zhang@gmail.com",
    python_requires=">=3.9.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9.6",
    ],
    description="乾照报警服务",
    entry_points={
        "console_scripts": ["simc=compiler:main"],
    },
    install_requires=["anytree"],
    license="MIT license",
    long_description=readme + "\n\n",
    include_package_data=True,
    keywords="simple-c-compiler",
    name="simple-c-compiler",
    packages=find_packages(include=["modules"]),
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
)
