import turicreate as tc
import os


data = tc.image_analysis.load_images("dogDataset", with_path=True)
data["dogBreed"] = data["path"].apply(lambda path: os.path.basename(os.path.dirname(path)))
data.save("dogbreed.sframe")
data.explore()

