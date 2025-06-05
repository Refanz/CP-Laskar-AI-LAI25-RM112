from fastapi import HTTPException
import io
import numpy as np
import tensorflow as tf

from PIL import Image

from app.util.logger import show_log


def preprocess_image(input_image: bytes, target_size=(224, 224)):
    try:
        raw_image = Image.open(io.BytesIO(input_image))
        processed_image = raw_image.resize(target_size)
        image_array = np.array(processed_image)
        image_array = np.expand_dims(image_array, axis=0)

        image_tensor = tf.constant(image_array, dtype=tf.float32)
        return image_tensor

    except Exception as e:
        show_log(__name__).error(e)

        raise HTTPException(
            status_code=400,
            detail=f"Error processing image: {e}"
        )
