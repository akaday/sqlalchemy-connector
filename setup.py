from setuptools import setup, find_packages

setup(
    name='sql_connector',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'psycopg2-binary',
        'mysql-connector-python',
    ],
    entry_points={
        'console_scripts': [
            'sql_connector=sql_connector.connector:main',
        ],
    },
)
