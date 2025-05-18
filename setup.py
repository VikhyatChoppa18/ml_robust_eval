import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml_robust_eval",

    version="0.1.6",

    author="Venkata Vikhyat Choppa",

    author_email="vikhyathchoppa699@gmail.com",


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