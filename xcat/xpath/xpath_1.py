from . import Function


position = Function("position")
count = Function("count")

translate = Function("translate", args_count=3)
string = Function("string")
concat = Function("concat")
starts_with = Function("starts-with")
contains = Function("contains")
substring = Function("substring", args_count=3)
substring_before = Function("substring-before", args_count=2)
substring_after = Function("substring-after", args_count=2)
string_length = Function("string-length")
normalize_space = Function("normalize-space")
not_ = Function("not")
true_ = Function("true")
false_ = Function("false")
sum_ = Function("sum")
name = Function("name", args_count=1)
boolean = Function("boolean", args_count=1)
function_available = Function('function-available')