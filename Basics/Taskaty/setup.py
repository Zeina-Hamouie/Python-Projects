from setuptools import setup, find_packages

setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line task app written in Python.',
    author='Zeina Hamouie',
    packages=find_packages(),  # يبحث تلقائياً عن مجلدات تحتوي __init__.py
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'taskaty=taskaty.app:main',
        ],
    },
    python_requires='>=3.7',
)