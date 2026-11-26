image_shape = (640, 480, 3)

train_labels = ["cat", "dog", "bird", "cat", "dog", "horse"]
test_labels = ["cat", "dog", "fish", "fish", "bird"]

# Tuple unpacking
width, height, channels = image_shape
total_pixels = width * height

# Remove duplicate labels
unique_train_labels = set(train_labels)
unique_test_labels = set(test_labels)

# Count classes
num_train_classes = len(unique_train_labels)
num_test_classes = len(unique_test_labels)

# Set operations
common_labels = unique_train_labels & unique_test_labels
train_only_labels = unique_train_labels - unique_test_labels
test_only_labels = unique_test_labels - unique_train_labels
all_labels = unique_train_labels | unique_test_labels

# Print results
print(f"Total pixels: {total_pixels}")
print(f"Training labels: {unique_train_labels}")
print(f"Test labels: {unique_test_labels}")
print(f"Number of training classes: {num_train_classes}")
print(f"Number of test classes: {num_test_classes}")
print(f"Common labels: {common_labels}")
print(f"Training-only labels: {train_only_labels}")
print(f"Test-only labels: {test_only_labels}")
print(f"All labels: {all_labels}")