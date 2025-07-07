from enum import Enum

class ModelEnum(Enum):
    # Updated Llama models (replacing deprecated ones)
    LLAMA3_3_70B_VERSATILE = "llama-3.3-70b-versatile"
    LLAMA3_1_8B_INSTANT = "llama-3.1-8b-instant"
    
    # Latest Llama 4 models (excellent for reasoning and code generation)
    LLAMA4_SCOUT = "meta-llama/llama-4-scout-17b-16e-instruct"
    LLAMA4_MAVERICK = "meta-llama/llama-4-maverick-17b-128e-instruct"
    
    # Current Gemma model (7B deprecated, using 9B)
    GEMMA2_9B_IT = "gemma2-9b-it"
    
    # DeepSeek reasoning models (great for complex problem solving)
    DEEPSEEK_R1_DISTILL_LLAMA_70B = "deepseek-r1-distill-llama-70b"
    DEEPSEEK_R1_DISTILL_QWEN_32B = "deepseek-r1-distill-qwen-32b"
    
    # Qwen models (excellent for coding and instruction following)
    QWEN_2_5_32B = "qwen-2.5-32b"
    QWEN_QWQ_32B = "qwen-qwq-32b"
    
    # Updated Mistral model
    MISTRAL_SABA_24B = "mistral-saba-24b"
    
    # Keep legacy models for backward compatibility until they're fully deprecated
    LLAMA3_70B_8192 = "llama3-70b-8192"  # Deprecated Aug 30, 2025
    LLAMA3_8B_8192 = "llama3-8b-8192"    # Deprecated Aug 30, 2025