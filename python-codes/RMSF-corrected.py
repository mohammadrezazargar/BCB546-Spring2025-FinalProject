import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# RMSF data folder
rmsf_folder = 'data_analysis/rmsf'
output_file = 'plots/rmsf.png'

# Mapping of filenames to real force field names
label_map = {
    'rmsf_amber03': 'AMBER03',
    'rmsf_amber94': 'AMBER94',
    'rmsf_amber96': 'AMBER96',
    'rmsf_amber99': 'AMBER99',
    'rmsf_amber99sb-idln': 'AMBER99SB-ILDN',
    'rmsf_amber99sb': 'AMBER99SB',
    'rmsf_ambergs': 'AMBERGS'
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
    return pd.DataFrame(data, columns=['Atom', 'RMSF (nm)'])

# Optional smoothing for visual clarity
def smooth(series, window_size=10):
    return series.rolling(window=window_size, center=True, min_periods=1).mean()

# Collect .xvg files
xvg_files = sorted(glob.glob(os.path.join(rmsf_folder, '*.xvg')))

# Color palette similar to paper
colors = ['black', 'brown', 'limegreen', 'blue', 'gold', 'gray', 'pink']

# Plot combined RMSF
plt.figure(figsize=(10, 6))

for idx, xvg_file in enumerate(xvg_files):
    df = read_xvg(xvg_file)
    df['RMSF (nm)'] = smooth(df['RMSF (nm)'])
    filename_key = os.path.splitext(os.path.basename(xvg_file))[0]
    label = label_map.get(filename_key, filename_key)  # Use mapped name or fallback
    color = colors[idx % len(colors)]
    plt.plot(df['Atom'], df['RMSF (nm)'], label=label, color=color, lw=1.5)

plt.title('RMS fluctuation', fontsize=14, fontname='Times New Roman')
plt.xlabel('Atom', fontsize=12, fontname='Times New Roman')
plt.ylabel('RMSF (nm)', fontsize=12, fontname='Times New Roman')
plt.xticks(fontsize=10, fontname='Times New Roman')
plt.yticks(fontsize=10, fontname='Times New Roman')
plt.ylim(0, 5)
plt.legend(title='', fontsize=10)
plt.tight_layout()

os.makedirs('plots', exist_ok=True)
plt.savefig(output_file, dpi=300)
plt.close()
print(f" RMSF combined plot saved as: {output_file}")
