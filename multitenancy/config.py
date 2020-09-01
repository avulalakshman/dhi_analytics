from multitenancy import logger,yaml

class MultiTenancyConfig:

    def __init__(self,app):
        self.app = app
        self.group_tenant_list = {}
        self.tenant_data = {}
        self.init(app.config["ENV"])
    
    def init(self,env):
        env = env.lower()
        if env in ['prod','qa','stag']:
             file_name = f'./resources/application.{env}.yml'
        else:
            file_name = f'./resources/application.yml'
        logger.info(f"Environment :{file_name}")
        self.init_tenants(file_name,env)

    def init_tenants(self,filePath,env):
        with open(filePath) as f:
            try:
                docs = yaml.load_all(f, Loader=yaml.Loader)
                for doc in docs:
                    self.group_tenant_list[doc['groupName']]=doc['tenantDataList']  
                
                for k,v in self.group_tenant_list.items():
                    for t in v:
                        self.tenant_data[t['tenantName']] = t['uri']
                logger.info(f"Total Groups found {len(self.group_tenant_list)} for the EVN: {env}")   
                logger.info(f"Total tenants found: {len(self.tenant_data)}")       
            except IOError:
                logger.error("Environment file is not found, provide valid environment file...")
    
    def tenant_details(self,teanantId):
        try:
            return self.tenant_data[teanantId]
        except KeyError as e:
            logger.error(f"Tenant with id: {teanantId} details are not found:{e}")


