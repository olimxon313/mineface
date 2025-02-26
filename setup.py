from setuptools import setup, find_packages

setup(
    name="mineface",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "pillow"
    ],
    author="Olimxon",
    description="Библиотека для превращения лица в Minecraft-стиль",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/olimxon313/mineface",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
