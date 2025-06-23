from dask.distributed import Client, TimeoutError
import sys
import json

SCHEDULER_ADDRESS = "10.0.1.2:8786"

try:
    client = Client(SCHEDULER_ADDRESS, timeout="5s")

    info = client.scheduler_info()

    # No. of workers
    num_workers = len(info["workers"])
    print(f"Number of Dask workers connected to {SCHEDULER_ADDRESS}: {num_workers}")

    # Woker names
    workers = info["workers"]
    for worker in workers:
        print(worker)

    # Save worker info to file
    with open("workers.json", "w") as fd:
        json.dump(info, fd)

    client.close()
except TimeoutError:
    print(
        f"Error: Could not connect to Dask scheduler at {SCHEDULER_ADDRESS}. Is it running and accessible?",
        file=sys.stderr,
    )
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(1)
