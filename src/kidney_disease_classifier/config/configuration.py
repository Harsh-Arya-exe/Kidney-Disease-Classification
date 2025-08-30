from kidney_disease_classifier.utils.common import (read_yaml,
                                                    create_directories)
from kidney_disease_classifier.entity.config_entity import (
    DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig,
    EvaluationConfig)
from kidney_disease_classifier.constants import (CONFIG_FILE_PATH,
                                                 PARAMS_FILE_PATH)
from pathlib import Path
import os


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        print(config_filepath)
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        print('problem is here')
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config

    def get_model_training_config(self) -> TrainingConfig:
        config = self.config.training
        params = self.params
        prepare_base_model = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'CT\
-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-\
KIDNEY-DATASET-Normal-Cyst-Tumor-Stone')
        print("parmas: ", params.AUGMENTATION)

        training_config = TrainingConfig(
            root_dir=Path(config.root_dir),
            trained_model_path=Path(config.trained_model_path),
            updated_base_model_path=Path(
                prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augumentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE
        )

        return training_config

    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="D:\\Kidney-Disease-Classification\\artifacts\\\
data_ingestion\\CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone\\CT\
-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone",
            all_params=self.params,
            mlflow_uri="https://dagshub.com/hars\
h.arya1004/Kidney-Disease-Classification.mlflow",
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
        )

        print("mlflow uri in configuration file: ", eval_config.mlflow_uri)
        return eval_config
