from setuptools import setup, find_packages

setup(
    name="do_setup",
    version="1.0",
    keywords=("test", "xxx"),
    description="hello world",
    long_description="hello world from python",
    license="MIT Licence",

    url="http://test.com",
    author="test",
    author_email="test@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],

    scripts=[],
    entry_points={
        'console_scripts': [
            'test = __main__:main'
        ]
    }
)
