# Image/Video Generation from Prompts or Reference Media

**Exam skill:** Build solutions that generate images and videos via **text prompts or reference media**.

## Core concept

For AI-103, understand the difference between:

> **Generate from instructions** vs. **generate/transform using existing media**

The basic pattern is:

**Prompt + optional reference media → Generative model → Image/Video**

---

# 1. Text-to-image

**Text-to-image** generates a new image from a natural-language prompt.

Example:

> "A modern AI laboratory with glass walls, cinematic lighting, photorealistic."

```text id="z4zv5x"
Text prompt
    ↓
Image generation model
    ↓
Generated image
```

### Use when

You don't have an existing image that needs to be preserved.

Examples:

* Marketing images
* Product concepts
* Architectural concepts
* Illustrations
* Creative designs
* Synthetic training data

### Exam clue

> **"Create an image based only on a textual description."**

→ **Text-to-image generation**

---

# 2. Text-to-video

Text-to-video generates a video based on a natural-language description.

Example:

> "A drone flying over a modern city at sunset, cinematic camera movement."

```text id="p5tq0s"
Text prompt
    ↓
Video generation model
    ↓
Generated video
```

### Use when

The desired video is described primarily through text.

Examples:

* Marketing videos
* Concept videos
* Educational content
* Storyboards/prototypes
* Creative video generation

---

# 3. Image-to-image / reference-image generation

A **reference image** can guide the generation process.

Instead of:

> "Generate a modern living room."

You can provide an existing room image and request:

> "Redesign this room in a modern minimalist style while maintaining the room's layout."

```text id="a6s4qe"
Reference image
       +
     Prompt
       ↓
Generative model
       ↓
New image
```

The reference provides **visual context**, while the prompt describes the desired transformation.

---

# 4. Reference media

Reference media can help maintain characteristics such as:

* Composition
* Subject appearance
* Style
* Layout
* Visual identity
* Objects
* Scene characteristics

### Exam clue

If the question says:

> **"Use an existing image as guidance for generating a new image."**

Think:

### **Reference-image generation**

---

# 5. Image-to-video

You can use an existing image as the starting point for video generation.

Example:

**Input:**

A still image of a car.

**Prompt:**

> "Camera slowly moves around the car while the headlights turn on."

```text id="x4w2nk"
Reference image
       +
     Prompt
       ↓
Video generation model
       ↓
Animated video
```

The image establishes the **initial visual state**, while the prompt describes the desired **motion/action**.

### Exam clue

> **"Animate an existing image."**

→ Think **image-to-video**.

---

# 6. Text-to-image vs. image editing

This is a very important distinction.

### Text-to-image

You want to **create a new image**.

> "Create a futuristic office."

→ Text-to-image

### Image editing / inpainting

You already have an image and want to **modify a specific region**.

> "Remove the chair from this image."

→ Inpainting + mask

### Reference-image generation

You want to **use an existing image as visual guidance** for generating another image.

> "Use this room as a reference and redesign it."

→ Reference-image generation

---

# 7. Image generation vs. video generation

| Requirement                                     | Approach                       |
| ----------------------------------------------- | ------------------------------ |
| Create image from description                   | **Text-to-image**              |
| Create video from description                   | **Text-to-video**              |
| Generate image using existing image as guidance | **Reference-image generation** |
| Animate an existing image                       | **Image-to-video**             |
| Modify selected region                          | **Inpainting**                 |
| Extend image beyond its boundaries              | **Outpainting**                |

---

# 8. Prompt design for generation

A strong generation prompt can specify:

### Subject

**What should appear?**

> "A modern electric vehicle"

### Environment

**Where is it?**

> "parked outside a glass office building"

### Style

**How should it look?**

> "photorealistic, cinematic"

### Composition

**How should it be framed?**

> "wide-angle shot, low camera angle"

### Lighting

> "golden-hour lighting"

### Motion — for video

> "slow camera pan from left to right"

Think:

> **SUBJECT + ENVIRONMENT + STYLE + COMPOSITION + MOTION**

---

# 9. Reference media + prompt

When using reference media, remember:

> **Reference = visual guidance**
> **Prompt = desired outcome**

For example:

```text id="t7y3hs"
Reference image
  ↓
"Keep the same building structure,
but redesign the exterior using
modern glass and wood."
  ↓
Generated image
```

The reference image provides the starting visual context.

The prompt specifies the transformation.

---

# 10. Common exam scenarios

### Scenario 1

> A marketing team wants to create a completely new product image from a written description.

**Answer: Text-to-image**

---

### Scenario 2

> A designer provides an existing product photograph and wants the model to create variations while maintaining the product's visual characteristics.

**Answer: Reference-image generation**

---

### Scenario 3

> A company wants to turn a still photograph into a short animated video.

**Answer: Image-to-video**

---

### Scenario 4

> A developer wants to create a short video entirely from a natural-language description.

**Answer: Text-to-video**

---

### Scenario 5

> A user wants to remove one object from an existing photograph while preserving the surrounding image.

**Answer: Inpainting with a mask**

---

# Exam decision framework

Ask:

### **1. Am I starting with text only?**

→ Text-to-image or text-to-video.

### **2. Do I have reference media?**

→ Use a reference-media workflow.

### **3. Is the reference an image that should become animated?**

→ Image-to-video.

### **4. Am I modifying only a specific region?**

→ Inpainting + mask.

### **5. Am I extending the image beyond its current boundaries?**

→ Outpainting.

---

# Memory trick

## **"TEXT → CREATE | IMAGE → GUIDE | MASK → EDIT | VIDEO → MOTION"**

**TEXT → CREATE**
Text-to-image/video

**IMAGE → GUIDE**
Reference media

**MASK → EDIT**
Inpainting

**VIDEO → MOTION**
Image-to-video / text-to-video

### One-line exam rule

> **Use text prompts to describe what to generate, reference media to provide visual guidance, masks for localized edits, and image/video generation capabilities according to whether the desired output is a static image or moving video.**
