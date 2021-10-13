FROM python:3.6.3-slim

LABEL maintainer="Simon Ryu <simonryu328@gmail.com>" \
      description="Vancouver Real Estate Data Analysis" 

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install numpy pandas seaborn jupyter boto3

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
