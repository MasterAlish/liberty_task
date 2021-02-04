BANK_CSV_CONFIGS = {
    "bank1": {
        "has_header": True,
        "columns_order": ["created_date", "type", "amount", "source", "destination"],
        "date_format": "%b %d %Y"
    },
    "bank2": {
        "has_header": True,
        "columns_order": ["created_date", "type", "amount", "destination", "source"],
        "date_format": "%d-%m-%Y"
    },
    "bank3": {
        "has_header": True,
        "columns_order": ["created_date", "type", "amount", "amount_hundredth", "destination", "source"],
        "date_format": "%d %b %Y"
    },
}

OUTPUT_DATE_FORMAT = "%d %b %Y"
