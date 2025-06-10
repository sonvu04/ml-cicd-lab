# tests/test_training.py
import subprocess

def test_model_training():
    result = subprocess.run(["python", "train.py"])
    assert result.returncode == 0
