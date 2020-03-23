from commons import get_model, get_tensor

model = get_model()

def get_response_image(image_bytes):
	tensor = get_tensor(image_bytes)
	outputs = model.forward(tensor)

	## how exactly do i interact with the model here? ie. inputs/outputs

	## return segmented image
	return output_image