import os
import logging
import sys

# log_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
# log_file_format = f"{log_time}.log"

log_format = "[%(asctime)s : %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_path = os.path.join(log_dir, "running_logs.log")


os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger('kidney_disease_classifier')
