# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/minimal-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    # for cython: https://cython.readthedocs.io/en/latest/src/quickstart/install.html
    build-essential \
    # for latex labels
    cm-super \
    dvipng \
    python3-opencv \
    python3-tables \
    python3-skimage \
    python3-skimage-lib \
    python3-sklearn \
    python3-sklearn-lib \
    python3-scipy \
    python3-pymediainfo \
    cython3 \
    cmake \
    graphviz \
    ffmpeg \
    mkvtoolnix &&\
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Install Python 3 packages
USER root
RUN python3 -m pip --no-cache-dir install \
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
    'numexpr' \
    'pandas' \
    'patsy' \
    'protobuf' \
    'seaborn' \
    'sqlalchemy' \
    'statsmodels' \
    'sympy' \
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
    'jupyter_bokeh'

WORKDIR /tmp
RUN git clone https://github.com/capnproto/pycapnp.git && \
    cd pycapnp && \
    python3 -m pip --no-cache-dir install --install-option "--libcapnp-url" \
    --install-option "https://github.com/capnproto/capnproto/archive/refs/tags/v0.9.1.tar.gz" \
    --install-option "--force-bundled-libcapnp" .


RUN git clone https://github.com/shersonb/python-ebml.git && \
    cd python-ebml && \
    python3 -m pip --no-cache-dir install .

RUN git clone https://github.com/shersonb/python-matroska.git && \
    cd python-matroska && \
    python3 -m pip --no-cache-dir install .

RUN chown -R ${NB_UID}:${NB_GID} /home/${NB_USER} && \
    adduser "${NB_USER}" vglusers

USER ${NB_UID}
RUN fix-permissions "/home/${NB_USER}"

# Install facets which does not have a pip or conda package at the moment
USER root
WORKDIR /tmp
RUN git clone https://github.com/PAIR-code/facets.git && \
    jupyter nbextension install facets/facets-dist/ --sys-prefix && \
    jupyter labextension install @jupyterlab/hdf5 && \
    rm -rf /tmp/facets && \
    fix-permissions "/home/${NB_USER}"

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME="/home/${NB_USER}/.cache/"

RUN MPLBACKEND=Agg python3 -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}

WORKDIR "${HOME}"
