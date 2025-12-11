from setuptools import setup, find_packages

setup(
    name='frcshow',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],  # requirements.txt
    entry_points={
        'console_scripts': [
            'frcshow=frcshow.main:main',
        ],
    },
    author='phorensic',
    author_email='phorensic@pm.me',
    description='Simple tool to show data of project in Firebase Remote Config',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/phor3nsic/frcshow',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
