experiments = {
    "model_A": {
        "learning_rate": 0.01,
        "batch_size": 32,
        "train_losses": [0.95, 0.62, 0.35, 0.18],
        "val_losses": [0.98, 0.65, 0.42, 0.45]
    },
    "model_B": {
        "learning_rate": 0.001,
        "batch_size": 64,
        "train_losses": [0.92, 0.58, 0.32, 0.21],
        "val_losses": [0.95, 0.61, 0.38, 0.29]
    },
    "model_C": {
        "learning_rate": 0.01,
        "batch_size": 32,
        "train_losses": [0.91, 0.55, 0.25, 0.10],
        "val_losses": [0.94, 0.60, 0.45, 0.58]
    }
}

# Initialization
final_train_losses = {}
final_val_losses = {}
loss_gaps = {}

learning_rates = []
batch_sizes = []

best_train_loss = float("inf")
best_val_loss = float("inf")

best_train_model = None
best_val_model = None

# Extract experiment data
for name, config in experiments.items():
    final_train_losses[name] = config["train_losses"][-1]
    final_val_losses[name] = config["val_losses"][-1]

    learning_rates.append(config["learning_rate"])
    batch_sizes.append(config["batch_size"])

# Remove duplicates
unique_learning_rates = set(learning_rates)
unique_batch_sizes = set(batch_sizes)

# Find the best training model
for name, loss in final_train_losses.items():
    if loss < best_train_loss:
        best_train_loss = loss
        best_train_model = name

# Find the best validation model
for name, loss in final_val_losses.items():
    if loss < best_val_loss:
        best_val_loss = loss
        best_val_model = name

# Calculate loss gaps
for name in final_val_losses:
    loss_gaps[name] = (
        final_val_losses[name] - final_train_losses[name]
    )

# Filter models with large loss gaps
high_gap_models = [
    name for name, gap in loss_gaps.items() if gap > 0.2
]

# Print results
print(f"Final training losses: {final_train_losses}")
print(f"Final validation losses: {final_val_losses}")

print(f"Unique learning rates: {unique_learning_rates}")
print(f"Unique batch sizes: {unique_batch_sizes}")

print(f"Best training model: {best_train_model}")
print(f"Best training loss: {best_train_loss}")

print(f"Best validation model: {best_val_model}")
print(f"Best validation loss: {best_val_loss}")

print(f"Loss gaps: {loss_gaps}")
print(f"High gap models: {high_gap_models}")