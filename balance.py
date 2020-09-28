def CFIM_resolve_balance(debit_balance, credit_balance):
    b = {
        "BalanceType": "None",
        "Balance": 0,
    }

    debit = float(debit_balance) - float(credit_balance)
    credit = float(credit_balance) - float(debit_balance)

    if debit == 0:
        return b
    elif debit < 0:
        b["BalanceType"] = "Credit"
        b["Balance"] = credit
        return b
    else:
        b["BalanceType"] = "Debit"
        b["Balance"] = debit
        return b


print(CFIM_resolve_balance(125.22, 65.08))