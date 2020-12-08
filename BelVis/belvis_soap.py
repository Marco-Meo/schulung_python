from zeep import Client, Settings
from datetime import datetime, timedelta

if __name__ == '__main__':

    meteringpoint = 'CH1022401234501000000000000002269'
    date_from = datetime.strptime('01.01.2019', '%d.%m.%Y')
    date_to = datetime.strptime('31.01.2019', '%d.%m.%Y')
    settings = Settings(raw_response=True)
    connection = Client('belvis_soap/BelVis_EAI_Connection.wsdl')
    ts_access = Client('belvis_soap/BelVis_EAI_TSAccess.wsdl')
    common = Client('belvis_soap/BelVis_EAI_Common.wsdl', settings=settings)

    handle = connection.service.OpenConnection('user', 'password', 'EPAG_ENERGIE', '', '', '')
    id_ent = ts_access.service.GetExtractionpoint(
        handle, meteringpoint
    )
    # print(id_ent.oInstanceId)
    id = str(id_ent.oInstanceId)
    zr = ts_access.service.GetTimeSeriesData_Metering_Eq(
        handle,
        meteringpoint,
        '700',
        '0',
        date_from.strftime('%Y-%m-%dT%H:%M:%S'),
        date_to.strftime('%Y-%m-%dT%H:%M:%S'),
    )
    print(zr)