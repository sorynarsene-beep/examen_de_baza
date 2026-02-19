Problema 1 — Transactions parsing & aggregation
from typing import List, Dict, Tuple, Optional

def parse_transactions(lines: List[str]) -> List[Dict]:
    result = []

    for line in lines:
        parts = line.split(";")

        # verificam daca sunt exact 3 campuri
        if len(parts) != 3:
            continue

        name, category, amount_str = parts

        try:
            amount = float(amount_str)
        except ValueError:
            # suma nu este numar valid
            continue

        result.append({
            "name": name,
            "category": category,
            "amount": amount
        })

    return result
Complexitate
O(n)



def totals_by_category(transactions: List[Dict]) -> Dict[str, float]:
    totals = {}

    for t in transactions:
        category = t["category"]
        amount = t["amount"]

        totals[category] = totals.get(category, 0.0) + amount

    # rotunjire la 2 zecimale
    for category in totals:
        totals[category] = round(totals[category], 2)

    return totals



def top_spender(transactions: List[Dict]) -> Tuple[Optional[str], float]:
    if not transactions:
        return (None, 0.0)

    totals = {}

    # agregam sumele pe persoana
    for t in transactions:
        name = t["name"]
        amount = t["amount"]
        totals[name] = totals.get(name, 0.0) + amount

    max_name = None
    max_total = -1.0

    for name, total in totals.items():
        if (
            total > max_total or
            (total == max_total and (max_name is None or name < max_name))
        ):
            max_total = total
            max_name = name

    return (max_name, max_total)
    Complexitate
    O(n)



Problema 2 — Max length subarray with sum k (O(n))

def max_len_subarray_sum_k(nums: List[int], k: int) -> int:
    prefix_sum = 0
    max_len = 0

    # retinem prima aparitie a fiecarui prefix sum
    prefix_map = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += num

        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_len = max(max_len, length)

        # salvam doar prima aparitie
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len

Complexitate
Timp: O(n)
Spatiu: O(n)

