# NIM probe for stages 5–6

81 models available to this key (full list: `nim_models.txt`).

## Stage 5: paragraph → JSON (their prompt, DAM's real paragraphs)

id 1 = the boy; id 0 = the floor, which DAM described as a person (P44).

### lightning-30b thinking ON (NVIDIA's example settings), object 1

FAILED: plain text: no JSON in reply: "Here's a thinking process:\n\n1.  **Analyze User Request:**\n   - User wants me to act as an information-extraction engine for visual scene understanding.\n   - Input: A short paragraph describing a video"

### lightning-30b thinking ON (NVIDIA's example settings), object 0

FAILED: plain text: no JSON in reply: '{\n  "object": "A young person",\n  "attributes": ["green shirt", "dark pants", "bright green shoes", "person"]  \n   - Actually, the paragraph describes "a young person". The main object is clearly a pe'

### lightning-30b thinking OFF, temp 0.6, object 1

OK via **strict json_schema** in 5.6 s

```json
{
 "Object": "person",
 "Attributes": [
  "bright green",
  "red trim",
  "dark blue",
  "light blue stripes",
  "vest",
  "pants",
  "side profile",
  "bent forward",
  "arms extended",
  "crouched position",
  "legs bent",
  "airborne",
  "legs bent",
  "arms reaching upwards",
  "landing",
  "poised stance",
  "fluid and expressive movements",
  "youthful exuberance",
  "agility"
 ],
 "Relationships": [
  "on top of ground",
  "next to environment",
  "facing forward during movement",
  "part of dynamic sequence"
 ],
 "Actions": [
  "shifting weight",
  "bending forward",
  "extending arms",
  "crouching",
  "jumping",
  "landing",
  "maintaining stance"
 ]
}
```

### lightning-30b thinking OFF, temp 0.6, object 0

OK via **strict json_schema** in 1.8 s

```json
{
 "Object": "person",
 "Attributes": [
  "young",
  "vibrant green shirt",
  "dark pants",
  "bright green shoes",
  "dynamic posture",
  "slight blur of limbs",
  "bent arms at elbows",
  "slightly tilted head"
 ],
 "Relationships": [
  "in motion",
  "playful activity"
 ],
 "Actions": [
  "jumping",
  "performing a playful maneuver"
 ]
}
```

### nemotron-3-super-120b, object 1

OK via **strict json_schema** in 10.7 s; reasoning 5508 chars

```json
{
 "Object": "person",
 "Attributes": [
  "bright green",
  "red",
  "dark blue",
  "light blue",
  "trimmed",
  "striped"
 ],
 "Relationships": [
  "side profile"
 ],
 "Actions": [
  "shifting weight",
  "bending forward",
  "extending arms",
  "crouching",
  "jumping",
  "flipping",
  "landing"
 ]
}
```

### nemotron-3-super-120b, object 0

OK via **strict json_schema** in 9.6 s; reasoning 6994 chars

```json
{
 "Object": "person",
 "Attributes": [
  "vibrant green shirt",
  "dark pants",
  "bright green shoes",
  "bent elbows",
  "tilted head"
 ],
 "Relationships": [
  "wearing a vibrant green shirt",
  "wearing dark pants",
  "wearing bright green shoes"
 ],
 "Actions": [
  "engaging in a playful activity",
  "moving",
  "maintaining a lively demeanor"
 ]
}
```

### nemotron-3-ultra-550b, object 1

OK via **strict json_schema** in 17.2 s; reasoning 5767 chars

```json
{
 "Object": "person",
 "Attributes": [
  "young",
  "wearing bright green vest with red trim",
  "wearing dark blue pants with light blue stripes"
 ],
 "Relationships": [
  "in side profile relative to camera",
  "airborne (not in contact with ground)",
  "standing on feet"
 ],
 "Actions": [
  "shifting weight",
  "bending forward",
  "extending arms",
  "crouching",
  "jumping",
  "flipping",
  "landing"
 ]
}
```

### nemotron-3-ultra-550b, object 0

OK via **strict json_schema** in 22.1 s; reasoning 6276 chars

```json
{
 "Object": "person",
 "Attributes": [
  "vibrant green shirt",
  "dark pants",
  "bright green shoes",
  "dynamic posture",
  "blurred limbs",
  "bent arms",
  "tilted head"
 ],
 "Relationships": [],
 "Actions": [
  "jumping",
  "moving",
  "performing playful maneuver"
 ]
}
```

### kimi-k3, object 1

OK via **strict json_schema** in 17.6 s; reasoning 1227 chars

