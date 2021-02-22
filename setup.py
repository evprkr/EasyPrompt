import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='EasyPrompt',  
     version='0.1.6',
     author="Evan Parker",
     author_email="evanjparker@outlook.com",
     description="A simple prompt-style input library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/evprkr/EasyPrompt",
     keywords = ['command', 'input', 'prompt', 'easy'],
     packages=setuptools.find_packages(),
     python_requires='>=3.6',
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
