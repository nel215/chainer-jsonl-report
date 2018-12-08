build:
	python setup.py build bdist_wheel
clean:
	rm -rf build/ dist/
install: build
	pip install -U ./dist/chainer_jsonl_report-0.0.1-py3-none-any.whl
test: install
	pip install -U -r requirements.txt
	py.test --flake8 .
