import os
from keras.src.export import TFSMLayer
from app.core.config import settings
from app.util.logger import show_log


class PalmOilModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PalmOilModel, cls).__new__(cls)
            cls._instance._model = None
            cls._instance.load_model()
        return cls._instance

    def load_model(self):
        if not os.path.exists(settings.MODEL_PATH):
            raise FileNotFoundError(f"Model dir not found at: {settings.MODEL_PATH}")

        print(f"Loading model from {settings.MODEL_PATH}")
        self._model = TFSMLayer(settings.MODEL_PATH, call_endpoint="serving_default")
        print("Model loaded successfully")

    def predict(self, input_data):
        if self._model is None:
            raise RuntimeError("Model has not been loaded.")

        prediction = self._model(input_data)['output_0'][0]
        show_log(__name__).debug(prediction)
        return prediction


palm_oil_model_instance = PalmOilModel()
