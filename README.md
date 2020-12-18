# IDD_HologramProject

## Proposal (11/15/20)

IDD Final Project - Desktop Hologram

This is the repo for my final IDD project. I'm away from home currently, but I'll post photos of parts and progress in the next few days. 

This project is to construct a desktop hologram using the Pepper's Ghost optical illusion. The device will use a RaspberryPi connected to a 7.0" TFT display to display an image, which will be reflected by a thin plastic reflector screen (angled at 45 degrees) to make the image appear is if it is floating behind the reflector. The device will have a voice recognition intercom to control key functions, and a stretch goal is to integrate a camera to track the viewer's face and change the displayed image according to their viewing angle. This stretch goal would improve the quality of the illusion significantly. 

I have already ordered all the parts (except the face tracking camera), and the links are below:

[Mic](https://www.bhphotovideo.com/c/product/753984-REG/CAD_U9_U9_USB_Omnidirectional_Microphone.html/?ap=y&ap=y&smp=y&smp=y&lsft=BI%3A514&gclid=Cj0KCQjwit_8BRCoARIsAIx3Rj5i8v2IneaH23_L43NfhiuR1F_kObbOOEiD-pONl-GnGrsYWOwVGwYaApNEEALw_wcB)

[Screen](https://www.adafruit.com/product/2353)

[RPi TFT Conversion Kippah](https://www.adafruit.com/product/2454)

[Reflector screen material](https://www.andymark.com/products/polycarbonate-sheet-0-06-in-thick-24-in-x24-in-clear)


## Functional Checkoff (12/3/20)

I have the hologram display working, as seen in the demo video [here](https://youtu.be/VnmK-LyLPDo).

I'm still working with the Adafruit forums to fix the TFT screen installation, forum post [here](https://forums.adafruit.com/viewtopic.php?f=47&t=171740).

Functional code for voice recognition and asset switching is ready, still making updates for the final version locally on my Pi. 


# Final Version (12/18/20, for now)

The semester is over, and I've finished most of my original goals for this project, but a couple are still outstanding for future work. I describe my progress for this final deliverable below. 

## Completion Checklist:

Done:
- Pepper's Ghost optical illusion projector, powered by 7" TFT display with breakout board driver
- UI/UX 3D printed enclosure, with clean ports for brightness dial, button, mic, and cords
- Natively printed enclosure hinge mechanism to allow for easy maintenance and viewing angle adjustment
- Backlight dimming control design
- Button press recognition system
- High quality microphone integration for voice recognition

Not Done:
- Integrate voice command recogntion into larger app to control what is on the display
- Actually display graphics with brightness dimmer functionality plugged in (need to hook up separate voltage supply for this)
- Integrate facial recognition with enclosed camera, and change displayed object viewing angle accordingly (stretch goal)

## The Illusion and the Device

<p float="left">
  <img src="/images/frontView.jpg" width="100" />
  <img src="/images/backView.jpg" width="100" />
</p>

The photos above show the device in its final form, and also illustrate that much of the functionality is achieved by attaching an external display to the Pi and holding it in a very specific position relative to a pane of partially reflective plastic. The illusion that creates the hologram effect can be seen below:

<img src="/images/peppers.jpg" width="100" />

Essentially, the clear plastic reflector tricks the human eye into thinking that there is a floating object made of light behind the reflector when you see only the target image and not the actual surface of the reflector. Since your brain doesn't perceive a solid object (the reflector) in the intervening space, it assumes that the object must exist floating in space. This technique is called the Pepper's Ghost illusion, and was invented in the 1800s and named after the clever stage director who thought of it. 

When an image with a black background is displayed on the screen, the illusion goes into effect, as shown in the sample image below. As you may be able to tell, there are some significant visual artifacts from the screen that decrease the quality of the illusion. The primary drawback of creating a hologram using an optical illusion is that the appearance of the system as a convincing hologram relies on the optical illusion remaining perfect, which is difficult to achieve consistently and is highly depended on light conditions in the surrounding environment. There is significant future work to be done on reducing visual artifacts to improve how convincing the illusion is. 

## Physical Design

The physical enclosure for the system is the most complete and successful part of this project. I designed and printed 6 different 3D printed parts that, when glued and slotted together, make a fully enclosed and adjustable system, including ports for the various wires, user controls, and gadgets that make up the system circuitry. 

### The Base

<img src="/images/baseCAD.jpg" width="100" />

The base and electronics enclosure is made of two primary clamshell parts, attached by a custom hinge geometry and secured by a 3D printed dowel. The CAD of these parts can be seen above. Key features include a window for the screen to be glued into, held at a 30 degree angle relative to the ground (this angle number is important later), holes for the mic, activation button, and brightness dial, and outlet holes for the power cables. The bottom part is 0.75" deep and is basically a tray for all the electronics, and the top part is a triangular prism used for setting the screen angle. Importantly, since the top part easily hinges up and can be propped in place, this system allows the user to easily change the up/down optimal viewing angle for the hologram, which would otherwise be very narrow. 

### The Reflector

<img src="/images/reflectorCAD.jpg" width="100" />

The reflector interface pieces are just a way to securely hold the reflector at the right angle to make the illusion appear in the correct place and angle. Since the base holds the screen at 30 degrees relative to the ground, the reflector's angle relative to the screen needs to be 30 degrees as well such that when the image is reflected over the plane of the panel, it appears to the viewer's eye as a perfectly vertical image. The large wings of the printed parts also serve to keep the reflector stiff and flat so that the resultant image is not stretched or distorted.

## What's Inside?

<img src="/images/interiorPic.jpg" width="100" />

The main driver of the system is the Raspberry Pi used in the other course projects. This is the brain of the system, and interfaces with three other major components that handle sub-tasks. 

### Adafruit HDMI Decoder

<img src="/images/decoderPic.jpg" width="100" />

This Adafruit board is a deceptively complex breakout board that converts the HDMI output of the Pi and formats it for the display's 40-pin input format. It also does the power and digital driving for the display in general, a task that turns out to be far more complex than the Adafruit tutorial for the part would make it seem. Particularly on the power end, this conversion was actually the bulk of the work for this project and took wayyy longer than I thought it would. 

I actually started with an entirely different Adafruit converter board, as mentioned above in my proposal. This part did not work at all, and would always cause the display to show only a white rectangle over the whole area. That part was intended to be an elegant shortcut for the video output task, but to bypass it I switched to the full decoder breakout because it has more exposed and debug-able functionality. Even with this new board, it took me several days of work and talking with David to figure out that the screen going all-white was because it wasn't getting enough power. Turns out that this display is extremely power-hungry, and to work at all needs to be plugged directly into a wall outlet. Adafruit also claims that you can easily dim the display by feeding it PWM into its "Backlight" pin, but I've found that that description is deceptive at best, and actually to dim the screen without it going all-white, one needs to feed the board a very high power supply, regulated by a PWM waveform via transistor. My dimmer functionality that just seeks to regulate the screen with Arduino PWM doesn't work because the Arduino can't supply nearly enough current to power the screen from its PWM pins.

All that said, the final version works for at least 20 minutes before eventually (still) whiting out when plugged into the wall at full brightness via micro-USB. This is functional for now, but the first future work I will tackle will be putting a dedicated power supply into the enclosure and powering the screen with it, regulated by my functional dimmer PWM setup. 

### Arduino

<img src="/images/backView.jpg" width="100" />

My Arduino is included in the enclosure, still on its breadboard, and it handles all the analog electronics connections. The dimmer dial is wired up to pins 6 and 7, exactly as in Lab 2, and the PWM signal is generated from pin 9. The activation button is hooked up with a pulldown resistor to analog pin A5, and to do the power supply future work I'll just insert a transistor into the power supply loop on this same breadboard. The Arduino is running "hologram.ino", included in this repo. All of the functionality is just taking bits of various labs, changing their outputs, and weaving them together into one file, so I won't go too much into the technical details of that work here. 

### CAD Audio Mic

<img src="/images/mic.jpg" width="100" />

As mentioned in the proposal, I ordered a high quality mic to improve the functionality of the Lab 6 speech recognition code, and this mic works great plug and play. I implemented a really clean UI for this part where it just sticks out of a hole in the casing, and since it's connected to the Pi via USB, this also holds the Pi in place. Not much to discuss here, the speech recognition for now works with the activation button exactly as it did in Lab 6. Future work will involve writing a central hub for the hologram to take in the speech recognition output and display video accordingly. I didn't get to this task, but will likely work with Ilan's suggestion to use a Kiosk mode browser window. 

## Demo Videos

Demo videos of the system can be found [here](https://youtu.be/VnmK-LyLPDo), [here](https://youtu.be/VnmK-LyLPDo), and [here](https://youtu.be/VnmK-LyLPDo). Let me know if there's anything that's unclear, happy to add more description of various subsystems. 
