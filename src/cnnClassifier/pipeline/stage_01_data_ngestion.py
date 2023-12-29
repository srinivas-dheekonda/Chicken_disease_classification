from cnnClassifier.config.configuration import configurationmanager
from cnnClassifier.components.data_ingestion import DataIngesion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationmanager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngesion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extrct_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e