# Analytics Pipeline

This repo contains the code for creating a data pipeline to calculate metrics for a fake webserver:

* `log_generator.py` -- generates fake webserver logs.
* `store_logs.py` -- parses the logs and stores them in a SQLite database.
* `count_visitors.py` -- pulls from the database to count visitors to the site per day.

# Installation

To get this repo running:

* Install Python 3.  You can find instructions [here](https://wiki.python.org/moin/BeginnersGuide/Download).
* Create a [virtual environment](https://docs.python.org/3/library/venv.html).
* Clone this repo with `git clone git@github.com:dataquestio/analytics_pipeline.git`
* Get into the folder with `cd analytics_pipeline`
* Install the requirements with `pip install -r requirements.txt`

# Usage

* Execute the three scripts mentioned above, in order.

You should see output from `count_visitors.py`.

