def code_signal_container_exercise(queries):
    value_set = set()
    values = []
    results = []

    for operation, value_str in queries:
        value = int(value_str)

        if operation == 'ADD':
            if value not in value_set:
                value_set.add(value)
                inserted = False
                for j in range(len(values)):
                    if values[j] > value:
                        values.insert(j, value)
                        inserted = True
                        break
                if not inserted:
                    values.append(value)
            results.append('')
        elif operation == 'REMOVE':
            existed = value in value_set
            if existed:
                value_set.remove(value)
                values.remove(value)
            results.append(str(existed).lower())
        elif operation == 'EXISTS':
            results.append(str(value in value_set).lower())
        elif operation == 'NEXT_UP':
            next_value = ''
            for candidate in values:
                if candidate > value:
                    next_value = str(candidate)
                    break
            results.append(next_value)
        else:
            results.append('')
    return results
