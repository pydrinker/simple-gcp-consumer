# simple-gcp-consumer
Consume an GCP Subscriber with [Pydrinker](https://github.com/rafaelhenrique/pydrinker)

# Install

```
$ pip install poetry
$ poetry shell
$ poetry install
```

# Configure

```
$ cp env-sample .env
```

Open .env and fill in the requested values. You may need a 'credential.json' file of a Service account from GCP, to create and download that follow this [instructions](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console).


# Running

```
$ export GOOGLE_APPLICATION_CREDENTIALS="credential.json"
$ poetry run python -m gcp_consumer
```

Add messages on topic/subscription and see how it works!
Adjust print_handler and error_handler for your purpouses.
