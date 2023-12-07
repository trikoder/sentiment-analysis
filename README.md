# Sentiment Analysis
Deploy your neural network locally with just a few easy commands! \
We will use a pretrained sentiment analysis neural network from [HuggingFace](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment/tree/main).
To make things as easy as possible, we will download models from HuggingFace on container startup.
</br>

## Prepare your environemnt

1. Install [Docker](https://docs.docker.com/engine/install/)
2. Clone this repository
</br>


## Build Docker image
Position your shell in the root of this repository, and execute (be patient, some heavy packages are required :)
```
$ docker build -t sentiment_analysis_streamlined .
```
</br>


## Run Docker container
```
$ docker run --rm -it -p 8000:8000 sentiment_analysis_streamlined
```
**Advance Usage**:</br>
- Set number of workers running inside a Docker container by adding a flag (default is 1):
`--env WORKERS=2` \
- Change application port by adding flag (defalut is 8000), don't forget to change ports in `docker run` as well: `--env PORT=8001`
- You can limit resource allocation for Docker container by adding these flags: `--gpus "device=0" --cpus="2.0" --memory="4g"`
    1. First flag gives access to GPU with ID=0. Without this flag, no GPUs are accessible inside docker container. If you want a container to have access to all GPUs on a system, write `--gpus all`. You must install additional Nvidia [packages](https://www.howtogeek.com/devops/how-to-use-an-nvidia-gpu-with-docker-containers/) to allow GPU usage inside containers
    2. Second flag limits access to 2 CPU cores, without this flag container can use **all** CPU cores
    3. Third flag limits memory access to 4GB, without this flag container can use **entire** memory


## Access API endpoints
API endpoints can be accessed, and are documented, here `http://0.0.0.0:8000`

## Format and check code
Install development packages
```
$ pip install -r requirements-dev.txt
```
Format and check code
```
$ isort . && black . && ruff --ignore E501 . && bandit -c bandit.yaml -rq . && mypy .
```
