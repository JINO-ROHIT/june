from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="june-llm_agent",
    version="0.0.1",
    description="An LLM Agent that autonomously uses tools to perform actions",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JINO-ROHIT/june",
    author="Jino Rohit",
    author_email="find.jinorohit@gmail.com",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[
        "colorama==0.4.6",
        "pydantic==2.5.3",
        "python-dotenv==1.0.0",
        "PyYAML==6.0.1",
        "transformers==4.36.2",
        "torch==2.1.0",
        "accelerate==0.25.0",
        "bitsandbytes @ https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.1-py3-none-win_amd64.whl#sha256=adacda9b2b65dcb1931b222dffd7a91f0b611b3410d5b51c37ef7b22654106e6",
    ],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.9",
)