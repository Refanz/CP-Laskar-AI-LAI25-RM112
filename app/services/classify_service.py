from app.model.classify_model import palm_oil_model_instance
from app.util.model_util import preprocess_image


class ClassifyService:
    def __init__(self, model_instance=palm_oil_model_instance):
        self.model = model_instance

    async def classify(self, input_data):
        processed_input = preprocess_image(input_data)
        prediction = self.model.predict(processed_input)

        return prediction

def get_classify_service():
    return ClassifyService()
