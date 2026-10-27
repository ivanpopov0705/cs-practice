"""Обработка журнала наблюдений метеостанции."""


def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(
            f"Ожидается 3 поля, разделённых ';', получено {len(parts)}: {line!r}"
        )

    city, temp_str, date = parts

    if not city.strip():
        raise ValueError(f"Пустое название города: {line!r}")
    if not date.strip():
        raise ValueError(f"Пустая дата: {line!r}")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(
            f"Температура не является числом: {temp_str!r}"
        ) from None

    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records: list[dict] = []
    for line in lines:
        if not line:
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            #плохую строку молча пропускаем
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    total: dict[str, float] = {}
    count: dict[str, int] = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""

    total: dict[str, float] = {}
    count: dict[str, int] = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temp"]
        count[city] = count.get(city, 0) + 1

    averages = {city: total[city] / count[city] for city in total}
    return min(averages, key=lambda c: (-averages[c], c))
