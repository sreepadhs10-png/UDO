def parse_text(text):
    # placeholder deterministic parser
    # return parsed dict and confidence score
    parsed = {
        "origin": "HYD",
        "destination": "TIR",
        "depart_window": "next weekend",
        "passengers": [{"type":"adult","count":3},{"type":"child","count":1}],
        "constraints": {"direct_only": True, "max_price_per_person": 2000}
    }
    confidence = 0.8
    return parsed, confidence
