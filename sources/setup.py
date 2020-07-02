from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Flask==1.1.2', 'requests==2.24.0', 'Pillow==7.2.0', 'Flask-SQLAlchemy==2.4.3']
)
