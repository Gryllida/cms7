from setuptools import setup

setup(
    name='cms7',
    version='0.1a11',
    description='Simple static site generator',
    author='Ed Kellett',
    author_email='e@kellett.im',
    url='https://github.com/edk0/cms7',
    packages=['cms7', 'cms7.modules'],
    install_requires=[
        'colorlog',
        'clize',
        'html5lib',
        'jinja2',
        'markdown',
        'pathlib2',
        'python-dateutil',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'cms7 = cms7.cli:main'
        ]
    }
)
