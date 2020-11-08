from setuptools import setup, find_packages

requires = [
    'click'
]

setup(
    name='OFD receipts analyzer',
    version='0.1',
    description='Parses receipts in json format, exported from iOS app "Проверка чеков ФНС России" (by nalog.ru)',
    classifiers=[
        'Programming Language :: Python',
    ],
    author='atronah',
    author_email='atronah.ds@gmail.com',
    keywords='python ofd fns nalog.ru receipt parser',
    packages=find_packages(),
    install_requires=requires,
)