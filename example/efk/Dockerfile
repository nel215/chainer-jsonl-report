FROM python:3.7

RUN pip install chainer
RUN pip install -i https://test.pypi.org/simple/ chainer-jsonl-report
WORKDIR /root
ADD ./train.py ./

CMD python ./train.py
