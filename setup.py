import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
   name="indonesia-earthquake",
   version="0.1",
   author="Diki Saputra",
   author_email="dikimistak@gmail.com",
   description="the data of this project from BMKG | Meteorological, Climatological, and Geophysical Agency, "
               "latest earthquake",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/dikisaputra15/indonesia-latest-earthquake",
   project_urls={
       "website" : "selaicoding.com",
   },
   classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (gplv3)e",
            "Operating System :: OS Independent",
            "Development Status :: 5 - Production/Stable"
           ],
   packages=setuptools.find_packages(),
   python_requires=">=3.6",

)