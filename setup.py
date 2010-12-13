from setuptools import setup, find_packages

setup(
    name = "pidlock",
    version = "0.1",
    packages = find_packages(),
    test_suite = "pidlock.test",
    include_package_data = True,
    author = "Martin Marrese",
    author_email = "marrese@gmail.com",
    description = "Library that allow application launch lock based on pid",
)
