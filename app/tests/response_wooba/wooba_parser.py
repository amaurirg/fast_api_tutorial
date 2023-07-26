from api_content import api_content
from airports import airports

carrier = {}
voos = []
trecho1 = api_content.get("ViagensTrecho1", [])
if trecho1:
    trecho1 = trecho1[0]
    carrier = trecho1.get("CiaMandatoria", {})
    voos = trecho1.get("Voos", [{}])

if not voos:
    response = {
        "count": 0,
        # "next": None,
        # "previous": None,
        "results": [],
        # "min_price": None,
        # "max_price": None
    }

else:
    response = {
        "count": len(voos),
        "next": None,
        "previous": None,
        "results": [
            {
                "flights": [
                    {
                        "id": voos[0].get("Id"),
                        "origin": {
                            "state": {
                                "country": {
                                    "name": airports[voos[0].get('Origem', {}).get('CodigoIata')].country_name,
                                    # colocar .get()
                                    "code": airports[voos[0].get('Origem', {}).get('CodigoIata')].country_code
                                },
                                # "name": "São Paulo",
                                "name": airports[voos[0].get('Origem', {}).get('CodigoIata')].state_name,
                                "initials": airports[voos[0].get('Origem', {}).get('CodigoIata')].state_code
                            },
                            "name": airports[voos[0].get('Origem', {}).get('CodigoIata')].city_name
                        },
                        "destination": {
                            "state": {
                                "country": {
                                    "name": "Brasil",
                                    "code": "BR"
                                },
                                "name": "Amazonas",
                                "initials": "AM"
                            },
                            "name": "Manaus"
                        },
                        "links": [  # TODO Criar o hash
                            {
                                "pricing": "/pricing?hash=81a7666c6967687473d9e05b7b226d6f64656c223a2022666c69676874732e666c69676874222c2022706b223a203532313739352c20226669656c6473223a207b226a6f75726e6579223a203133303830382c20226f726967696e223a2034333939302c202264657374696e6174696f6e223a2034343039352c2022646972656374696f6e223a20226f7574626f756e64222c202274726176656c5f74696d65223a2022333435222c202265787465726e616c5f6964223a202230222c2022646972656374223a2066616c73652c202270726f76696465725f726573706f6e7365223a206e756c6c7d7d5d"
                            }
                        ],
                        "segments": [
                            {
                                "origin": {
                                    "name": airports[voos[0].get('Origem', {}).get('CodigoIata')].airport_name,
                                    "iata_code": voos[0].get('Origem', {}).get('CodigoIata'),
                                    "city_name": airports[voos[0].get('Origem', {}).get('CodigoIata')].city_name,
                                    "state_name": airports[voos[0].get('Origem', {}).get('CodigoIata')].state_name
                                },
                                "destination": {
                                    "name": airports[voos[0].get('Destino', {}).get('CodigoIata')].airport_name,
                                    "iata_code": voos[0].get('Destino', {}).get('CodigoIata'),
                                    "city_name": airports[voos[0].get('Destino', {}).get('CodigoIata')].city_name,
                                    "state_name": airports[voos[0].get('Destino', {}).get('CodigoIata')].state_name
                                },
                                "carrier": {
                                    "id": voos[0]["CiaOperacional"]["Id"],
                                    "name": voos[0]["CiaOperacional"]["Descricao"],
                                    "iata_code": voos[0]["CiaOperacional"]["CodigoIata"]
                                },
                                "marketing_carrier": {
                                    "id": voos[0]["CiaMandatoria"]["Id"],
                                    "name": voos[0]["CiaMandatoria"]["Descricao"],
                                    "iata_code": voos[0]["CiaMandatoria"]["CodigoIata"]
                                },
                                "date_departure": "2023-08-16T06:05:00-03:00",  # falta pegar
                                "date_arrival": "2023-08-16T07:50:00-03:00",    # falta pegar
                                "flight_number": voos[0].get("Numero"),
                                "flight_time": 105.0,   # voos[0].get("Duracao") converter str para float
                                "distance": 540.0,      # falta pegar
                                "equipment": voos[0].get("Equipamento"),
                                "connection": voos[0].get("Conexao")
                            }
                        ],
                        "prices": [  # Fazer loop em voos[0].get("ListaDeClasses")
                            {
                                "id": voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("Id"),
                                "brand": {
                                    "name": voos[0].get("ListaDeClasses", [{}])[0].get("Familia"),
                                    "slug": voos[0].get("ListaDeClasses", [{}])[0].get("Familia").lower(),
                                    "code": voos[0].get("ListaDeClasses", [{}])[0].get("FamiliaCodigo"),
                                },
                                "taxes": [
                                    {
                                        "name": "Taxes",
                                        "value": voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("Taxa"),
                                        "currency_code": "BRL"  # falta pegar
                                    }
                                ],
                                "breakdown": [  # Pegar valores CHD e INF também
                                    {
                                        "pax_type": "ADT",
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("FaixaEtaria")
                                        "pax_count": 1,
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("Quantidade")
                                        "base": 1376.9,
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("ValorTarifa")
                                        "taxes": 177.62,
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("ValorTaxaEmbarque")
                                        # + TODO Verificar se soma a TAXA DE SERVIÇO AQUI
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("ValorTaxaServico")
                                        # + TODO Verificar se soma o FEE
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("ValorFee")

                                        "total": 1554.52,
                                        # voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("PrecoAdulto", {}).get("ValorTarifa")
                                        # +
                                        # "ValorTarifaNet": 260.9,  TODO Verificar essa taxa
                                        # "ValorTaxaAssento": 0,
                                        # "ValorTaxaBagagem": 0,
                                        # "ValorTaxaCombustivel": 0,
                                        # "ValorTaxaEmbarque": 42.29,
                                        # "ValorTaxaMenorDesacompanhado": 0,
                                        # "ValorTaxaServico": 40
                                        "discount": 0.0,
                                        "currency_code": voos[0].get("ListaDeClasses", [{}])[0].get("Moeda")
                                    }
                                ],
                                "links": {
                                    "farerules": "/farerules?hash=1129347"
                                },
                                "base": voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("TotalTarifa"),
                                "total": voos[0].get("ListaDeClasses", [{}])[0].get("Preco", {}).get("TotalGeral"),
                                "baggage_included": voos[0].get("ListaDeClasses", [{}])[0].get("BagagemInclusa"),
                                "baggage_pieces": voos[0].get("ListaDeClasses", [{}])[0].get("BagagemQuantidade"),
                                "date_added": "2023-07-18T13:03:34.306030-03:00",   # falta pegar
                                "fare_basis": voos[0].get("BaseTarifaria", [{}])[0].get("Codigo"),
                                "currency_code": voos[0].get("ListaDeClasses", [{}])[0].get("Moeda"),
                                "promocode": None,      # falta pegar
                                "discount": 0.0         # falta pegar
                            },
                        ],
                        "direction": None,              # falta pegar
                        "travel_time": float(trecho1.get("Duracao")),
                        # voos[0].get("Duracao")  ==>  converter "Duracao": "01:05",
                        "direct": None                  # falta pegar
                    }
                ],
                "carrier": {
                    "id": carrier.get("Id"),
                    "name": carrier.get("Descricao"),
                    "iata_code": carrier.get("CodigoIata")
                },
                "origin": trecho1.get("Origem", {}).get("CodigoIata"),
                "destination": trecho1.get("Destino", {}).get("CodigoIata"),
                "date_outbound": voos[0].get("DataSaida"),
                "date_inbound": voos[-1].get("DataChegada"),
                "adults": api_content.get("QuantidadeAdultos"),
                "children": api_content.get("QuantidadeCriancas"),
                "infants": api_content.get("QuantidadeBebes"),
                "direction": None,      # falta pegar
                "promocode": None       # falta pegar
            }
        ],
        "min_price": None,      # falta pegar
        "max_price": None,      # falta pegar
    }

