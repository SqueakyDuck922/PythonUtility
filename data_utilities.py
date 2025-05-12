import yaml
from sqlalchemy import create_engine, engine
import pyodbc
from datetime import datetime
import pandas as pd
from sqlalchemy.dialects.mssql import DATETIMEOFFSET



def UploadFileToDatabase():

    log_message("uploading file to database...")

    configFile = open("config.yaml")
    configDict = yaml.load(configFile, Loader=yaml.FullLoader)
        
    # original version used on windows - didn't need TrustServerCertificate (also didn't need to pass port then)
    # engine_url = engine.URL.create(
    #             drivername='mssql',
    #             username=configDict['database']['username'],
    #             password=configDict['database']['password'],
    #             host=configDict['database']['server'],                
    #             database=configDict['database']['database'],
    #             query={'driver': configDict['database']['driver']}
    #         )
    
    #MAC version - needs TrustServerCertificate
    engine_url = engine.URL.create(
            drivername='mssql',
            username=configDict['database']['username'],
            password=configDict['database']['password'],
            host=configDict['database']['server'],          
            port=configDict['database']['port'],      
            database=configDict['database']['database'],
            query={"TrustServerCertificate": "YES", "driver": "ODBC Driver 18 for SQL Server"}   #Currently not been able to pass driver value from yaml as well as having TrustServerCertificate
        )
    

    #TODO
    # engine_url = "Driver={ODBC Driver 18 for SQL Server};Server=127.0.0.1,1007;Database=securities_masterC2;uid=sa;pwd=Badger99;TrustServerCertificate=yes"  


    mssql_engine = create_engine(engine_url, echo=False, fast_executemany=True)


    # csv_file_path = r"C:\Users\richk\OneDrive\Documents\TD\Strategies\ParamCombo_StrategyADX2.csv"
    # csv_file_path = r"C:\Users\richk\OneDrive\Documents\TD\Strategies\ParamCombo_EmaStrategy.csv"

    csv_file_path = configDict['general']['FilePath']  

    table_name = configDict['database']['ImportTable']  


    df = pd.read_csv(csv_file_path)



    # Test dataframe
    # base = datetime.datetime.today().replace(tzinfo=pytz.utc)
    # date_list = [base - datetime.timedelta(days=x) for x in range(20)]
    # df = pd.DataFrame(date_list, columns = ['date_time'])



    df.to_sql(table_name, mssql_engine, schema='dbo', if_exists='replace', dtype = {'date_time':DATETIMEOFFSET})

    log_message("csv loaded to database")

    return


def log_message(message):

    current_time = datetime.now()
    time_string = current_time.strftime('%H:%M:%S')
    msg = time_string + "  " + message
    print(msg)