# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

ARG OPEN_CV_VERSION=4.10.0
ENV DEBIAN_FRONTEND=noninteractive

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt-get update && apt-get install -y build-essential cmake git \
    libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    libjpeg-dev libpng-dev libtiff5-dev libdc1394-dev libeigen3-dev libtheora-dev \
    libvorbis-dev libxvidcore-dev libx264-dev sphinx-common libtbb-dev yasm \
    libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenexr-dev \
    libturbojpeg-dev libsparsehash-dev libboost-all-dev zlib1g-dev graphviz ffmpeg \
    libgstreamer-plugins-base1.0-dev libavutil-dev libavfilter-dev libjsoncpp-dev ffmpeg \
     && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    # for cython: https://cython.readthedocs.io/en/latest/src/quickstart/install.html
    build-essential \
    # for latex labels
    cm-super \
    dvipng \
    python3-tables \
    python3-pymediainfo \
    python3-numpy \
    python3-dev \
    cython3 \
    graphviz \
    libsm6 \
    libxext6 \
    htop \
    rsync \
    mkvtoolnix \
    python3-mysqldb \
    mysql-client && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python 3 packages
USER root
RUN python3 -m pip --no-cache-dir install --no-binary  \
    'altair' \
    'beautifulsoup4' \
    'bokeh' \
    'bottleneck' \
    'cloudpickle' \
    'cython' \
    'dask' \
    'dill' \
    'h5py' \
    'ipympl'\
    'ipywidgets' \
    'matplotlib' \
    'numba' \
    'numexpr>=2.8.4' \
    'pandas' \
    'patsy' \
    'protobuf' \
    'seaborn' \
    'sqlalchemy' \
    'statsmodels' \
    'sympy' \
    'scipy' \
    'scikit-learn' \
    'widgetsnbextension'\
    'xlrd' \
    'bagpy' \
    'pyarrow' \
    'srt' \
    'timecode' \
    'ffmpeg-python' \
    'prefect[viz]' \
    'dask-labextension' \
    'jupyterlab_hdf' \
    'hdf5plugin' \
    'jupyter_bokeh' \
    'pycapnp' \
    'torch' \
    'torchvision' \
    'highdicom>=0.18.2' \
    'monai>=1.0.0' \
    'nibabel>=3.2.1' \
    'numpy>=1.21.6' \
    'numpy-stl>=2.12.0' \
    'Pillow>=8.0.0' \
    'pydicom>=2.3.0' \
    'PyPDF2>=2.11.1' \
    'scikit-image>=0.17.2' \
    'SimpleITK>=2.0.0' \
    'torch>=2.0.1' \
    'trimesh>=3.8.11' \
    'typeguard>=3.0.0' \
    'aiortc==1.5.0' \
    'eclipse-zenoh==0.11.0' \
    'pycdr2==1.0.0'

WORKDIR /tmp
RUN git clone --depth 1 --branch $OPEN_CV_VERSION https://github.com/opencv/opencv.git && \
    git clone --depth 1 --branch $OPEN_CV_VERSION https://github.com/opencv/opencv_contrib.git && \
    cd opencv && mkdir -p build && cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_opencv_apps=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_DOCS=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D WITH_TBB=ON \
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=1 \
    -D WITH_CUDA=ON \
    -D BUILD_opencv_cudacodec=OFF \
    -D WITH_CUDNN=ON \
    -D OPENCV_DNN_CUDA=ON \
    -D CUDA_ARCH_BIN=8.6,8.9 \
    -D WITH_V4L=ON \
    -D WITH_QT=OFF \
    -D WITH_OPENGL=ON \
    -D WITH_GSTREAMER=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_PC_FILE_NAME=opencv.pc \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D PYTHON3_PACKAGES_PATH=/usr/lib/python3.10/dist-packages \
    -D PYTHON3_EXECUTABLE=/usr/bin/python3 \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
    .. && \
    make -j8 && \
    make install && \
    ldconfig

WORKDIR /tmp
RUN git clone https://github.com/shersonb/python-ebml.git && \
    cd python-ebml && \
    python3 -m pip --no-cache-dir install .

RUN git clone https://github.com/shersonb/python-matroska.git && \
    cd python-matroska && \
    python3 -m pip --no-cache-dir install .

RUN chown -R ${NB_UID}:${NB_GID} /home/${NB_USER} && \
    mkdir -p /home/${NB_USER}/work/.ipynb_checkpoints /home/${NB_USER}/.cache /home/${NB_USER}/.config && \
    chown -R ${NB_UID}:${NB_GID} /home/${NB_USER}/work/.ipynb_checkpoints /home/${NB_USER}/.cache /home/${NB_USER}/.config && \
    adduser "${NB_USER}" vglusers


RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    libfontenc-dev \
    libxaw7-dev \
    libxkbfile-dev \
    libxmu-dev \
    libxmuu-dev \
    libxpm-dev \
    libxres-dev \
    libxss-dev \
    libxt-dev \
    libxtst-dev \
    libxv-dev \
    libxxf86vm-dev \
    libxcb-glx0-dev \
    libxcb-render-util0-dev \
    libxcb-xkb-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-shape0-dev \
    libxcb-sync-dev \
    libxcb-xfixes0-dev \
    libxcb-xinerama0-dev \
    libxcb-dri3-dev \
    libxcb-cursor-dev \
    libxcb-dri2-0-dev \
    libxcb-dri3-dev \
    libxcb-present-dev \
    libxcb-composite0-dev \
    libxcb-ewmh-dev \
    libxcb-res0-dev \
    libxcb-util0-dev \
    libsoundio-dev \
    nasm \
    mono-devel \
    libomp-dev \
    libacl1-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip --no-cache-dir install --no-binary  \
    'conan' \
    'contextlib_chdir'

USER ${NB_UID}
RUN fix-permissions "/home/${NB_USER}"

# Install facets which does not have a pip or conda package at the moment
USER root

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME="/home/${NB_USER}/.cache/"

RUN MPLBACKEND=Agg python3 -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}

WORKDIR "${HOME}"
