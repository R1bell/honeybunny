from typing import Dict

RESPONSE: Dict[int, str] = {
    200: "Success",
    401: "Unauthorized",
    404: "Not Found",
    409: "Already Exists"
}


def get_codes(*codes) -> Dict[int, str]:
    return {
        code: RESPONSE.get(code)
        for code in codes
        if RESPONSE.get(code)
    }