```json
{
 "Object": "person",
 "Attributes": [
  "young",
  "bright green",
  "red-trimmed",
  "dark blue",
  "light-blue-striped"
 ],
 "Relationships": [
  "side profile to camera",
  "reaching toward something in front"
 ],
 "Actions": [
  "shifting weight",
  "bending forward",
  "extending arms",
  "crouching",
  "jumping",
  "performing flip",
  "reaching upwards",
  "landing"
 ]
}
```

### kimi-k3, object 0

OK via **strict json_schema** in 11.3 s; reasoning 1486 chars

```json
{
 "Object": "person",
 "Attributes": [
  "young",
  "vibrant green shirt",
  "dark pants",
  "bright green shoes",
  "slightly tilted head",
  "bent elbows"
 ],
 "Relationships": [
  "wearing vibrant green shirt",
  "wearing dark pants",
  "wearing bright green shoes"
 ],
 "Actions": [
  "moving",
  "possibly jumping",
  "performing playful maneuver"
 ]
}
```

## Stage 6 feasibility: can the model read 5 frames in one request?

Frames [0, 24, 48, 72, 96] of sav_000001 (336 px wide JPEG). Question: how many images, plus one sentence each.

### `meta/llama-3.2-90b-vision-instruct`, 1 image(s): 11.3 s

```
N = 1

The image depicts a person in a green vest and blue pants, with their arms outstretched, standing on a trampoline.
```

### `meta/llama-3.2-90b-vision-instruct`, 5 image(s): FAILED

`BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request. You can set `--limit-mm-per-prompt` to increase this limit if the model supports it.', 'type': 'BadRequestError', 'param': None, 'code': 400}`

### `google/gemma-4-31b-it`, 1 image(s): 10.3 s

```
N = 1
A young boy in a teal vest and blue pants is jumping on a trampoline in an indoor park.
```

### `google/gemma-4-31b-it`, 5 image(s): FAILED

`BadRequestError: Error code: 400 - {'message': 'At most 4 image(s) may be provided in one prompt. (parameter=image)', 'type': 'Bad Request', 'code': 400}`

### `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`, 1 image(s): 2.8 s

```
N = 1
A boy in a green vest and blue outfit is jumping on a trampoline in an indoor play area.
```

### `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`, 5 image(s): 20.9 s

```
N = 5
A boy in a green vest crouches on a trampoline in an indoor park.
The boy stands up on the trampoline surface.
The boy looks down at a red cross painted on the trampoline mat.
The boy falls backward onto the trampoline mat with his legs in the air.
The boy sits up on the trampoline mat after falling.
```

### `moonshotai/kimi-k3`, 1 image(s): 6.7 s

```
N = 1  
A child in a green vest runs across an indoor trampoline park while others play near a foam pit in the background.
```

### `moonshotai/kimi-k3`, 5 image(s): 9.1 s

```
N = 5
A boy in a green vest walks across an indoor trampoline park.
He continues moving toward a red X marker on the trampoline surface.
He steps near the red X while others jump in the background.
He loses balance and falls backward onto the trampoline.
He ends up sitting on the trampoline near the red marker.
```

### `google/gemma-3-12b-it`, 1 image(s): FAILED

`NotFoundError: Error code: 404 - {'status': 404, 'title': 'Not Found', 'detail': "Function 'ee47df99-c92b-4dc9-b3a7-f3fb0f087b73': Not found for account 'k4B_L3UFd2X6zdo42eP9Sw__1h3ZhKpX-enAIjgZKzc'"}`

### `google/gemma-3-12b-it`, 5 image(s): FAILED

`NotFoundError: Error code: 404 - {'status': 404, 'title': 'Not Found', 'detail': "Function 'ee47df99-c92b-4dc9-b3a7-f3fb0f087b73': Not found for account 'k4B_L3UFd2X6zdo42eP9Sw__1h3ZhKpX-enAIjgZKzc'"}`

### `microsoft/phi-3-vision-128k-instruct`, 1 image(s): FAILED

`NotFoundError: Error code: 404 - {'status': 404, 'title': 'Not Found', 'detail': "Function '20f2537e-8593-4eb9-ad40-60eee3bbaa55': Not found for account 'k4B_L3UFd2X6zdo42eP9Sw__1h3ZhKpX-enAIjgZKzc'"}`

### `microsoft/phi-3-vision-128k-instruct`, 5 image(s): FAILED

`NotFoundError: Error code: 404 - {'status': 404, 'title': 'Not Found', 'detail': "Function '20f2537e-8593-4eb9-ad40-60eee3bbaa55': Not found for account 'k4B_L3UFd2X6zdo42eP9Sw__1h3ZhKpX-enAIjgZKzc'"}`

