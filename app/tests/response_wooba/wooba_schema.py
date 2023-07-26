from typing import Any

from pydantic import BaseModel, Field, StrictInt, StrictFloat

from main import app


class Fornecedor(BaseModel):
    id: StrictInt | None = Field(default=None, alias="Id")
    codigo: StrictInt | None = Field(default=None, alias="Codigo")
    nome: str | None = Field(default=None, alias="Nome")


class CiaOrigemDestino(BaseModel):
    id: StrictInt | None = Field(default=None, alias="Id")
    codigo_iata: str | None = Field(default=None, alias="CodigoIata")
    descricao: str | None = Field(default=None, alias="Descricao")


class BaseTarifaria(BaseModel):
    id: StrictInt = Field(default=None, alias="Id")
    classe: str | None = Field(default=None, alias="Classe")
    codigo: str | None = Field(default=None, alias="Codigo")
    familia: str | None = Field(default=None, alias="Familia")


class PrecoIndividual(BaseModel):
    id: StrictInt | StrictFloat | None = Field(default=None, alias="Id")
    eq_valor_tarifa: StrictInt | StrictFloat | None = Field(default=None, alias="EqValorTarifa")
    eq_valor_taxa_servico: StrictInt | StrictFloat | None = Field(default=None, alias="EqValorTaxaServico")
    faixa_etaria: str | None = Field(default=None, alias="FaixaEtaria")
    quantidade: StrictInt | None = Field(default=None, alias="Quantidade")
    valor_fee: StrictInt | StrictFloat | None = Field(default=None, alias="ValorFee")
    valor_rav: StrictInt | StrictFloat | None = Field(default=None, alias="ValorRav")
    valor_tarifa: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTarifa")
    valor_tarifa_net: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTarifaNet")
    valor_taxa_assento: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTaxaAssento")
    valor_taxa_bagagem: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTaxaBagagem")
    valor_taxa_combustivel: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTaxaCombustivel")
    valor_taxa_embarque: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTaxaEmbarque")
    valor_taxa_menor_desacompanhado: StrictInt | StrictFloat | None = Field(default=None,
                                                                            alias="ValorTaxaMenorDesacompanhado")
    valor_taxa_servico: StrictInt | StrictFloat | None = Field(default=None, alias="ValorTaxaServico")


class Preco(BaseModel):
    id: StrictInt | None = Field(default=None, alias="Id")
    eq_cambio: StrictInt | None = Field(default=None, alias="EqCambio")
    eq_moeda: bool | None = Field(default=None, alias="EqMoeda")
    moeda: str | None = Field(default=None, alias="Moeda")
    preco_adulto: PrecoIndividual | None = Field(default=None, alias="PrecoAdulto")
    preco_bebe: PrecoIndividual | None = Field(default=None, alias="PrecoBebe")
    preco_crianca: PrecoIndividual | None = Field(default=None, alias="PrecoCrianca")
    tarifa: StrictInt | None = Field(default=None, alias="Tarifa")
    tarifa_operadora: bool | None = Field(default=None, alias="TarifaOperadora")
    tarifa_privada: bool | None = Field(default=None, alias="TarifaPrivada")
    taxa: StrictInt | StrictFloat | None = Field(default=None, alias="Taxa")
    total: StrictInt | StrictFloat | None = Field(default=None, alias="Total")
    total_geral: StrictInt | StrictFloat | None = Field(default=None, alias="TotalGeral")
    total_tarifa: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTarifa")
    total_tarifaNet: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTarifaNet")
    total_taxa_assento: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTaxaAssento")
    total_taxa_bagagem: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTaxaBagagem")
    total_taxa_de_combustivel: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTaxaDeCombustivel")
    total_taxa_embarque: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTaxaEmbarque")
    total_taxa_menor_desacompanhado: StrictInt | StrictFloat | None = Field(default=None,
                                                                            alias="TotalTaxaMenorDesacompanhado")
    total_taxa_servico: StrictInt | StrictFloat | None = Field(default=None, alias="TotalTaxaServico")
    valor_emd: StrictInt | StrictFloat | None = Field(default=None, alias="ValorEMD")
    valor_fee: StrictInt | StrictFloat | None = Field(default=None, alias="ValorFEE")
    valor_rav: StrictInt | StrictFloat | None = Field(default=None, alias="ValorRAV")


