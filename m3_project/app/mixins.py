def get_qs_tuple(model):
    res = []
    qs = model.objects.all()
    for i in range(1, len(qs) + 1):
        res.append((i, qs[i]))
    return res
