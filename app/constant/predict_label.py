predict_label = ("Fungal Disease", "Healthy", "Magnesium Deficiency", "Scale Insect")


def get_label_with_index(index) -> str:
    result = None

    for i, label in enumerate(predict_label):
        if i == index:
            result = label
            break

    return result
