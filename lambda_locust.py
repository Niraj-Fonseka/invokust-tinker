# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, "python-packages")

import logging
import json
import requests
from invokust.aws_lambda import get_lambda_runtime_info
from invokust import LocustLoadTest, create_settings

logging.basicConfig(level=logging.INFO)


def handler(event=None, context=None):
    url = "https://raw.githubusercontent.com/Niraj-Fonseka/invokust-tinker/master/invokust/locustfile.py"

    r = requests.get(url)
    with open("temp_locustfile.py", 'wb') as f:
        f.write(r.content) 

    logging.info("wrote file")

    try:
        if event:
            settings = create_settings(**event)
        else:
            settings = create_settings(from_environment=True)

        loadtest = LocustLoadTest(settings)
        loadtest.run()

    except Exception as e:
        logging.error("Locust exception {0}".format(repr(e)))

    else:
        locust_stats = loadtest.stats()
        lambda_runtime_info = get_lambda_runtime_info(context)
        loadtest_results = locust_stats.copy()
        loadtest_results.update(lambda_runtime_info)
        json_results = json.dumps(loadtest_results)

        logging.info(json_results)
        return json_results