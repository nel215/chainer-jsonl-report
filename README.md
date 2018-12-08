# About

JSONL formatted LogReport extention for chainer.

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
