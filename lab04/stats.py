def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(
            f"Ожидается 3 поля, разделённых ';', получено {len(parts)}: {line!r}"
        )

    city, temp_str, date = parts

    city = city.strip()
    date = date.strip()

    if not city:
        raise ValueError(f"Пустое название города: {line!r}")
    if not date:
        raise ValueError(f"Пустая дата: {line!r}")

    temp_str = temp_str.strip().replace(",", ".")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(
            f"Температура не является числом: {temp_str!r}"
        ) from None

    return {"city": city, "temperature": temp, "date": date}
