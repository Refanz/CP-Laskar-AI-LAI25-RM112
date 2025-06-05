import logging

def show_log(module_name):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s}")
    logger = logging.getLogger(module_name)

    return logger