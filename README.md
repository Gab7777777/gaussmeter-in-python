# gaussmeter-in-python
Magnetic field sensor, readings in microteslas (µT), designed for the mobile sensor mag-akm09918.

Make sure that the mg0.py script is present in the same directory as the main script, or you provide the correct path to the mg0.py script in the command variable.
The script relies on the subprocess module, which is a standard Python library and does not require any additional installations. However, if you encounter any import errors related to subprocess, it usually indicates a problem with your Python installation.

To be run using the termux-sensor utility

pkg update

pkg install termux-api


A tool for understanding and quantifying magnetic fields, allowing measurements and analysis. It can be used to measure it's strenght to be used in various applications, such as industrial processes and cybersecurity assesments:

Electromagnetic Interference (EMI) Detection: In cybersecurity, electromagnetic radiation and interference can have implications for the security and integrity of electronic devices and systems. A gaussmeter can be used to detect and measure electromagnetic fields emitted by electronic devices, power lines, or other sources that may cause interference or compromise the security of sensitive data.

Physical Security Assessments: Gaussmeters can be used as part of physical security assessments to identify and analyze the magnetic signatures of different electronic components or systems. For example, they can help detect hidden magnetic locks or identify magnetic anomalies that may indicate tampering or unauthorized access.

Magnetic Data Storage: Magnetic storage devices, such as hard disk drives (HDDs), use magnetic fields to store and retrieve data. Gaussmeters can be used to analyze the magnetic fields produced by these storage devices and assist in understanding their behavior, vulnerabilities, or potential for data leakage.
