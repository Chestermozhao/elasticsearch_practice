<h1 align="center">Elasticsearch Python Practice</h1>

<p align="center">
<a href="https://github.com/psf/black">
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

<img src="https://github.com/Chestermozhao/elasticsearch_practice/blob/master/demo.gif" width=100% />

```shell
# Backend
cd backend
python3 -m venv venv

# optional: requirements with poetry
pip install poetry;poetry install

# install pre-commit
pip install pre-commit
pre-commit install

# Frontend
cd frontend
npm install
# just for dev environment, plz using build at prod environment
npm run dev
```

1. Frontend
  - next.js
  - Using [unDraw](https://undraw.co/?fbclid=IwAR2WAsw_6Mt8N8cFB2KwjAB0_axgo_G8YSY5-wzjKeV9qwxvTudD6MtH938) svg image

2. Backend
  - Python3.6+
  - Using Black for pre-commit
  - Elasticsearch 7.5: About Installation [Document](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
