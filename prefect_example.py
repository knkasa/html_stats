# https://python.plainenglish.io/i-accidentally-built-a-10x-faster-etl-empire-with-7-python-libraries-youve-never-used-8be7dd02fafc
# Allows to setup function with pipeline.  Auto-logging, retry built-in.

from prefect import flow, task

# Define tasks
@task
def extract():
    data = [1, 2, 3, 4, 5]
    print("Extracted:", data)
    return data

@task
def transform(data):
    transformed = [x * 10 for x in data]
    print("Transformed:", transformed)
    return transformed

@task
def load(data):
    print("Loaded into target system:", data)

# Define flow
@flow
def etl_flow():
    raw = extract()
    clean = transform(raw)
    load(clean)

if __name__ == "__main__":
    etl_flow()
