import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.2"

REPO_NAME = "transaction_monitoring"
AUTHOR_USER_NAME = "aoorogun"
SRC_REPO = "transaction_monitoring"
AUTHOR_EMAIL = "info@oaorgun.co.uk"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "multimodal TM",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages= setuptools.find_packages(where="src")
)
