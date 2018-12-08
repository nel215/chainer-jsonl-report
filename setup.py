from setuptools import setup


setup(
    name='chainer-jsonl-report',
    version='0.0.1',
    description='JSONL formatted LogReport extention for chainer.',
    author='nel215',
    author_email='otomo.yuhei@gmail.com',
    url='https://github.com/nel215/chainer-jsonl-reporter',
    packages=['chainer_jsonl_report'],
    install_requires=[
        "chainer",
    ],
    keywords=['machine learning'],
)
