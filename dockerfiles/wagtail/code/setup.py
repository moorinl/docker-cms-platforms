from setuptools import find_packages, setup


install_requires = [
    'django==1.11.1',
    'django-environ==0.4.1',
    'wagtail==1.10'
]

setup(
    name='application',
    version='0.1.0',
    description='My application short description.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    install_requires=install_requires,
    scripts=[
        'manage.py'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
