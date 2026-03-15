def evaluate_rules(parsed):
    # simple mock: if direct_only and max_price < 2000, return connecting flight primary
    scenarios = []
    if parsed['constraints'].get('direct_only') and parsed['constraints'].get('max_price_per_person') < 2000:
        scenarios.append({
            "type":"primary",
            "mode":"flight",
            "reason":"No direct flights under budget; showing connecting flight",
            "price_per_person":1950,
            "stops":1
        })
        scenarios.append({
            "type":"backup",
            "mode":"flight",
            "reason":"Direct flight exists but over budget",
            "price_per_person":2600,
            "stops":0
        })
    else:
        scenarios.append({"type":"primary","mode":"flight","price_per_person":2500,"stops":0})
    return scenarios
