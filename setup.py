import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="ml_robust_eval",

    # version of the module
    version="1.3",

    # Name of Author
    author="Vekata Vikhyat Choppa",

    # your Email address
    author_email="vikhyathchoppa699@gmail.com",

    # #Small Description about module
    # description="adding number",

    # long_description=long_description,

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/VikhyatChoppa18",
    packages=setuptools.find_packages(),
    license="MIT",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)