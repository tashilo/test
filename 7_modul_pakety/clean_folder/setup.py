from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="0.0.1",
    description="Script for clean folders and sort files",
    url="https://github.com/tashilo/test",
    author="Tatiana SHilo",
    author_email="zerkalo.tatiana@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'consol_scripts': ['clean-folder=clean_folder.clean:main']}
)