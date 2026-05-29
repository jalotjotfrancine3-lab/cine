def check_compatibility(parts):
    errors = []
    warnings = []
    suggestions = []

    cpu = parts.get("cpu")
    motherboard = parts.get("motherboard")
    ram = parts.get("ram")
    psu = parts.get("psu")
    gpu = parts.get("gpu")

    # CPU + Motherboard
    if cpu and motherboard:
        if cpu["socket"] != motherboard["socket"]:
            errors.append("CPU and motherboard are incompatible")
            suggestions.append("Use matching socket motherboard")
            suggestions.append("Or change CPU")

    # PSU check
    if psu and gpu:
        if psu["wattage"] < gpu["required_wattage"]:
            warnings.append("PSU too weak")
            suggestions.append("Upgrade PSU to 650W+")

    # RAM check
    if ram and ram["size"] < 16:
        suggestions.append("Upgrade RAM to 16GB")

    return {
        "errors": errors,
        "warnings": warnings,
        "suggestions": suggestions
    }