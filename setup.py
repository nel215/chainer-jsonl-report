import pypandoc
from setuptools import setup
import chainer_jsonl_report

with open('./README.md') as fp:
    readme = pypandoc.convert_file('./README.md', 'rst')


setup(
    name='chainer-jsonl-report',
    version=chainer_jsonl_report.__version__,
    description='JSONL formatted LogReport extention for chainer.',
    long_description=readme,
    author='nel215',
    author_email='otomo.yuhei@gmail.com',
    url='https://github.com/nel215/chainer-jsonl-reporter',
    packages=['chainer_jsonl_report'],
    install_requires=[
        "chainer",
    ],
    keywords=['machine learning'],
)
