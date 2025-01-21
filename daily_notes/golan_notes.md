# Misc. Golan Notes

---


### Gohai's p5-to-Comfy realtime toolchain:

* This toolchain by Gottfried Haider (Gohai) uses the Comfy API (with Dev Mode) to process images that are transmitted via WebSockets: [https://github.com/gohai/p5.comfyui-helper](https://github.com/gohai/p5.comfyui-helper)
* Gohai's Inpainting [p5 sketch](https://editor.p5js.org/gohai/sketches/x_nkT_dBx) & [duplicate](https://editor.p5js.org/golan/sketches/d8KmJ3t2A)
* According to Gohai, we'll need the following: 
  * Enable *Dev Mode* (get to Settings using small cog in ComfyUI remote control panel)
  * Install `comfyui-tooling-nodes`. Note: It MAY be possible to use [https://github.com/LyazS/comfyui-nettools](https://github.com/LyazS/comfyui-nettools) instead of `comfyui-tooling-nodes`.
  * To access ComfyUI remotely: `--listen 0.0.0.0 --enable-cors-header`
  * Load a provisioned certificate into ComfyUI with `--tls-keyfile privkey.pem --tls-certfile fullchain.pem`

**Henlee** from RunComfy writes: 

* Aside from loading the cert, I think you hould be able to finish the first three steps, there are two API that you mentioned, RunComfy API as you mentioned is for machine launching/stopping, ComfyUI API is for queue prompt. 
* Where to get the ComfyUI server url so you can access ComfyUI remotely, [https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/how-to-call-the-comfyui-api-on-a-runcomfy-machine](https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/how-to-call-the-comfyui-api-on-a-runcomfy-machine)
* How to interact with ComfyUI API, [https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/working-with-comfyui-backend-api](https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/working-with-comfyui-backend-api)
* please see this part of code and this is how we implement the custom node for RunComfy: [https://github.com/InceptionsAI/ComfyUI-RunComfy-Helper/blob/main/helpers/workflow.py](https://github.com/InceptionsAI/ComfyUI-RunComfy-Helper/blob/main/helpers/workflow.py)

Installing `comfyui-tooling-nodes`:

* ComfyUI Manager, Install via Git:
* https://github.com/Acly/comfyui-tooling-nodes.git
* "This action is not allowed with this security level configuration."
* Advice here: https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/how-to-fix-this-action-is-not-allowed-with-this-security-level-configuration
* Inside the Assets file browser, go to ComfyUI > custom_nodes > ComfyUI-Manager and find the config.ini file.
* Double-click on the config.ini. This will open the file in a simple text editor. Now you can config the manager.
* Change security_level to weak at the bottom of the file.
* Click the floppy disk icon in upper right to save the change. Close that editor.
* Once you finish editing config.ini, you need to restart the ComfyUI by clicking the top left Restart Comfy button (NOT restart the machine!). This should take a few seconds.
* For good measure, refresh the browser page.
* Click, Add Node, "External Tooling", Load Image b64...

Working with ComfyUI Backend API:

[https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/working-with-comfyui-backend-api](https://comfyui-guides.runcomfy.com/ultimate-comfyui-how-tos-a-runcomfy-guide/working-with-comfyui-backend-api)

From henlee from RunComfy: 
```
import websocket
import uuid

ws = websocket.WebSocket()
ws.connect("ws://{}/ws?clientId={}".format('yyyyyyy-yyyy-yyyy-yyyyyyyyyyyy-comfyui.runcomfy.com', client_id))
while True:
    out = ws.recv()
    print(out)
```