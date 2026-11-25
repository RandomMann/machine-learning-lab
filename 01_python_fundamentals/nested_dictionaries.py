models = {
	"MLP": {
		"learning_rate": 0.01,
		"Epochs": 100,
		"Accuracy": 0.85
	},

	"CNN": {
	    "learning_rate": 0.001,
	    "Epochs": 200,
	    "Accuracy": 0.93
	},

	"Resnet": {
	    "learning_rate": 0.0001,
	    "Epochs": 300,
	    "Accuracy": 0.96
	}

}

models["CNN"]["Epochs"] = 250
print(models["Resnet"]["Accuracy"])
print(len(models))