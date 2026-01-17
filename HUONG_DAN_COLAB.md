# 🌍 Hướng dẫn chạy TranslateGemma 12B trên Google Colab

## Bước 1: Upload notebook lên Colab

1. Truy cập https://colab.research.google.com
2. Click **File** > **Upload notebook**
3. Chọn file `TranslateGemma_Colab.ipynb`

## Bước 2: Chọn GPU Runtime

**QUAN TRỌNG:** Phải chọn GPU để chạy model!

1. Click **Runtime** > **Change runtime type**
2. Chọn **Hardware accelerator**: **T4 GPU** (hoặc A100 nếu có)
3. Click **Save**

## Bước 3: Chạy từng cell

Chạy lần lượt các cell từ trên xuống:

### Cell 1: Cài đặt thư viện (~30 giây)

```python
!pip install -q transformers>=4.46.0 torch pillow accelerate sentencepiece protobuf
```

### Cell 2: Load model (~1-2 phút)

```python
# Load TranslateGemma 12B
model_id = "google/translategemma-12b-it"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(...)
```

**Lưu ý:** Lần đầu load sẽ mất 1-2 phút để download model (~25GB)

### Cell 3: Định nghĩa hàm dịch

```python
def translate_text(text, source_lang="vi", target_lang="en"):
    ...
```

### Cell 4-7: Test các ví dụ

- Dịch Tiếng Việt → Tiếng Anh
- Dịch Tiếng Anh → Tiếng Việt
- Dịch Tiếng Việt → Tiếng Trung
- Dịch text từ ảnh

### Cell 8: Dịch văn bản của bạn

Thay đổi text và ngôn ngữ theo ý muốn!

## Ví dụ sử dụng

### Dịch văn bản

```python
# Tiếng Việt -> Tiếng Anh
result = translate_text(
    "Xin chào thế giới!",
    source_lang="vi",
    target_lang="en"
)
print(result)  # Hello world!

# Tiếng Anh -> Tiếng Trung
result = translate_text(
    "I love learning languages",
    source_lang="en",
    target_lang="zh"
)
print(result)  # 我喜欢学习语言
```

### Dịch từ ảnh

```python
result = translate_image(
    "https://example.com/image.jpg",
    source_lang="en",
    target_lang="vi"
)
print(result)
```

## Ngôn ngữ hỗ trợ (55 ngôn ngữ)

| Mã   | Ngôn ngữ       | Mã   | Ngôn ngữ             |
| ---- | -------------- | ---- | -------------------- |
| `vi` | Tiếng Việt 🇻🇳  | `en` | Tiếng Anh 🇺🇸         |
| `zh` | Tiếng Trung 🇨🇳 | `ja` | Tiếng Nhật 🇯🇵        |
| `ko` | Tiếng Hàn 🇰🇷   | `fr` | Tiếng Pháp 🇫🇷        |
| `de` | Tiếng Đức 🇩🇪   | `es` | Tiếng Tây Ban Nha 🇪🇸 |
| `th` | Tiếng Thái 🇹🇭  | `id` | Tiếng Indonesia 🇮🇩   |
| `cs` | Tiếng Séc 🇨🇿   | `ru` | Tiếng Nga 🇷🇺         |
| `ar` | Tiếng Ả Rập 🇸🇦 | `pt` | Tiếng Bồ Đào Nha 🇵🇹  |
| `it` | Tiếng Ý 🇮🇹     | `nl` | Tiếng Hà Lan 🇳🇱      |

Và 39 ngôn ngữ khác!

## Lưu ý quan trọng

### GPU Runtime

- **Colab Free**: T4 GPU (16GB VRAM) - Chạy tốt model 12B
- **Colab Pro**: A100 GPU (40GB VRAM) - Chạy rất nhanh
- **Thời gian sử dụng**: Colab Free giới hạn ~12 giờ/session

### Tối ưu hóa

- Model 12B nhẹ hơn 27B, chạy nhanh hơn trên T4 GPU
- Model chỉ load 1 lần, sau đó dịch nhanh (~1-3 giây/câu)
- Nếu session timeout, phải load lại model
- Để giữ session: Click vào notebook thường xuyên

### Lỗi thường gặp

**1. "Runtime disconnected"**

- Nguyên nhân: Hết thời gian GPU miễn phí
- Giải pháp: Đợi vài giờ hoặc nâng cấp Colab Pro

**2. "CUDA out of memory"**

- Nguyên nhân: GPU không đủ VRAM
- Giải pháp: Runtime > Restart runtime, chạy lại từ đầu

**3. "Model not found"**

- Nguyên nhân: Chưa chạy cell load model
- Giải pháp: Chạy lại Cell 2 (Load model)

## So sánh với Beam.cloud

| Tiêu chí      | Google Colab           | Beam.cloud        |
| ------------- | ---------------------- | ----------------- |
| **Chi phí**   | Miễn phí (có giới hạn) | $3-4/giờ GPU H100 |
| **GPU**       | T4 (16GB) hoặc A100    | H100 (80GB)       |
| **Tốc độ**    | Trung bình             | Rất nhanh         |
| **Thời gian** | ~12 giờ/session        | Không giới hạn    |
| **API**       | Không                  | Có REST API       |
| **Sử dụng**   | Cá nhân, thử nghiệm    | Production, scale |

## Kết luận

**Dùng Colab khi:**

- Bạn muốn dùng miễn phí
- Dịch thuật cá nhân, không thường xuyên
- Học tập, thử nghiệm

**Dùng Beam.cloud khi:**

- Cần API để tích hợp vào app
- Cần tốc độ nhanh, ổn định
- Sử dụng thương mại, production

## Liên kết hữu ích

- [Google Colab](https://colab.research.google.com)
- [TranslateGemma Model Card](https://huggingface.co/google/translategemma-12b-it)
- [Colab Pro](https://colab.research.google.com/signup)

---

**Chúc bạn dịch thuật vui vẻ! 🎉**
