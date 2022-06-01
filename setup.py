from setuptools import setup, find_packages


setup(
    name="api",
    version="0.1.0",
    install_requires=[
        "fastapi==0.60.1",
        "httpx==0.23.0",
        "pydantic==1.6.1",
        "uvicorn==0.11.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
)
