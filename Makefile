.PHONY: run

run:
	gunicorn -c app/gunicorn_config.py run:app

.PHONY: debug

debug:
	gunicorn -c app/gunicorn_config.py --log-level debug run:app

.PHONY: bare-run

bare-run:
	gunicorn -b 0.0.0.0:8000 run:app

.PHONY: 
