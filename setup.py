import setuptools, pathlib

NAME = "hypergz"
URL = "https://github.com/AmitSheer/hypergz/"
HERE = pathlib.Path(__file__).parent
print(f"\nHERE = {HERE.absolute()}\n")
README = (HERE / "README.md").read_text()
REQUIRES = (HERE / "requirements.txt").read_text().strip().split("\n")
REQUIRES = [lin.strip() for lin in REQUIRES]
print(f'\nVERSION = {(HERE / "hypergz" / "VERSION").absolute()}\n')
VERSION = (HERE / "hypergz" / "VERSION").read_text().strip()

setuptools.setup(
    name=NAME,
    version=VERSION,

    # packages=setuptools.find_packages(exclude=["tests"]),
    packages=setuptools.find_packages(),
    install_requires=REQUIRES,

    long_description=README,
    long_description_content_type='text/markdown',

    url=URL,
    project_urls={
        'Documentation': URL,
        'Bug Reports': URL + '/issues',
        'Source Code': URL,
    },

    python_requires='>=3.8',
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 7 - Inactive',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
    ],

    include_package_data=True,
)

# Build:
#   Delete old folders: build, dist, *.egg_info, .venv_test.
#   Then run:
#        build
#   Or (old version):
#        python setup.py sdist bdist_wheel


# Publish to test PyPI:
#   twine upload --repository testpypi dist/*

# Publish to real PyPI:
#   twine upload --repository pypi dist/*


# Test in a virtual environment:
#    cd ..
#    virtualenv test_env
#    test_env\Scripts\activate
#    pip install numpy
#    pip install -i https://test.pypi.org/simple/ example-pypi-package-5782
#    pytest test_env\Lib\site-packages\examplepy