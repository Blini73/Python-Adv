from typing import Optional, Any, List, Union

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name())

def proccess_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return F"Number: {value}"
    return f"String: {value}"

print(proccess_value(11))

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)
numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)