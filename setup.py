import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pms7003",
    version="1.0.0",
    author="Tomasz Lewicki",
    author_email="t.w.lewicki@gmail.com",
    description="A python driver for plantower pms7003 pm sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomek-l/pms7003",
    packages=setuptools.find_packages(),
    install_requires=[
          'pyserial',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
