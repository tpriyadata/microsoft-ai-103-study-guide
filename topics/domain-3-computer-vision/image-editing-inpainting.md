# Image-Editing Workflows — Inpainting and Mask-Based Edits

**Exam skill:** Configure image-editing workflows for **inpainting and mask-based edits**.

## Core concept

**Inpainting** means **editing or replacing a selected region of an existing image** while preserving the rest of the image.

The key idea is:

> **IMAGE + MASK + PROMPT → EDITED IMAGE**

The **mask determines where the model is allowed to make changes**.

---

## 1. What is inpainting?

Suppose you have this image:

![Image](https://images.openai.com/static-rsc-4/rivutjpyxkAFpvdJ0tRHJEpikP6xUOkEZO8hgvC8QUPfRSpLqV8m9z7F8kbkWUF23f1WlmHf4STp1p-M-TFYoM3YAdkYuCR1YKBpqxl-bMlZrdz3gkYdfWG97qZvsGgToFahOm-QRhf8ydj2Lp7ghFnZ3OeU7xSzD4oOZHz_NghqOqosvip2vtaGjAZ3fpx1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ijzAffl5waDG-85O9CTWLAeBBW8XMgP6BlNtbePfA1DKM6-Tl21aK-m32FJgqtTZmHvUoPu-EmuY4xSN_JblU7TMo4QKyxz2ATLO7l2EqMn8aFSjeznXEQMbHx-RjopfazGTHU6uHCEBmLJWF31u3QYRrYJ3gXB8FlPiP7zDQhugHeqCz7srVkIL9sbG0RnA?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UTKdyga_-VPcI8YA4yWOQLzlFQLNFfXlK8VtBGxMN793ba2CdXSIHq9r_AZekjA6fQ2qf66Z1hXFmfcg48oKbXhbnhCWoL-a5ApWM1MTY-_Nobqvgbgk8L-y6JEFjd0xgLe-Gacq3Xd0Rw1wZoh3CKbAklMfMHAdWfL_mJnqAO3oX8e4mhvV_IN_abyfWjDz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/wx2NbZ1wlrEj0EltNYUd1uyftRqQ3O0MCTIt8vKqcTKaycMHQK1JODQEj7kdOjho8kzfVXVZozvNk20DG3BiI7pp41p0PULezpE8_KBdyQwgp-zppMhk9bls1ngjf2YEx8x5SbbLTnLYMTjc1uEKqxCFVw9u4L2r8ww-qCLa8dBYtp0JZ1lOJ6EFRUeWaqNN?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/02O_usupzM5hS0wy5c9iSUi10WijI9LMPkUars3yA7LVXWcsStSLQRHcNoEhzKaNq0HbcHKlD3lAUlJVp3N8IC24R9NQhUs9uovetB1xG-nM2qeik3tjDllyYAPP5CbFAn-hK6IbgAiQ3bMJiX473HZPk4uiyWXS56I6cqzLRNor0Ptu9axX3EvUpcfmY0q9?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/z5J-QUQcqR4C74sAgXrnak2q4N9HKTEeHA8ZTalWeFEJxLYNxM-zK8qf288AY-zVyIMZ39yxsIAD-qNItOZ_YJKBOEgtacJ43FB6tCbpWZA6kvv0QEEYL1RGKznuZm_yVD4OKoMMfppQsAW4ySojsU2TqGBkIKBcymV863UJV7Jm6KgKqpbtmRWWUD66jwbQ?purpose=fullsize)

You want to remove a chair from the image.

You provide:

```text
Original image
      +
    Mask
      +
"Remove the chair"
      ↓
Edited image
```

The model modifies the **masked region** and attempts to make the result blend naturally with the surrounding image.

---

# 2. What is a mask?

A **mask identifies the area that should be edited**.

Think:

> **Mask = WHERE to edit**

For example:

```text
Original image:

┌─────────────────────────┐
│                         │
│       🏠                │
│             🚗          │
│                         │
└─────────────────────────┘

Mask:

┌─────────────────────────┐
│                         │
│                         │
│             ███         │
│             ███         │
└─────────────────────────┘

Prompt:
"Replace the car with a bicycle."
```

The model focuses the edit on the masked area.

---

# 3. Inpainting vs. outpainting

This distinction is useful for the exam.

### Inpainting

**Modify an existing region inside the image.**

Example:

> Remove a person from the background.

→ **Inpainting**

### Outpainting

**Extend the image beyond its original boundaries.**

Example:

> Extend this landscape to create a wider image.

→ **Outpainting**

### Memory trick

> **IN = edit INSIDE**
> **OUT = expand OUTSIDE**

---

# 4. Typical image-editing workflow

A mask-based editing workflow looks like:

```text
Original Image
      ↓
Create / provide mask
      ↓
Define editing prompt
      ↓
Image generation/editing model
      ↓
Validate result
      ↓
Edited Image
```

### Example

**Original:**
A living room with an old sofa.

**Mask:**
Select only the sofa.

**Prompt:**

> "Replace the sofa with a modern gray sectional."

**Result:**
The sofa is changed while the surrounding room remains substantially unchanged.

---

# 5. When should you use inpainting?

Use inpainting when the requirement is to:

* Remove an object
* Replace an object
* Modify part of an image
* Change clothing
* Change a background region
* Repair damaged areas
* Add an object to a specific location
* Modify a selected portion while preserving the rest

### Exam clue

If you see:

> **"Modify only a selected portion of an existing image."**

Think:

### **Inpainting + mask**

---

# 6. Mask precision matters

The quality of the mask affects the result.

### Tight mask

Selects only the target object.

Useful when:

> You want minimal changes to surrounding content.

### Larger mask

Includes surrounding pixels.

Useful when:

> The replacement needs more room to blend naturally.

The important principle:

> **The mask controls the editing region; the prompt describes what should happen there.**

---

# 7. Mask vs. prompt

Don't confuse their responsibilities.

| Component  | Responsibility                 |
| ---------- | ------------------------------ |
| **Image**  | Starting visual content        |
| **Mask**   | Where the edit occurs          |
| **Prompt** | What the edit should be        |
| **Model**  | Generates the modified content |

### Memory trick

## **"WHERE + WHAT"**

**Mask = WHERE**

**Prompt = WHAT**

---

# 8. Common exam scenarios

### Scenario 1

> A user wants to remove a person from an existing photograph without changing the rest of the image.

**Answer: Inpainting with a mask**

---

### Scenario 2

> A user wants to replace the red car in an image with a blue electric vehicle.

**Answer: Mask the car + provide an editing prompt**

---

### Scenario 3

> A user wants to make an image wider by generating content beyond the original edges.

**Answer: Outpainting**

---

### Scenario 4

> A user wants to change the entire image from daytime to nighttime.

This is **not necessarily a mask-based inpainting problem** because the requested change affects the overall image.

Think about the appropriate **image transformation/generation workflow** instead.

---

# Exam decision framework

Ask these questions:

### **1. Do I already have an image?**

If no → image generation may be appropriate.

If yes → continue.

### **2. Do I only want to modify part of it?**

Yes → **Inpainting**

### **3. Do I need to identify the exact region?**

Yes → **Mask**

### **4. What should happen to that region?**

Describe it in the **prompt**.

### **5. Do I want to extend beyond the image boundaries?**

Yes → **Outpainting**

---

# Memory trick

## **"IMAGE → MASK → PROMPT → EDIT"**

**IMAGE** = starting point

**MASK** = where

**PROMPT** = what

**EDIT** = generated result

And the most important exam association:

> **Selected region + existing image = Inpainting**

> **Mask = controls the area being edited**

> **Expansion beyond image boundary = Outpainting**
