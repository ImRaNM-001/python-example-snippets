import inspect
from types import FrameType
from typing import Optional

# initializing function
def get_function_name() -> Optional[str]:

    # get the frame object of the function
    frame: FrameType | None = inspect.currentframe()
    if frame is not None:
        return frame.f_code.co_name
    return None

# printing function name
print('The name of function is : ', get_function_name())                        # test_function
print('The type of function is : ', type(get_function_name))                    #  <class 'function'>  