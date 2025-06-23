from dask.distributed import Client
import time
import os.path
import os

import distributed_image_process as di

SCHEDULER_ADDRESS = "10.0.1.2:8786"


def process_img(input_path, output_dir, file_name):
    di.DA_brigthnessDecrease(
        input_path, os.path.join(output_dir, f"{file_name}_bright_dec.jpg")
    )
    di.DA_brigthnessIncrease(
        input_path, os.path.join(output_dir, f"{file_name}_bright_inc.jpg")
    )
    di.DA_contrastIncrease(
        input_path, os.path.join(output_dir, f"{file_name}_contrast_inc.jpg")
    )
    di.DA_contrastDecrease(
        input_path, os.path.join(output_dir, f"{file_name}_contrast_dec.jpg")
    )
    di.DA_flipVertical(
        input_path, os.path.join(output_dir, f"{file_name}_flip_vertical.jpg")
    )
    di.DA_flipHorizontal(
        input_path, os.path.join(output_dir, f"{file_name}_flip_horizontal.jpg")
    )
    di.DA_gaussianBlur(
        input_path, os.path.join(output_dir, f"{file_name}_gaussian_blur.jpg")
    )
    di.DA_randomNoise(
        input_path, os.path.join(output_dir, f"{file_name}_random_noise.jpg")
    )
    di.DA_resize(input_path, os.path.join(output_dir, f"{file_name}_resized.jpg"))
    di.DA_heavyShapening(input_path, os.path.join(output_dir, f"{file_name}_sharp.jpg"))


if __name__ == "__main__":
    print(f"Connecting to Dask scheduler at {SCHEDULER_ADDRESS}...")
    try:
        client = Client(SCHEDULER_ADDRESS, timeout="10s")
        print(
            f"Successfully connected to Dask cluster. Dashboard: {client.dashboard_link}"
        )

        info = client.scheduler_info()
        print(f"Number of workers: {len(info["workers"])}")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        module_path = os.path.join(current_dir, "distributed_image_process.py")

        if os.path.exists(module_path):
            print(f"Uploading module: {module_path}")
            client.upload_file(module_path)
            print("Module uploaded successfully.")
        else:
            print(
                f"Warning: '{module_path}' not found. Ensure 'distributed_image_process.py' is in the same directory."
            )

        print("Waiting for the result...")
        start_time = time.time()

        local_input_path_base = "/home/betelgeuse/drives/smb/public/cd-image-proc/input"
        local_output_path_base = (
            "/home/betelgeuse/drives/smb/public/cd-image-proc/output"
        )

        worker_input_path_base = "/home/cd-vm/share/input"
        worker_output_path_base = "/home/cd-vm/share/output"

        futures = []
        for file in os.listdir(local_input_path_base):
            if os.path.isfile(os.path.join(local_input_path_base, file)):
                print(f"Submitting task for: {file}")
                worker_input_file_path = os.path.join(worker_input_path_base, file)

                future = client.submit(
                    process_img,
                    worker_input_file_path,
                    worker_output_path_base,
                    os.path.splitext(file)[0],
                )
                futures.append(future)

        client.gather(futures)

        end_time = time.time()

        print(f"\nFunction executed successfully!")
        print(
            f"Time taken to execute and retrieve result: {end_time - start_time:.2f} seconds"
        )

    except TimeoutError:
        print(
            f"Error: Could not connect to Dask scheduler at {SCHEDULER_ADDRESS}. ",
            end="\n\n",
        )
    except Exception as e:
        print(f"An error occurred: {e}", end="\n\n")
    finally:
        if "client" in locals() and client:
            print("Closing Dask client connection.")
            client.close()
