FROM python:3.10.4
WORKDIR /app
COPY . .
RUN pip install cython
RUN python compile.py build_ext --inplace
CMD ["python","../app"]
