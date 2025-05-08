import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# Folder with radius of gyration .xvg files
gyration_folder = 'data_analysis/gyration'
output_panel = 'plots/gyration_panel_figure7_style.png'
output_combined = 'plots/gyration_combined.png'

# Read .xvg files
xvg_files = sorted(glob.glob(os.path.join(gyration_folder, '*.xvg')))

# Mapping short names to proper labels for combined plot
label_map = {
    'amber03': 'Amber03',
    'amber94': 'Amber94',
    'amber96': 'Amber96',
    'amber99': 'Amber99',
    'amber99sb-idln': 'Amber99SB-ILDN',
    'amber99sb': 'Amber99SB',
    'ambergs': 'AmberGS'
}

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

# Smoothing
def smooth(series, window_size=50):
    return series.rolling(window=window_size, center=True, min_periods=1).mean()

# === Plot 1: Panel Grid ===
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

# Hide any unused subplots
for j in range(len(xvg_files), 9):
    fig.delaxes(axes[j])

plt.tight_layout()
os.makedirs('plots', exist_ok=True)
plt.savefig(output_panel, dpi=300)
plt.close()
print(f"Panel figure saved: {output_panel}")

# === Plot 2: Combined Line Plot ===
colors = ['black', 'brown', 'green', 'blue', 'orange', 'purple', 'pink']

plt.figure(figsize=(12, 6))

for idx, xvg_file in enumerate(xvg_files):
    df = read_xvg(xvg_file)
    df = df.sort_values('Time (ps)')  # Ensure proper order
    df['Rg (nm)'] = smooth(df['Rg (nm)'])

    basename = os.path.basename(xvg_file).replace('gyrate_', '').replace('.xvg', '').lower()
    label = label_map.get(basename, basename)
    color = colors[idx % len(colors)]

    plt.plot(df['Time (ps)'], df['Rg (nm)'], label=label, color=color, lw=1.5)

plt.title('Radius of Gyration', fontsize=14, fontname='Times New Roman')
plt.xlabel('Time (ps)', fontsize=12, fontname='Times New Roman')
plt.ylabel('Rg (nm)', fontsize=12, fontname='Times New Roman')
plt.xticks(fontsize=10, fontname='Times New Roman')
plt.yticks(fontsize=10, fontname='Times New Roman')
plt.legend(fontsize=10)
plt.ylim(1.2, 3.8)
plt.tight_layout()
plt.savefig(output_combined, dpi=300)
plt.close()
print(f"Combined figure saved: {output_combined}")
