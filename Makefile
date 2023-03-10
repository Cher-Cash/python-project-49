build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

install:
	poetry install

brain-games:
	poetry run brain-games

update:
	pip install --user --force-reinstall dist/hexlet_code*.whl

lint:
	poetry run flake8 brain_games

delete:
	python3 -m pip uninstall hexlet-code
