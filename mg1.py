import subprocess

command = 'python mg0.py'

while True:
    try:
        subprocess.run('clear', shell=True)
        print (" ")
        print ("+++POISON CORP. SENSOR TOOLS+++")
        print ("Gaussometer, readings in microtesla (uT)")
        print (" ")
 
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True).decode('utf-8')

        # Parse the output to retrieve the values
        values = []
        start_index = output.find('values": [') + len('values": [')
        end_index = output.find(']', start_index)
        values_str = output[start_index:end_index]
        values_str = values_str.replace(',', '').strip()
        if values_str:
            values = [float(value) for value in values_str.split()]

        print("X:", values[0])
        print("Y:", values[1])
        print("Z:", values[2])
        print()

        print("GRAPH:")
        for value in values:
            if value >= 0:
                graph = '+' * int(value)
            else:
                graph = '-' * int(abs(value))
            print(graph)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with error: {e}")

    print(" ")
    print ("max. range of 2000.0 uT")
    print ("resolution of 0.0625 uT")
    print(" ") 
    print("\nPress Enter to repeat the process, or Ctrl + X to exit.")
    user_input = input()

    if user_input == "\x18":  # Ctrl + X
        break

print("Script ended.")
