from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='1.0.0',
    description='Very useful clean code',
    url='https://github.com/Iryna-Lytvynchuk/goit-python',
    author='Lytvynchuk Iryna',
    author_email='irinalytvinchuks@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean=clean_folder.clean:main']}
)
