# granite_pipeline.py
# ------------------
# This file exports `get_generator()` which returns an object with a `.generate(prompt, **kwargs)` method
# or a callable that accepts text prompts and returns a text response. Replace this placeholder with
# your exact pipeline code from Hugging Face for IBM Granite 3.3 2B Instruct.


from typing import Callable, Dict, Any


# Example minimal Hugging Face pipeline wrapper.
# *** Replace this with your provided pipeline code. ***


def get_generator():
"""Return a simple generator function that accepts prompt and returns generated text.
Replace internally with your actual Hugging Face pipeline/model initialization.
"""
try:
from transformers import pipeline
# Example model id - replace if your model ID differs.
model_id = "IBM/granite-3.3-2b-instruct"
gen = pipeline(
task="text-generation",
model=model_id,
trust_remote_code=True,
# device_map="auto" # uncomment if using GPUs and accelerate
)


def generate(prompt: str, max_new_tokens: int = 256, **kwargs) -> str:
out = gen(prompt, max_new_tokens=max_new_tokens, do_sample=True, **kwargs)
# pipeline returns a list of dicts with 'generated_text'
if isinstance(out, list) and len(out) > 0:
return out[0].get("generated_text", "")
return str(out)


return type("G", (), {"generate": staticmethod(generate)})()


except Exception as e:
# Fallback echo generator for local development/testing
class EchoGen:
@staticmethod
def generate(prompt: str, **kwargs):
return "[pipeline not available — paste your pipeline here]" + "\n\nPrompt:\n" + prompt
return EchoGen()