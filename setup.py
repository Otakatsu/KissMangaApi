import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name='kissmanga',
    version='1.0.9',
    description='An Unofficial Python API Library to Download Manga  for FREE...',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    author='otakatsu',
    author_email='moezilla@otakatsu.studio',
    url='https://github.com/otakatsu/kissmangaapi.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["bs4", "requests", "requests_html"],
    python_requires='>=3.6'
)
