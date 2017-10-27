from setuptools import setup

setup(
    name='pandash',
    version='0.1.0',
    description='Convert Redash Query Result as Pandas DataFrame.',
    author='Takuya Arita',
    author_email='takuya.arita@gmail.com',
    url='https://github.com/ariarijp/pandash',
    packages=[
        'pandash',
    ],
    license='MIT',
    install_requires=[
        'pandas',
        'redash-dynamic-query',
    ],
)
