from datetime import datetime

def strptime(date_string, dt_format, default_format=None):
    try:
        return datetime.strptime(date_string, dt_format)
    except (ValueError, TypeError):
        return datetime.strptime(date_string, default_format)
    except:
        raise ValueError(
            f"Формат даты {date_string} не соответствует ни одному из возможных - [{dt_format}, {default_format}]"
        )

