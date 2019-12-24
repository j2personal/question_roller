from setuptools import setup, find_packages

requires = [
    'flask',
]

setup(
    name='question-roller',
    version='0.0',
    description='An api',
    author='JJ',
    author_email='junjang17@gmail.com',
    keywords='web flask',
    packages="",
    include_package_data=True,
    install_requires=requires
)