
from setuptools import setup, find_packages

setup(
    name="roastmycode",
    version="0.1.0",
    description="A CLI tool to roast your code using AI.",
    author="RoastMaster",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
        "google-generativeai",
        "python-dotenv",
        "importlib-metadata; python_version < '3.10'"
    ],
    entry_points={
        "console_scripts": [
            "roast=roastmycode.cli:app",
        ],
    },
)
