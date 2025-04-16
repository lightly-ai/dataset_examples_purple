# We import the DatasetLoader class from the lightly_purple module
from lightly_purple import DatasetLoader
from pathlib import Path

# Create a DatasetLoader instance
loader = DatasetLoader()

data_yaml_path = Path(__file__).resolve().parent / "data.yaml"
loader.from_yolo(
    data_yaml_path=str(data_yaml_path),
    input_split="val",
)

# We start the UI application on port 8001
loader.launch()
