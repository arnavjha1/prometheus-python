import subprocess

# Run the student's file
result = subprocess.run(
    ["python", "problems/p01_hello.py"],
    capture_output=True,
    text=True
)

# What the student printed
student_output = result.stdout

# Correct answer
expected_output = "Hello, World!\n"

# Compare outputs
if student_output == expected_output:
    print("PASS")
else:
    print("FAIL")

    print("Expected:")
    print(repr(expected_output))

    print("Got:")
    print(repr(student_output))