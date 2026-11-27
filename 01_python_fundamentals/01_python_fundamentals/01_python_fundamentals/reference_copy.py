import copy

model_config = {
    "learning_rate": 0.01,
    "epochs": 100,
    "layers": [64, 128, 10]
}

reference_config = model_config
shallow_config = model_config.copy()
deep_config = copy.deepcopy(model_config)

reference_config["learning_rate"] = 0.001
shallow_config["epochs"] = 200
shallow_config["layers"][0] = 32
deep_config["layers"][0] = 256

print(reference_config, shallow_config, deep_config, model_config)