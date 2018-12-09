import argparse

import chainer.functions as F
import chainer.links as L
from chainer import Chain, datasets, optimizers, iterators
from chainer.training import Trainer, extensions
from chainer.training.updaters import StandardUpdater
from chainer_jsonl_report import JsonlReport


class MLP(Chain):

    def __init__(self, n_units, n_out):
        super(MLP, self).__init__()
        with self.init_scope():
            self.l1 = L.Linear(None, n_units)
            self.l2 = L.Linear(None, n_units)
            self.l3 = L.Linear(None, n_out)

    def forward(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batchsize', '-b', type=int, default=128)
    parser.add_argument('--epoch', '-e', type=int, default=20)
    parser.add_argument('--out', '-o', default='result')
    args = parser.parse_args()

    model = L.Classifier(MLP(128, 10))

    optimizer = optimizers.Adam()
    optimizer.setup(model)

    train, test = datasets.get_mnist()

    train_iter = iterators.SerialIterator(train, args.batchsize)
    test_iter = iterators.SerialIterator(
        test, args.batchsize, repeat=False, shuffle=False)

    updater = StandardUpdater(train_iter, optimizer, device=-1)
    trainer = Trainer(updater, (args.epoch, 'epoch'), out=args.out)

    trainer.extend(extensions.Evaluator(test_iter, model, device=-1))

    trainer.extend(JsonlReport())
    trainer.extend(extensions.PrintReport(
        ['epoch', 'main/loss', 'validation/main/loss',
         'main/accuracy', 'validation/main/accuracy', 'elapsed_time'],
        log_report='JsonlReport',
    ))
    trainer.extend(extensions.ProgressBar())

    trainer.run()


if __name__ == '__main__':
    main()