class ListaDeClasses(BaseModel):
    bagagem_inclusa: bool | None = Field(default=None, alias="BagagemInclusa")
    bagagem_indicador: StrictInt | None = Field(default=None, alias="BagagemIndicador")
    bagagem_peso: StrictInt | None = Field(default=None, alias="BagagemPeso")
    bagagem_quantidade: StrictInt | None = Field(default=None, alias="BagagemQuantidade")
    bagagem_unidade_de_medida: str | None = Field(default=None, alias="BagagemUnidadeDeMedida")
    base_tarifaria: str | None = Field(default=[], alias="BaseTarifaria")
    cabine: str | None = Field(default=None, alias="Cabine")
    classe: str | None = Field(default=None, alias="Classe")
    familia: str | None = Field(default=None, alias="Familia")
    familia_codigo: str | None = Field(default=None, alias="FamiliaCodigo")
    moeda: str | None = Field(default=None, alias="Moeda")
    perfil: Any | None = Field(default=None, alias="Perfil")
    preco: Preco | None = Field(default=None, alias="Preco")
    tarifa_adulto: StrictInt | StrictFloat | None = Field(default=None, alias="TarifaAdulto")
    tarifa_beba: StrictInt | StrictFloat | None = Field(default=None, alias="TarifaBeba")
    tarifa_crianca: StrictInt | StrictFloat | None = Field(default=None, alias="TarifaCrianca")
    tpo: str | None = Field(default=None, alias="Tipo")


class Voos(BaseModel):
    id: StrictInt | None = Field(default=None, alias="Id")
    bagagem_inclusa: bool | None = Field(default=None, alias="BagagemInclusa")
    bagagem_indicador: StrictInt | None = Field(default=None, alias="BagagemIndicador")
    bagagem_peso: StrictInt | None = Field(default=None, alias="BagagemPeso")
    bagagem_quantidade: StrictInt | None = Field(default=None, alias="BagagemQuantidade")
    bagagem_unidade_de_medida: str | None = Field(default=None, alias="BagagemUnidadeDeMedida")
    base_tarifaria: list[BaseTarifaria] | None = Field(default=[], alias="BaseTarifaria")
    cabine: str | None = Field(default=None, alias="Cabine")
    campo1: bool | None = Field(default=None, alias="Campo1")
    cia_mandatoria: CiaOrigemDestino | None = Field(default=None, alias="CiaMandatoria")
    cia_operacional: CiaOrigemDestino | None = Field(default=None, alias="CiaOperacional")
    classe: str | None = Field(default=None, alias="Classe")
    companhia: bool | None = Field(default=None, alias="Companhia")
    conexao: bool | None = Field(default=None, alias="Conexao")
    data_chegada: str | None = Field(default=None, alias="DataChegada")
    data_saida: str | None = Field(default=None, alias="DataSaida")
    destino: CiaOrigemDestino | None = Field(default=None, alias="Destino")
    duracao: str | None = Field(default=None, alias="Duracao")
    equipamento: str | None = Field(default=None, alias="Equipamento")
    escalas: bool | None = Field(default=None, alias="Escalas")
    familia: str | None = Field(default=None, alias="Familia")
    familia_codigo: str | None = Field(default=None, alias="FamiliaCodigo")
    grupo_de_segmento: StrictInt | None = Field(default=None, alias="GrupoDeSegmento")
    hora_chegada: str | None = Field(default=None, alias="HoraChegada")
    hora_saida: str | None = Field(default=None, alias="HoraSaida")
    icone: str | None = Field(default=None, alias="Icone")
    linha: bool | None = Field(default=None, alias="Linha")
    lista_de_classes: list[ListaDeClasses] | None = Field(default=None, alias="ListaDeClasses")  # criar classe
    localizador_companhia: bool | None = Field(default=None, alias="LocalizadorCompanhia")
    numero: str | None = Field(default=None, alias="Numero")
    origem: CiaOrigemDestino | None = Field(default=None, alias="Origem")
    quantidade_paradas: StrictInt | None = Field(default=None, alias="QuantidadeParadas")
    referencia: bool | None = Field(default=None, alias="Referencia")
    referencia_do_segmento: bool | None = Field(default=None, alias="ReferenciaDoSegmento")
    segmento: str | None = Field(default=None, alias="Segmento")
    status: bool | None = Field(default=None, alias="Status")


