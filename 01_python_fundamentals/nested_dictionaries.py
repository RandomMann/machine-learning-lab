models = {
	"MLP": {
		"learning_rate": 0.01,
		"Epochs": 100,
		"Accuracy": 0.98
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
	},

	"Transformer": {
     	    "learning_rate": 0.0003,
	    "Epochs": 80,
	    "Accuracy": 0.99
   
	}

}

max_accuracy = 0.0
best_model = None
sum_accuracy = 0
min_epochs = float("inf")
min_epochs_model = None
model_beyond_average = []

for key, value in models.items():
    sum_accuracy = sum_accuracy + value["Accuracy"]
    if value["Accuracy"] > max_accuracy:
        max_accuracy = value["Accuracy"]
        best_model = key

    if value["Epochs"] < min_epochs:
        min_epochs = value["Epochs"]
        min_epochs_model = key

average_accuracy = sum_accuracy/len(models)

for key, value in models.items():
    if value["Accuracy"] > average_accuracy:
        model_beyond_average.append(key)

print(f"Average accuracy is {average_accuracy:.4f}")
print(f"Min epochs is {min_epochs} with model {min_epochs_model}")
print(model_beyond_average)