import setuptools

with open('README.md', 'r', encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-MLflow-DVC"
AUTHOR_NAME = 'harsharya'
SRC_REPO = "kidney_disease_classifier"
AUTHOR_EMAIL = "harsh.arya1004@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harsh-Arya-exe/Kidney-Disease-Classification",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
