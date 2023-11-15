FROM python:3.10.13

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash grandgrz && chmod 777 /opt /run

WORKDIR /grandgrz

RUN mkdir /grandgrz/static && mkdir /grandgrz/media && chown -R grandgrz:grandgrz /grandgrz && chmod 755 /grandgrz

COPY --chown=grandgrz:grandgrz . .

RUN pip install -r requirements.txt

USER grandgrz

CMD ["gunicorn", "-b", "0.0.0.0:8000", "grandgrz.wsgi:application"]
