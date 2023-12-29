import os
from urllib.request import request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngesionConfig
from pathlib import Path


class DataIngesion:
    def __init__(self, config = DataIngesionConfig):
        self.config = config
        

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file

            )

            logger.info(f"{filename} download with following info: \n{headers}")

        else:
            logger.info(f"file already exists of size : {get_size(Path(self.config.local_data_file))}")



        

        def extrct_zip_file(self):
            """
            zip_file_path:str
            extracts the zip file into the data directory
            function returns none
            """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

