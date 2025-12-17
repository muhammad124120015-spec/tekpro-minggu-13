import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Interactive Seismic Data Visualization")

# Contoh data seismik (bisa diganti data asli)
nt = 500   # jumlah sampel waktu
nx = 50    # jumlah trace
data = np.random.randn(nt, nx)

# Sidebar
st.sidebar.header("Pengaturan Plot")

# Dropdown colormap
cmap = st.sidebar.selectbox(
    "Pilih Colormap",
    ["gray", "seismic", "viridis", "plasma", "inferno"]
)

# Mode scaling
scale_mode = st.sidebar.radio(
    "Mode Scaling",
    ["Auto", "Manual"]
)

# Slider vmin dan vmax
vmin = st.sidebar.slider(
    "vmin",
    float(data.min()),
    float(data.max()),
    float(data.min())
)

vmax = st.sidebar.slider(
    "vmax",
    float(data.min()),
    float(data.max()),
    float(data.max())
)

# Opsi tambahan: membalik sumbu waktu
invert_time = st.sidebar.checkbox("Balik Sumbu Waktu")

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

if scale_mode == "Auto":
    im = ax.imshow(
        data,
        aspect="auto",
        cmap=cmap
    )
else:
    im = ax.imshow(
        data,
        aspect="auto",
        cmap=cmap,
        vmin=vmin,
        vmax=vmax
    )

# Membalik sumbu waktu jika dipilih
if invert_time:
    ax.invert_yaxis()

ax.set_xlabel("Trace")
ax.set_ylabel("Time")
ax.set_title("Seismic Section")

plt.colorbar(im, ax=ax, label="Amplitude")

st.pyplot(fig)