import requests
import xmltodict
import datetime

#Get the exchange rate of a particular date
def get_exchange_rate(date):
    date_ojb = datetime.datetime.strptime(date, '%Y-%m-%d')
    #struct of xml data
    xml_data = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <TipoCambioRango xmlns="http://www.banguat.gob.gt/variables/ws/">
        <fechainit>{date_ojb.year}-{date_ojb.day}-{date_ojb.month}</fechainit>
        <fechafin>{date_ojb.year}-{date_ojb.day}-{date_ojb.month}</fechafin>
        </TipoCambioRango>
    </soap:Body>
    </soap:Envelope>"""
    xml = bytes(xml_data,'UTF-8')
    res = requests.post(
        url="http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx",
        headers={
            'Content-Type':'text/xml; charset=utf-8',
            'SOAPAction':'http://www.banguat.gob.gt/variables/ws/TipoCambioRango'
        },
        data=xml
    )
    #convert xml to dict
    data = xmltodict.parse(res.content)
    data_res = data['soap:Envelope']['soap:Body']['TipoCambioRangoResponse']['TipoCambioRangoResult']['Vars']['Var']
    return {
        "venta":data_res["venta"],
        "compra":data_res["compra"],
        "fecha":data_res["fecha"],
    }