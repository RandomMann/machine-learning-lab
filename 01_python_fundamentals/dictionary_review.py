experiments = {
	"Run_1": {
		      "learning_rate": 0.01, 
	          "loss_history":[0.8, 0.5, 0.3]
			  },

	"Run_2": {
		      "learning_rate": 0.001, 
	          "loss_history":[0.9, 0.4, 0.2]
			  },

	"Run_3": {
		      "learning_rate": 0.0001, 
	          "loss_history":[0.9, 0.7, 0.6]
			  }
              }

results = {}
best_loss = float("inf")
ave_loss = 0
best_name = None

for key, value in experiments.items():
	final_loss = value["loss_history"]
	print(final_loss[-1])
	results[key] = final_loss[-1]

print(results)

for name, loss in results.items():
	if loss < best_loss:
		best_loss = loss
		best_name = name


ave_loss = sum(results.values())/len(experiments)
print(f"Minimal loss is {best_loss},and average loss is {ave_loss},name is {best_name}")
