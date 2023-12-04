FROM python:3.10-slim as builder

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt --no-cache-dir

FROM python:3.10-slim AS runner
WORKDIR /opt/webapp
RUN groupadd -g 1001 django \
    && useradd -u 1001 -g django -m -d /opt/webapp django \
    && chown django:django -R /opt/webapp
USER django

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --chown=django:django . /opt/webapp