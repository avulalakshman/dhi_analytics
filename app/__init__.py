from flask import Flask
from multitenancy.config import MultiTenancyConfig
from applogging.config import ProductionConfig,StaggingConfig,Config

app = Flask(__name__)

mdb = MultiTenancyConfig(app); 

if app.config["ENV"] == "prod":
     app.config.from_object(ProductionConfig)
elif app.config["ENV"] == "stag":
    app.config.from_object(StaggingConfig)
else:
    app.config.from_object(Config)

from app import routes
