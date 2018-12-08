[![Build Status](https://travis-ci.org/nel215/chainer-jsonl-report.svg?branch=master)](https://travis-ci.org/nel215/chainer-jsonl-report)

# About

JSONL formatted LogReport extention for chainer.

# Installation

```
$ pip install chainer-jsonl-report
```

# Usage

```python3
from chainer_jsonl_report import JsonlReport
...
trainer.extend(JsonlReport())
trainer.extend(extensions.PrintReport(
    ['epoch', 'main/loss', 'validation/main/loss'],
    log_report='JsonlReport',
))
```
