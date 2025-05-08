import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# Folder with radius of gyration .xvg files
gyration_folder = 'data_analysis/gyration'
output_file = 'plots/gyration_panel_figure7_style.png'

# Read .xvg files
xvg_files = sorted(glob.glob(os.path.join(gyration_folder, '*.xvg')))

# Function to read XVG

def read_xvg(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('@', '#')):
                continue
            parts = line.strip().split()
            if len(parts) >= 2:
                data.append((float(parts[0]), float(parts[1])))
    return pd.DataFrame(data, columns=['Time (ps)', 'Rg (nm)'])

# Function to smooth data (optional but improves appearance)
def smooth(series, window_size=50):
    return series.rolling(window=window_size, center=True, min_periods=1).mean()

# Plotting grid (3x3 if 7 files, remaining empty)
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
axes = axes.flatten()

for idx, xvg_file in enumerate(xvg_files):
    df = read_xvg(xvg_file)
    df['Rg (nm)'] = smooth(df['Rg (nm)'])
    label = os.path.basename(xvg_file).replace('.xvg', '')

    ax = axes[idx]
    ax.plot(df['Time (ps)'], df['Rg (nm)'], color='black', linewidth=1)
    ax.set_title(f'{label}', fontsize=10)
    ax.set_xlabel('Time (ps)', fontsize=9)
    ax.set_ylabel('Rg (nm)', fontsize=9)
    ax.set_xlim(0, 100000)
    ax.set_ylim(1.2, 3.8)
    ax.tick_params(axis='both', labelsize=8)

# Hide empty subplots if fewer than 9 files
for j in range(len(xvg_files), 9):
    fig.delaxes(axes[j])

plt.tight_layout()
os.makedirs('plots', exist_ok=True)
plt.savefig(output_file, dpi=300)
plt.close()
print(f" Gyration panel figure saved as: {output_file}")
