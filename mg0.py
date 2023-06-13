import subprocess

command = 'termux-sensor -s "mag-akm09918" -n 1'

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Command execution failed with error: {e}")

print("Script ended.")
