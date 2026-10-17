FROM python:3.12-slim-bookworm

ARG UID=1000
ARG GID=1000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    MPLCONFIGDIR=/tmp/matplotlib

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       graphviz \
       libgomp1 \
       ca-certificates \
       curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel \
    && python -m pip install --prefer-binary -r /tmp/requirements.txt \
    && python -m ipykernel install --sys-prefix \
       --name qiskit \
       --display-name "Python 3.12 (Qiskit)"

RUN groupadd --gid "${GID}" qiskit \
    && useradd --uid "${UID}" --gid "${GID}" --create-home --shell /bin/bash qiskit \
    && mkdir -p /workspace/notebooks /workspace/data /workspace/scripts \
    && chown -R qiskit:qiskit /workspace /home/qiskit

USER qiskit
ENV HOME=/home/qiskit

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--ServerApp.root_dir=/workspace"]
