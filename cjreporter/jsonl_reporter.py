import os
import json
from chainer.training import extensions


class LatestLog:

    def __init__(self):
        self._record = {}
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, idx):
        assert idx == self._size-1
        return self._record

    def update(self, record):
        self._record = record
        self._size += 1


class JsonlReport(extensions.LogReport):

    # TODO: fix args and kwargs
    def __init__(self, *args, **kwargs):
        super(JsonlReport, self).__init__(*args, **kwargs)
        self._initialized = {}
        self._latest_log = LatestLog()

    def _prepare_log_file(self, path):
        if path in self._initialized:
            return
        self._initialized[path] = True
        if os.path.exists(path):
            os.remove(path)

    def __call__(self, trainer):
        keys = self._keys
        observation = trainer.observation
        summary = self._summary

        if keys is None:
            summary.add(observation)
        else:
            summary.add({k: observation[k] for k in keys if k in observation})

        if self._trigger(trainer):
            stats = self._summary.compute_mean()
            stats_cpu = {}
            for name, value in stats.items():
                stats_cpu[name] = float(value)

            updater = trainer.updater
            stats_cpu['epoch'] = updater.epoch
            stats_cpu['iteration'] = updater.iteration
            stats_cpu['elapsed_time'] = trainer.elapsed_time

            self._latest_log.update(stats_cpu)

            if self._postprocess is not None:
                self._postprocess(stats_cpu)

            if self._log_name is not None:
                path = os.path.join(trainer.out, self._log_name)
                self._prepare_log_file(path)
                with open(path, 'a') as fp:
                    fp.write(json.dumps(stats_cpu) + '\n')

            self._init_summary()

    @property
    def log(self):
        return self._latest_log