def get_qs_tuple(model):
    res = []
    qs = model.objects.all()
    for i in range(0, len(qs)):
        res.append((i, qs[i]))
    return res
