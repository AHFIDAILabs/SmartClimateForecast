from setuptools import setup, find_packages

setup(
    name='SmartClimateForecast',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi', 'uvicorn', 'pandas', 'numpy', 'scikit-learn', 'mlflow'
    ],
)
