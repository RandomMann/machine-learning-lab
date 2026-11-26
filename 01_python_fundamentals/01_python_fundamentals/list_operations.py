losses = [0.95, 0.82, 0.63, 0.41, 0.28, 0.19]

first_three_losses = losses[:3]
last_three_losses = losses[-3:]
middle_losses = losses[2:6]
sampled_losses = losses[::3]
reversed_losses = losses[::-1]

average_loss = sum(last_three_losses) / len(last_three_losses)
filtered_losses = [loss for loss in losses if loss > 0.6]
scaled_losses = [loss * 100 for loss in losses]
squared_losses = [loss**2 for loss in losses]
filtered_squared_losses = [loss**2 for loss in losses if loss < 0.5]