print(response)
#
response = {
    'count': 1,
    'next': None,
    'previous': None,
    'results': [
        {
            'flights': [
                {
                    'id': 0,
                    'origin': {
                        'state': {
                            'country': {
                                'name': 'Brasil',
                                'code': 'BR'
                            },
                            'name': 'São Paulo',
                            'initials': 'SP'
                        },
                        'name': 'São Paulo'
                    },
                    'destination': {
                        'state': {
                            'country': {
                                'name': 'Brasil',
                                'code': 'BR'
                            },
                            'name': 'Amazonas',
                            'initials': 'AM'
                        },
                        'name': 'Manaus'
                    },
                    'links': [
                        {
                            'pricing': '/pricing?hash=81a7666c6967687473d9e05b7b226d6f64656c223a2022666c69676874732e666c69676874222c2022706b223a203532313739352c20226669656c6473223a207b226a6f75726e6579223a203133303830382c20226f726967696e223a2034333939302c202264657374696e6174696f6e223a2034343039352c2022646972656374696f6e223a20226f7574626f756e64222c202274726176656c5f74696d65223a2022333435222c202265787465726e616c5f6964223a202230222c2022646972656374223a2066616c73652c202270726f76696465725f726573706f6e7365223a206e756c6c7d7d5d'
                        }
                    ],
                    'segments': [
                        {
                            'origin': {
                                'name': 'Congonhas Airport',
                                'iata_code': 'CGH',
                                'city_name': 'São Paulo',
                                'state_name': 'São Paulo'
                            },
                            'destination': {
                                'name': 'Presidente Juscelino Kubistschek International Airport',
                                'iata_code': 'BSB',
                                'city_name': 'Brasília',
                                'state_name': 'Distrito Federal'
                            },
                            'carrier': {
                                'id': 0,
                                'name': 'Gol Linhas Aéreas',
                                'iata_code': 'G3'
                            },
                            'marketing_carrier': {
                                'id': 0,
                                'name': 'Gol Linhas Aéreas',
                                'iata_code': 'G3'
                            },
                            'date_departure': '2023-08-16T06:05:00-03:00',
                            'date_arrival': '2023-08-16T07:50:00-03:00',
                            'flight_number': '1015',
                            'flight_time': 105.0,
                            'distance': 540.0,
                            'equipment': '738',
                            'connection': False
                        }
                    ],
                    'prices': [
                        {
                            'id': 0,
                            'brand': {
                                'name': 'Promo',
                                'slug': 'promo',
                                'code': 'PRO'
                            },
                            'taxes': [
                                {
                                    'name': 'Taxes',
                                    'value': 82.29,
                                    'currency_code': 'BRL'
                                }
                            ],
                            'breakdown': [
                                {
                                    'pax_type': 'ADT',
                                    'pax_count': 1,
                                    'base': 1376.9,
                                    'taxes': 177.62,
                                    'total': 1554.52,
                                    'discount': 0.0,
                                    'currency_code': 'BRL'
                                }
                            ],
                            'links': {
                                'farerules': '/farerules?hash=1129347'
                            },
                            'base': 1376.9,
                            'total': 1554.52,
                            'baggage_included': False,
                            'baggage_pieces': 0,
                            'date_added': '2023-07-18T13:03:34.306030-03:00',
                            'fare_basis': 'ONJAAG1G',
                            'currency_code': 'BRL',
                            'promocode': None,
                            'discount': 0.0
                        },
                        {
                            'id': 1129348,
                            'brand': {
                                'name': 'Plus',
                                'slug': 'plus',
                                'code': 'PL'
                            },
                            'taxes': [
                                {
                                    'name': 'Taxes',
                                    'value': 188.62,
                                    'currency_code': 'BRL'
                                }
                            ],
                            'breakdown': [
                                {
                                    'pax_type': 'ADT',
                                    'pax_count': 1,
                                    'base': 1486.9,
                                    'taxes': 188.62,
                                    'total': 1675.52,
                                    'discount': 0.0,
                                    'currency_code': 'BRL'
                                }
                            ],
                            'links': {
                                'farerules': '/farerules?hash=1129348'
                            },
                            'base': 1486.9,
                            'total': 1675.52,
                            'baggage_included': True,
                            'baggage_pieces': 1,
                            'date_added': '2023-07-18T13:03:34.332392-03:00',
                            'fare_basis': 'UNJAAG3G',
                            'currency_code': 'BRL',
                            'promocode': None,
                            'discount': 0.0
                        },
                        {
                            'id': 1129349,
                            'brand': {
                                'name': 'Max',
                                'slug': 'max',
                                'code': 'MX'
                            },
                            'taxes': [
                                {
                                    'name': 'Taxes',
                                    'value': 201.32,
                                    'currency_code': 'BRL'
                                }
                            ],
                            'breakdown': [
                                {
                                    'pax_type': 'ADT',
                                    'pax_count': 1,
                                    'base': 1613.9,
                                    'taxes': 201.32,
                                    'total': 1815.22,
                                    'discount': 0.0,
                                    'currency_code': 'BRL'
                                }
                            ],
                            'links': {
                                'farerules': '/farerules?hash=1129349'
                            },
                            'base': 1613.9,
                            'total': 1815.22,
                            'baggage_included': True,
                            'baggage_pieces': 2,
                            'date_added': '2023-07-18T13:03:34.347763-03:00',
                            'fare_basis': 'UNJAAG4G',
                            'currency_code': 'BRL',
                            'promocode': None,
                            'discount': 0.0
                        }
                    ],
                    'direction': None,
                    'travel_time': 65.0,
                    'direct': None
                }
            ],
            'carrier': {
                'id': 0,
                'name': 'Gol Linhas Aéreas',
                'iata_code': 'G3'
            },
            'origin': 'SDU',
            'destination': 'CGH',
            'date_outbound': '/Date(1692797700000-0300)/',
            'date_inbound': '/Date(1692801600000-0300)/',
            'adults': 1,
            'children': 0,
            'infants': 0
        }
    ],
    'min_price': None,
    'max_price': None
}
