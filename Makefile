.PHONY: verify benchmark-all tables clean

verify:
	python -m pytest tests/ -v

benchmark-all:
	python scripts/run_all_benchmarks.py --seed 42 --out results/metrics.json
	python scripts/make_tables.py --in results/metrics.json --out results/tables.md
	pip freeze > results/env-freeze.txt
	cat results/tables.md

tables:
	python scripts/make_tables.py --in results/metrics.json --out results/tables.md

clean:
	rm -rf results/metrics.json results/tables.md __pycache__ .pytest_cache
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
