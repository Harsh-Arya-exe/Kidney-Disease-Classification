from kidney_disease_classifier.config.configuration import (
    ConfigurationManager)
from kidney_disease_classifier import logger
from kidney_disease_classifier.components.model_evaluation_mlflow import (
    Evaluation)

STAGE_NAME = "Model Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info("*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====\
                    ======x")
    except Exception as e:
        logger.exception(e)
        raise e
