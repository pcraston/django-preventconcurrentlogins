import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-preventconcurrentlogins',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django'],
    license='MIT License',
    description='Django middleware that prevents multiple concurrent logins.',
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    url='https://github.com/pcraston/django-preventconcurrentlogins',
    author='Patrick Craston',
    author_email='patrick@craston.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)