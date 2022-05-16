

# apply filter in a data
def filter(data, search: str):
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

    return filter_list