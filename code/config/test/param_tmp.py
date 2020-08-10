def get_class_fine_tuning_parameter_base() -> dict:
    """
    Get parameter sample for class fine_tuning (like Keras)
    Returns:
        dict: parameter sample generated by trial object
    """
    return {
        "output_dir": r"D:\work\candlestick_model\output\model\ts_dataset_all_2day_label",
    }