# Assignment Set #2: Building Systems with ComfyUI

This Unit will culminate in the creation of a **custom imaging system** in ComfyUI, due on Thursday, February 6.

---

## 2.1. Technical Overview of Stable Diffusion

*20 minutes, due Thursday 1/30. There is no deliverable for this exercise, but it's still important.*

* **Watch** [*How Do Diffusion Models like Midjourney and Stable Diffusion Work?*](https://www.youtube.com/watch?v=BWUApLkLH-8) (19 minutes) by Derrick Schultz, **AND/OR**
* **Read** [*Bare-Bones Diffusion Models*](https://madebyoll.in/posts/dino_diffusion/) by Ollin Boer Bohan, and **play** with his interactive demonstration [here](https://madebyoll.in/posts/dino_diffusion/demo/).


---

## 2.2. ComfyUI Ecosystem Exploration 

*40 minutes, due Thursday 1/30. A very tiny written report is required.*

* **Browse** the RunComfy [readymade workflows](https://www.runcomfy.com/comfyui/)
* **Browse** the models available [at Civitai](https://civitai.com/models) (*content warning!*)
* **Browse** the 6000+ [ComfyUI Extensions & Nodes](https://www.runcomfy.com/comfyui-nodes) available at RunComfy

**View/skim** the following resources. Make a mental note about the one(s) you think might be useful for you: 

* [Beginner's Guide to ComfyUI](https://aituts.com/comfyui/)
* [ComfyUI Shortcuts](https://blenderneko.github.io/ComfyUI-docs/Interface/Shortcuts/)
* [ComfyUI Github](https://github.com/comfyanonymous/ComfyUI/blob/master/README.md)
* [ComfyUI Examples](https://github.com/comfyanonymous/ComfyUI_examples)
* [ComfyUI Reddit](https://www.reddit.com/r/comfyui/)
* [Excellent intro page](https://www.latent.space/p/comfyui)
* [ComfyUI for Everything (other than stable diffusion)](https://www.youtube.com/watch?v=fUcDAExxndQ&t=0)

**Peek** at these ComfyUI tutorial channels: 

* [Pixaroma ComfyUI YouTube Tutorials](https://www.youtube.com/playlist?list=PL-pohOSaL8P9kLZP8tQ1K1QWdZEgwiBM0)
* [Derrick Schultz YouTube Tutorials](https://www.youtube.com/watch?v=NoB1E3nZnUk&list=PLWuCzxqIpJs8e8fET1QP96tWngqlsoIZu&index=2)
* [Purz ComfyUI YouTube Channel](https://www.youtube.com/@PurzBeats) (now on Patreon)

*Now,*

* In the Discord channel `2-2-ComfyResources`, briefly **report** on something you came across that you found intriguing: **Describe** it in a sentence or two, and, if possible, **include** a link and image. **Write** a sentence about why you found it interesting. 

---

## 2.3. Readings

### *(30 minutes, due 2/4)*

* Briefly **read** these three articles:
  1. Reading: [Will AI ever be able to write a good song?](https://www.theredhandfiles.com/considering-human-imagination-the-last-piece-of-wilderness-do-you-think-ai-will-ever-be-able-to-write-a-good-song/), by Nick Cave
  2. Reading: [The Algorithmic Gaze: Representations of Women in AI Art](https://www.lerandom.art/editorial/the-algorithmic-gaze-representations-of-women-in-ai-art), by Danielle King
  3. Reading: [Unnatural Images: On AI-Generated Photographs](https://www.journals.uchicago.edu/doi/10.1086/731729), by Amanda Wasielewski
* **Create** a post in the Discord channel, `2-3-readings`
* In your post, **write** a brief response to something that stuck with you from the reading. 

---

## 2.4. Worky Work

### *(30 minutes, due 2/4)*

Here are some helpful viewings to give you some valuable ComfyUI instruction. Please do these.

* [Upload Base Models to RunComfy](https://www.youtube.com/watch?v=dOCTwnrWi7g) (13 minute video)
* [Intro to the ComfyUI Manager](https://www.youtube.com/watch?v=4M_R1heWGWs) (9 minute video)
* [How to Add a LoRa to Your Workflow in ComfyUI](https://medium.com/@promptingpixels/how-to-add-a-lora-to-your-workflow-in-comfyui-b5635cd7a8aa) (4 minute read)

---

## 2.5. Simple Comfy Tests

In this simple exercise I ask you to do some controlled experiments with the ComfyUI default patch. 

* At RunComfy.com, **load** the default patch ("Purple Galaxy Bottle"). Change the prompt according to your preferences.
* **Experiment** with different base models. At the bare minimum I encourage you to try the difference between SD 1.5 and SDXL, but try other models that are available in RunComfy as well.
* For these experiments, **modify** the `seed` value so that it is held constant, and then: 
  * **Experiment** with different samplers
  * **Experiment** with different numbers of steps
  * **Experiment** with different denoising values
* In the Discord channel `2-4-ComfyTests`, **report** on your findings. A sentence or two is sufficient. **Provide** images showing some of your findings.


---

## 2.6. ComfyUI IPAdapter Plus Tutorial

The ComfyUI IPAdapter Plus custom node allows you to do single-image style transfer: Creating "image X in the style of image Y". In this exercise, I ask you to get the IPAdapter Plus node working, and use it to make an image that interests you. 

![ipadapter-overview.png](img/ipadapter-overview.png)

![ipadapter.png](img/ipadapter.png)

* Follow this tutorial, ["A Detailed Guide to Mastering ComfyUI IPAdapter Plus (IPAdapter V2)"](https://www.runcomfy.com/tutorials/comfyui-ipadapter-plus-deep-dive-tutorial). You can determine which parts of this tutorial are relevant to you, but I recommend especially part 6, "Style and Composition", shown above.
* **Note** that you will need to use the ComfyUI Manager to install some custom nodes, including ComfyUI IPAdapter Plus. 
* **Use** IPAdapter Plus to generate a style transfered image. 
* **Use** Ultimate Upscaler (another custom node) to upscale your result! [Here's a video about how to do that](https://www.youtube.com/watch?v=CxB47DMEyYQ)
* **Create** a post in the Discord channel `#2-6-ipadapter`
* **Upload** both your style image and your result (generated) image.
* **Write** a sentence or two about your process and/or what you learned or noticed. 

---

# MORE TBA. 

<!--

In this exercise we will use the ComfyUI Manager to install some custom nodes. Skim the following articles: 

* [A Guide to ComfyUI Custom Nodes](https://www.bentoml.com/blog/a-guide-to-comfyui-custom-nodes)
* [Recommended Custom Node Plugins for ComfyUI](https://comfyui-wiki.com/en/resource/custom-nodes) 
* [Top ComfyUI custom node packs](https://modal.com/blog/comfyui-custom-nodes)

* ComfyUI Essentials
* ComfyUI Impact Pack
* ComfyUI Inspire Pack
* ComfyUI WAS Suite
* ComfyUi IPAdapter Plus
* KJNodes for ComfyUI
* RGThree Node Pack 
* SeargeSDXL

-->












