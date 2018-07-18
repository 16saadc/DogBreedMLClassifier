import turicreate as tc
data = tc.SFrame("dogBreed.sframe")
train_data, test_data = data.random_split(0.8)
model = tc.image_classifier.create(train_data, target="dogBreed", model="resnet-50", max_iterations=20)
predictions = model.predict(test_data)
metrics = model.evaluate(test_data)
print(metrics["accuracy"])
model.save("dog_breeds.model")
model.export_coreml("DogBreeds.mlmodel")
