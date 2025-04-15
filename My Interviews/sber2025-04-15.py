from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


# factorial_service.py
class Service:
    def calculate_factorial(self, number: int) -> int:
        return _calculate_factorial(number)


# # container
# class Container(BaseModel):
#     service: Service


# def init_container() -> Container:
#     container = Container()
#     return container


# schemas.py
class Response(BaseModel):
    output: int


def _calculate_factorial(number: int) -> int:
    result = 1
    for i in range(2, number + 1):
        result *= i  # 120
    return result


# depends.py
# def get_factorial_service() -> Service:
#     container = init_container()
#     return container.factorial_service


@app.get("/{number}")
def calculate_factorial(number: int) -> Response:
    if number < 0 or number > 1_000:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    service = Service()
    result = service.calculate_factorial(number)
    return Response(output=result)
