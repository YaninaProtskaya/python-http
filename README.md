# HTTP Server

### Setup
In project root folder:
```
virtualenv .venv  
source .venv/bin/activate   
pip install -r requirements.txt
```

### Configuration
```
cp http_server/config/config.sample.yml http_server/config/config.yml
```
Edit config.yml

### Mocked endpoints:
Modify `http_server/impl/MyRequestHandler.py`

### Run
```
source .venv/bin/activate

python -m http_server.server -c http_server/config/config.yml
```

