# Hướng dẫn Deploy TranslateGemma 27B lên Beam.cloud

## Bước 1: Cài đặt Beam SDK

```bash
pip install beam-client
```

## Bước 2: Cấu hình API Token

1. Truy cập https://platform.beam.cloud/settings/api-keys
2. Lấy API token của bạn
3. Chạy lệnh (thay [TOKEN] bằng token thực):

```bash
beam configure default --token [TOKEN]
```

## Bước 3: Deploy lên Beam

```bash
beam deploy translategemma_app.py:translate
```

## Bước 4: Sử dụng API

### Dịch văn bản (Text Translation)

```bash
curl -X POST 'https://app.beam.cloud/endpoint/translategemma-27b' \
  -H 'Authorization: Bearer [TOKEN]' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "text",
    "source_lang": "vi",
    "target_lang": "en",
    "text": "Xin chào, tôi là trợ lý AI"
  }'
```

### Dịch từ ảnh (Image to Text Translation)

```bash
curl -X POST 'https://app.beam.cloud/endpoint/translategemma-27b' \
  -H 'Authorization: Bearer [TOKEN]' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "image",
    "source_lang": "cs",
    "target_lang": "vi",
    "image_url": "https://c7.alamy.com/comp/2YAX36N/traffic-signs-in-czech-republic-pedestrian-zone-2YAX36N.jpg"
  }'
```

## Các ngôn ngữ được hỗ trợ

TranslateGemma hỗ trợ 55 ngôn ngữ. Một số mã ngôn ngữ phổ biến:

- `vi` - Tiếng Việt
- `en` - Tiếng Anh
- `en-US` - Tiếng Anh (Mỹ)
- `en-GB` - Tiếng Anh (Anh)
- `zh` - Tiếng Trung
- `ja` - Tiếng Nhật
- `ko` - Tiếng Hàn
- `fr` - Tiếng Pháp
- `de` - Tiếng Đức
- `es` - Tiếng Tây Ban Nha
- `th` - Tiếng Thái
- `id` - Tiếng Indonesia
- `cs` - Tiếng Séc

## Tham số tùy chọn

- `max_tokens`: Số token tối đa cho output (mặc định: 200)

## Ví dụ với Python

```python
import requests

url = "https://app.beam.cloud/endpoint/translategemma-27b"
headers = {
    "Authorization": "Bearer [TOKEN]",
    "Content-Type": "application/json"
}

# Dịch văn bản
data = {
    "type": "text",
    "source_lang": "vi",
    "target_lang": "en",
    "text": "Hôm nay trời đẹp quá!"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

## Lưu ý

- Model 27B cần GPU H100 (80GB VRAM) để chạy tốt
- Lần đầu tiên gọi API sẽ mất thời gian load model (~30-60s)
- Sau đó model sẽ được cache và phản hồi nhanh hơn
- `keep_warm_seconds=300` giữ model warm trong 5 phút để tránh cold start

## Chi phí

- Bạn chỉ trả tiền cho thời gian compute thực tế sử dụng
- GPU H100: ~$3-4/giờ
- Tài khoản mới có 15 giờ credit miễn phí

## Kiểm tra trạng thái

Xem logs và metrics tại: https://platform.beam.cloud
