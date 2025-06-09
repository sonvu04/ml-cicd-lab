# check_performance.py
import subprocess
import re
import sys

# Run evaluate.py and capture output
result = subprocess.run(["python", "evaluate.py"], capture_output=True, text=True)
print(result.stdout)

# Extract accuracy from output
match = re.search(r"Model Accuracy: ([0-9.]+)", result.stdout)
if match:
    accuracy = float(match.group(1))
    if accuracy < 0.99:
        print("FAIL: Model accuracy is below threshold (0.80)")
        sys.exit(1)
    else:
        print("PASS: Model meets performance threshold")
else:
    print("ERROR: Could not read accuracy")
    sys.exit(1)
