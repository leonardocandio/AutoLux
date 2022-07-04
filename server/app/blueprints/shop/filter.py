# apply filter in a data
def search_by_name(data, search: str, nitems: int):
    filter_list = []
    if search != '':
        for i in range(len(data)):
            # looking for similar values
            if search in data[i].brand.lower():
                filter_list.append(data[i])

            # looking for similar values
            if search in data[i].model.lower():
                filter_list.append(data[i])

            # looking for similar values
            if search in data[i].name.lower():
                filter_list.append(data[i])
    else:
        return data

    if nitems is None:
        return filter_list
    else:
        return filter_list[0:nitems]


def filter_by(data, by, search):
    filter_list = []
    if search == '':
        return []

    for i, _ in enumerate(data):
        if by == 'price':
            start_price = search[0]
            end_price = search[1]
            # looking for similar values
            if start_price < data[i].price < end_price:
                filter_list.append(data[i])

        if by == 'model':
            # looking for similar values
            if search in data[i].model.lower():
                filter_list.append(data[i])

        if by == 'brand':
            # looking for similar values
            if search in data[i].brand.lower():
                filter_list.append(data[i])

        if by == 'year':
            # looking for similar values
            if search == data[i].year:
                filter_list.append(data[i])

    return filter_list
