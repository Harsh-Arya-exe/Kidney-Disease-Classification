from kidney_disease_classifier.config.configuration import (
    ConfigurationManager)
from kidney_disease_classifier import logger
from kidney_disease_classifier.components.model_training import (
    Training)

STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            training_config = config.get_model_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info("*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====\
                    ======x")
    except Exception as e:
        logger.exception(e)
        raise e
