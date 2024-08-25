from setuptools import setup

setup(
    name='Clarity-Tool',
    version='0.0.1',
    packages=[''
              'modules'],
    entry_points={
        'console_scripts': [
            'clarity-tool=main:main'
        ]
    },
    install_requires=[
        'pystyle',
        'requests'
    ],
    python_requires='>=3.12',
    url='',
    license='MIT',
    author='Alex',
    author_email='',
    description=''
)
