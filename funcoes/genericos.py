import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

def filtro_dinheiro(valor):
    try:
        dinheiro = float(valor)
        return moeda(dinheiro)
    except:
        pass

    try:
        dinheiro = valor.replace(".", "")
        dinheiro = dinheiro.replace(",", ".")
        return moeda(dinheiro)
    except:
        pass

    return moeda(valor)


def moeda(valor):
    valor = float(valor)
    return locale.currency(valor, grouping=True)

    
