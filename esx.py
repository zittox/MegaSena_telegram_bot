def ultimo_resultado():
    r = requests.get(apicaixa).json()
    data = {
        'concurso': r['concurso'],
        'data': r['data'],
        'dezenas': r['dezenas'],
        'acumulou': 'Sim' if r['acumulou'] else 'Não',
        'prox_premio': r['acumuladaProxConcurso'],
        'prox_concurso': r['dataProxConcurso']
    }
    return data