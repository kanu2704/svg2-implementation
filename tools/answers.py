"""What we record about one TRASER answer. No heavy imports: used by run_traser.py (Hugging Face path) and
tools/vllm_generate.py (vLLM path, in its own environment), so both record the same things."""
import json


def answer_stats(text):
    try:
        graph = json.loads(text)
        return {"json_ok": True, "out_objects": len(graph.get("objects", [])),
                "out_relationships": len(graph.get("relationships", [])),
                "out_uncertain_labels": sum("uncertain" in json.dumps(o) for o in graph.get("objects", []))}
    except json.JSONDecodeError as e:
        return {"json_ok": False, "json_error": str(e)[:200]}
