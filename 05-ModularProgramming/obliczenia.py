import statistics

def obliczenia(dane):
    srednia = statistics.mean(data)
    mediana = statistics.median(data)
    min = min(data)
    max = max(data)
    return [srednia, mediana, min, max]