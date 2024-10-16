import os
import matplotlib.pyplot as graph


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines[5:]  # Skip the first 5 lines
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return []


# Define file paths
file_paths = [
    r"C:\ENSEEIHT\INTERNSHIP\Final_laptop_backup\Internship\Internship\2jul\power2.5new.txt",
]

# Colors and labels for the plots
colors = ['r']
labels = ['2.5um']



# Process each file and plot data
for file_path, color, label in zip(file_paths, colors, labels):
    lines = read_file(file_path)
    output = {}

    for line in lines:
        ncladding = line[:25].strip()
        pout = line[50:].strip()
        if ncladding in output.keys():
            output[ncladding] += float(pout)
        else:
            output[ncladding] = float(pout)

    pmax = max(pout)
    print(f"maxpower: {pmax}")

    for ncladding, pout in output.items():
        print(f"ncladding: {ncladding}, sumofpout: {pout}")
    ncladding_list = list(output.keys())
    pout_list = list(output.values())
    print(pout_list)
    # Convert ncladding to float for plotting
    ncladding_list = [float(n) for n in ncladding_list]
    graph.plot(ncladding_list, pout_list, color=color, label=label, marker='o')


# Set graph attributes and show the plot
graph.title('Refractive Index vs Power-SemiPeriodic')
#graph.text(1.36, 0.016, pmax, fontsize=12, ha='right')
graph.xlabel('ncladding')
graph.ylabel('Power')
graph.legend()
graph.grid(True)
graph.show()
