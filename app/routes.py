from app import app,mdb
import applogging.logconfig
import logging 

logger = logging.getLogger(__name__)


@app.route('/')
def index():
    logger.info(f"Environment Test Message {app.config['MESSAGE']}")
    return mdb.tenant_details('dhi_examuat1')
