"""validationのファイルを読み込む関数"""
from logging import getLogger, INFO

# setting logging
logger = getLogger(__name__)
logger.setLevel(INFO)


def read_file(file_path) -> list:
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        list: _description_
    """
    with open(file_path, encoding="utf-8") as file:
        ex_outputs = file.read().splitlines()
        logger.info("ex outputs : %s", ex_outputs)

    return ex_outputs
