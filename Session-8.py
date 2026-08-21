"""
Name: SUCHITRA YADAWAD
Training ID: PYT_07/26_WD_PM_BATCH1
Module Title: Session 7 - Modular Code II
"""


# -------------------- Task 1 --------------------
# The Multi-Vector Firewall (*args & kwargs)
print("-" * 10 + " Task 1 " + "-" * 10)

def analyze_traffic(source_name, *ips, **metadata):
    """
    LEGB:
    Local: source_name, ips, metadata inside this function.
    Enclosing: No enclosing function is used.
    Global: The function itself is defined in the global scope.
    Built-in: len() and other built-in functions can be accessed if needed.
    """
    return f"Source: {source_name} | Analyzed {len(ips)} IPs | Security Tags: {', '.join(metadata.keys())}"


result = analyze_traffic(
    "Mainframe_A",
    "192.168.1.1",
    "172.16.0.1",
    "10.0.0.5",
    threat_level="High",
    protocol="SSH"
)

print(result)


# -------------------- Task 2 --------------------
# The Instant Payload Decoder (Lambda & Map)
print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

def decode_payload(payload):
    """
    LEGB:
    Local: payload is local to this function.
    Enclosing: No enclosing scope is used.
    Global: map() and lambda are used within the function's global definition.
    Built-in: map() is a Python built-in function.
    """
    return list(map(lambda x: x * 2 if x % 2 == 0 else x + 5, payload))


payload = [10, 15, 20, 25]

result = decode_payload(payload)

print(result)


# -------------------- Task 3 --------------------
# The Darknet Traffic Purge (Filter & Scope)
print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

BLACKLIST_RANGE = range(1000, 2000)


def filter_ports(ports):
    """
    LEGB:
    Local: BLACKLIST_RANGE inside this function is checked first.
    Enclosing: No enclosing function is present.
    Global: The global BLACKLIST_RANGE is accessed using globals().
    Built-in: filter() and range() are built-in functions.

    The local BLACKLIST_RANGE shadows the global BLACKLIST_RANGE.
    """
    BLACKLIST_RANGE = range(0, 500)

    return list(filter(lambda port: port not in globals()["BLACKLIST_RANGE"], ports))


ports = [80, 443, 1050, 21, 1500]

result = filter_ports(ports)

print(result)


# -------------------- Task 4 --------------------
# The Signature Hash Aggregator (Reduce)
print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

from functools import reduce


def aggregate_tokens(tokens):
    """
    LEGB:
    Local: tokens is the local parameter of this function.
    Enclosing: No enclosing function is used.
    Global: reduce is imported and available in the global scope.
    Built-in: No special built-in function is required for the calculation.

    The lambda calculates the cumulative product. If multiplying the
    current product by the next token reaches the limit of 1,000,000,
    the accumulator resets to 1000. The next token is then multiplied
    with this reset value.
    """
    return reduce(
        lambda product, token:
        product * token if product * token < 1000000 else 1000,
        tokens
    )


tokens = [10, 100, 5, 200, 2]

result = aggregate_tokens(tokens)

print(result)


# -------------------- Task 5 --------------------
# The Modular Threat Dispatcher (Higher-Order Functions)
print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

def security_engine(data_stream, strategy):
    """
    LEGB:
    Local: data_stream and strategy are local parameters.
    Enclosing: No enclosing function is used.
    Global: The function is defined in the global scope.
    Built-in: map() and filter() are built-in functions.
    """
    boosted_data = map(lambda x: x * 1.5, data_stream)
    return strategy(boosted_data)


def noise_reduction(data):
    """
    LEGB:
    Local: data is local to this function.
    Enclosing: No enclosing function is used.
    Global: The function is defined in the global scope.
    Built-in: filter() and list() are built-in functions.
    """
    return list(filter(lambda x: x > 100, data))


raw_stream = [50, 80, 120, 200]

result = security_engine(raw_stream, noise_reduction)

print(result)