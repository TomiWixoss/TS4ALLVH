from beam import endpoint, Image
import torch

# Cấu hình image với các dependencies cần thiết
image = (
    Image(
        python_version="python3.11",
        base_image="nvcr.io/nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04"
    )
    .add_python_packages([
        "transformers>=4.46.0",
        "torch>=2.0.0",
        "pillow",
        "accelerate",
        "sentencepiece",
        "protobuf"
    ])
)

@endpoint(
    name="translategemma-27b",
    cpu=4,
    memory="32Gi",
    gpu="H100",  # Model 27B cần GPU mạnh
    image=image,
    keep_warm_seconds=300,  # Giữ model warm 5 phút
)
def translate(**inputs):
    """
    Dịch văn bản hoặc trích xuất và dịch text từ ảnh
    
    Inputs:
    - type: "text" hoặc "image"
    - source_lang: mã ngôn ngữ nguồn (vd: "vi", "en", "cs")
    - target_lang: mã ngôn ngữ đích (vd: "en", "de-DE", "vi")
    - text: văn bản cần dịch (nếu type="text")
    - image_url: URL ảnh (nếu type="image")
    """
    from transformers import AutoModelForImageTextToText, AutoProcessor
    
    # Load model và processor (sẽ cache sau lần đầu)
    model_id = "google/translategemma-27b-it"
    processor = AutoProcessor.from_pretrained(model_id)
    model = AutoModelForImageTextToText.from_pretrained(
        model_id,
        device_map="auto",
        torch_dtype=torch.bfloat16
    )
    
    # Lấy parameters từ input
    translation_type = inputs.get("type", "text")
    source_lang = inputs.get("source_lang", "en")
    target_lang = inputs.get("target_lang", "vi")
    
    # Tạo message theo format của TranslateGemma
    if translation_type == "text":
        text = inputs.get("text", "")
        if not text:
            return {"error": "Missing 'text' parameter"}
        
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "source_lang_code": source_lang,
                        "target_lang_code": target_lang,
                        "text": text,
                    }
                ],
            }
        ]
    else:  # image
        image_url = inputs.get("image_url", "")
        if not image_url:
            return {"error": "Missing 'image_url' parameter"}
        
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source_lang_code": source_lang,
                        "target_lang_code": target_lang,
                        "url": image_url,
                    },
                ],
            }
        ]
    
    # Xử lý và generate
    inputs_processed = processor.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device, dtype=torch.bfloat16)
    
    input_len = len(inputs_processed['input_ids'][0])
    
    with torch.inference_mode():
        generation = model.generate(
            **inputs_processed,
            do_sample=False,
            max_new_tokens=inputs.get("max_tokens", 200)
        )
    
    generation = generation[0][input_len:]
    translated_text = processor.decode(generation, skip_special_tokens=True)
    
    return {
        "translated_text": translated_text,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "type": translation_type
    }
