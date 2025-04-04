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

### Run
```
source .venv/bin/activate

python -m http_server.server -c http_server/config/config.yml
```

