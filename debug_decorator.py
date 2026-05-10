import functools


def debug(*test_inputs, exec=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        if exec:
            print(f"\033[1;34m🚀 Auto-Testing: [{func.__name__}]\033[0m")
            for i, case in enumerate(test_inputs, 1):
                # 核心改进：
                # 如果 case 是元组，就解包传参；如果不是，就当成单参数传
                if isinstance(case, tuple):
                    result = func(*case)
                    display_input = ", ".join(map(repr, case))
                else:
                    result = func(case)
                    display_input = repr(case)

                print(f"  \033[1;32mTest {i}:\033[0m ({display_input})")
                print(f"  \033[1;33mResult ->\033[0m {result}")
                print(f"  {'-' * 30}")
        return wrapper
    return decorator

# @debug("wjj",exec=True)
# def test_hello(name):
#     print(f"Hello,{name}!")
