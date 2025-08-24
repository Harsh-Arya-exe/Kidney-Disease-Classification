from kidney_disease_classifier.config.configuration import (
    ConfigurationManager)
from kidney_disease_classifier import logger
from kidney_disease_classifier.components.prepare_base_model import (
    PrepareBaseModel)

STAGE_NAME = "Prepare Base Model stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(
                config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.updated_base_model()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info("*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====\
                    ======x")
    except Exception as e:
        logger.exception(e)
        raise e
