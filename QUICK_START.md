# 🚀 Quick Start - TranslateGemma 12B

## Các bước nhanh (5 phút)

### 1️⃣ Xin quyền truy cập model

👉 https://huggingface.co/google/translategemma-12b-it

- Đăng nhập Hugging Face
- Click **"Agree and access repository"**
- Đợi vài giây (tự động chấp thuận)

### 2️⃣ Tạo Hugging Face Token

👉 https://huggingface.co/settings/tokens

- Click **"New token"**
- Tên: `colab-translategemma`
- Quyền: **Read**
- Copy token (bắt đầu `hf_...`)

### 3️⃣ Upload notebook lên Colab

👉 https://colab.research.google.com

- File > Upload notebook
- Chọn `TranslateGemma_Colab.ipynb`

### 4️⃣ Chọn GPU

- Runtime > Change runtime type
- Hardware accelerator: **T4 GPU**
- Save

### 5️⃣ Chạy các cell

1. **Cell 1**: Cài đặt thư viện (~30s)
2. **Cell 2**: Login - paste token vào (~5s)
3. **Cell 3**: Load model (~1-2 phút)
4. **Cell 4**: Định nghĩa hàm
5. **Cell 5-8**: Test dịch thuật
6. **Cell 9**: Dịch văn bản của bạn

## ✅ Xong!

Bây giờ bạn có thể dịch thuật giữa 55 ngôn ngữ miễn phí!

```python
# Ví dụ
result = translate_text(
    "Xin chào thế giới!",
    source_lang="vi",
    target_lang="en"
)
print(result)  # Hello world!
```

## ❓ Gặp lỗi?

**"Gated repo" / "Unauthorized"**
→ Chưa xin quyền hoặc token sai
→ Làm lại bước 1 và 2

**"CUDA out of memory"**
→ Runtime > Restart runtime
→ Chạy lại từ đầu

**"Runtime disconnected"**
→ Hết thời gian GPU miễn phí
→ Đợi vài giờ hoặc nâng cấp Colab Pro

## 📚 Đọc thêm

- [Hướng dẫn chi tiết](./HUONG_DAN_COLAB.md)
- [Model card](https://huggingface.co/google/translategemma-12b-it)
