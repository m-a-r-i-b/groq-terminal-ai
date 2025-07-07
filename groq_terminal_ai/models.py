from enum import Enum

class ModelEnum(Enum):
    LLAMA3_8B_8192 = "llama3-8b-8192"
    GEMMA2_9B_IT = "gemma2-9b-it"
    GEMMA_7B_IT = "gemma-7b-it"
    LLAMA3_70B_8192 = "llama3-70b-8192"
    LLAMA3_1_70B_VERSATILE = "llama-3.1-70b-versatile"
    LLAMA3_1_8B_INSTANT = "llama-3.1-8b-instant"
    LLAVA_V1_5_7B_4096_PREVIEW = "llava-v1.5-7b-4096-preview"
    MIXTRAL_8X7B_32768 = "mixtral-8x7b-32768"
    
    # Latest Grok models from xAI
    GROK_3_BETA = "grok-3-beta"
    GROK_3_MINI_BETA = "grok-3-mini-beta"
    GROK_3_MINI_FAST_BETA = "grok-3-mini-fast-beta"
    GROK_BETA = "grok-beta"
    GROK_VISION_BETA = "grok-vision-beta"