class ViagensTrecho(BaseModel):
    cia_mandatoria: CiaOrigemDestino | None = Field(default=None, alias="CiaMandatoria")
    destino: CiaOrigemDestino | None = Field(default=None, alias="Destino")
    duracao: StrictInt | StrictFloat | None = Field(default=None, alias="Duracao")
    fornecedor: Fornecedor | None = Field(default=None, alias="Fornecedor")
    id: StrictInt | None = Field(default=None, alias="Id")
    identificacao_da_viagem: str | None = Field(default=None, alias="IdentificacaoDaViagem")
    numero_paradas: StrictInt | None = Field(default=None, alias="NumeroParadas")
    origem: CiaOrigemDestino | None = Field(default=None, alias="Origem")
    preco: dict | None = Field(default=None, alias="Preco")
    rota: bool | None = Field(default=None, alias="Rota")
    segmento: str | None = Field(default=None, alias="Segmento")
    sub_fornecedor: bool | None = Field(default=None, alias="SubFornecedor")
    tempo_de_duracao: str | None = Field(default=None, alias="TempoDeDuracao")
    voos: Voos | None = Field(default=[], alias="Voos")


class ApiContent(BaseModel):
    data: str | None = Field(default=None, alias="Data")
    data_versao: str | None = Field(default=None, alias="DataVersao")
    sessao_expirada: bool | None = Field(default=None, alias="SessaoExpirada")
    cia: list[CiaOrigemDestino] | None = Field(default=[], alias="Cia")
    data_ida: str | None = Field(default=None, alias="DataIda")
    data_volta: str | None = Field(default=None, alias="DataVolta")
    destino: CiaOrigemDestino | None = Field(default={}, alias="Destino")
    exception: bool | None = Field(default=None, alias="Exception")
    exception_por_sistema: bool | None = Field(default=None, alias="ExceptionPorSistema")
    origem: CiaOrigemDestino | None = Field(default={}, alias="Origem")
    quantidade_adultos: int | None = Field(default=None, alias="QuantidadeAdultos")
    quantidade_bebes: int | None = Field(default=None, alias="QuantidadeBebes")
    quantidade_criancas: int | None = Field(default=None, alias="QuantidadeCriancas")
    recomendacoes: bool | None = Field(default=None, alias="Recomendacoes")
    rota: str | None = Field(default=None, alias="Rota")
    tempo_pesquisa: str | None = Field(default=None, alias="TempoPesquisa")
    viagens_multiplos_trechos: bool | None = Field(default=None, alias="ViagensMultiplosTrechos")
    viagens_trecho1: list[ViagensTrecho] = Field(default=[], alias="ViagensTrecho1")
    viagens_trecho2: list[ViagensTrecho] = Field(default=[], alias="ViagensTrecho2")


# @app_wooba.post("/results/")
# @app_wooba.post("/results/", response_model=ApiContent)
@app.post("/results/", response_model=ApiContent, response_model_exclude_unset=True)
# @app_wooba.post("/results/", response_model=ApiContent, response_model_exclude_defaults=True)
# @app_wooba.post("/results/", response_model=ApiContent, response_model_exclude_none=True)
# @app_wooba.post("/results/", response_model=ApiContent, response_model_exclude_defaults=True, response_model_exclude_none=True)
async def get_results(response: ApiContent):
    return response
