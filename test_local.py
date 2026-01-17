"""
Script test TranslateGemma local trước khi deploy lên Beam
Chỉ chạy nếu bạn có GPU đủ mạnh (ít nhất 32GB VRAM)
"""

from translategemma_app import translate

# Test 1: Dịch văn bản Tiếng Việt sang Tiếng Anh
print("Test 1: Dịch Tiếng Việt -> Tiếng Anh")
result = translate(
    type="text",
    source_lang="vi",
    target_lang="en",
    text="Xin chào, tôi là trợ lý AI. Tôi có thể giúp gì cho bạn?"
)
print(f"Kết quả: {result}\n")

# Test 2: Dịch văn bản Tiếng Anh sang Tiếng Việt
print("Test 2: Dịch Tiếng Anh -> Tiếng Việt")
result = translate(
    type="text",
    source_lang="en",
    target_lang="vi",
    text="Hello, I am an AI assistant. How can I help you today?"
)
print(f"Kết quả: {result}\n")

# Test 3: Dịch từ ảnh (nếu có URL ảnh)
print("Test 3: Dịch text từ ảnh")
result = translate(
    type="image",
    source_lang="cs",
    target_lang="vi",
    image_url="https://c7.alamy.com/comp/2YAX36N/traffic-signs-in-czech-republic-pedestrian-zone-2YAX36N.jpg"
)
print(f"Kết quả: {result}\n")
