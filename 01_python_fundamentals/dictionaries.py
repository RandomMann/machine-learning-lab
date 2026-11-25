learning_rates = {
	"Linear_Regression": 0.01,
	"Logistic_Regression": 0.001,
	"Neural_Network": 0.0001
}
learning_rates["SVM"] = 0.27
learning_rates["Logistic_Regression"] = 0.27

learning_rates_2 = {
	"Random_Forest": 0.003,
	"Line_search": 0.005
}
learning_rates.update(learning_rates_2)

max_learning_rate = max(learning_rates.values())
best_model = []

for item in learning_rates.items():
	if item[1] == max_learning_rate:
	    best_model.append(item[0])
		
print(f"Max Learning Rateis {max_learning_rate},Best Model is {best_model}")

#print(learning_rates.keys())
#print(learning_rates.values())
#print(f"Maxmium is {max(learning_rates.values())}")
#print(f"Minimum is {min(learning_rates.values())}")
#print(learning_rates.get("Random_Forest", 0.3))
#print(learning_rates["Neural_Network"])
#print(learning_rates["SVM"])
#print(learning_rates)
