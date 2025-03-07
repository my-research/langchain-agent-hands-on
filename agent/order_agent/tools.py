import requests
from langchain.tools import tool

# 상품 목록 조회 API
@tool
def get_products() -> str:
    """Mock API에서 상품 목록을 가져오는 함수"""
    url = "http://localhost:1080/products"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "상품 목록을 가져오는 데 실패했습니다."

# 주문 생성 API
@tool
def place_order(user_id: int, product_id: int) -> str:
    """사용자의 주문을 Mock API에 요청하는 함수"""
    url = "http://localhost:1080/order"
    payload = {"userId": user_id, "productId": product_id}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["message"]
    return "주문 요청 실패"
