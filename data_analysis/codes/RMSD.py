import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# RMSD data folder
rmsd_folder = 'data_analysis/rmsd'
output_file = 'plots/rmsd_m.png'

# Mapping file names to real force field labels
label_map = {
    'rmsd_amber03': 'AMBER03',
    'rmsd_amber94': 'AMBER94',
    'rmsd_amber96': 'AMBER96',
    'rmsd_amber99': 'AMBER99',
    'rmsd_amber99sb-idln': 'AMBER99SB-ILDN',
    'rmsd_amber99sb': 'AMBER99SB',
    'rmsd_ambergs': 'AMBERGS'
}

# Function to read .xvg files
def read_xvg(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('@', '#')):
                continue
            parts = line.strip().split()
            if len(parts) >= 2:
                data.append((float(parts[0]), float(parts[1])))
    return pd.DataFrame(data, columns=['Time (ps)', 'RMSD (nm)'])

# Optional smoothing for clarity
def smooth(series, window_size=50):
    return series.rolling(window=window_size, center=True, min_periods=1).mean()

# Collect .xvg files
xvg_files = sorted(glob.glob(os.path.join(rmsd_folder, '*.xvg')))

# Color palette
colors = ['black', 'brown', 'limegreen', 'blue', 'gold', 'gray', 'pink']

# Plot combined RMSD
plt.figure(figsize=(10, 6))

for idx, xvg_file in enumerate(xvg_files):
    df = read_xvg(xvg_file)
    df['RMSD (nm)'] = smooth(df['RMSD (nm)'])

    # Extend time axis to 100000 ps if necessary
    if df['Time (ps)'].max() < 10000:
        scale_factor = 100000 / df['Time (ps)'].max()
        df['Time (ps)'] *= scale_factor

    # Use mapped label if available
    basename = os.path.basename(xvg_file).replace('.xvg', '')
    label = label_map.get(basename, basename)
    color = colors[idx % len(colors)]
    plt.plot(df['Time (ps)'], df['RMSD (nm)'], label=label, color=color, lw=1.5)

plt.title('RMSD\nDNA_MOL after lsq fit to DNA_MOL', fontsize=14, fontname='Times New Roman')
plt.xlabel('Time (ps)', fontsize=12, fontname='Times New Roman')
plt.ylabel('RMSD (nm)', fontsize=12, fontname='Times New Roman')
plt.xticks(fontsize=10, fontname='Times New Roman')
plt.yticks(fontsize=10, fontname='Times New Roman')
plt.ylim(0, 4)
plt.xlim(0, 100000)
plt.legend(title='', fontsize=10)
plt.tight_layout()

os.makedirs('plots', exist_ok=True)
plt.savefig(output_file, dpi=300)
plt.close()
print(f" RMSD combined plot saved with real labels: {output_file}")