# Goblin for Unity: User Guide

This guide walks you through using the Goblin in Unity, from opening the demo scenes to building your own goblin camp with randomized looks and ragdoll deaths.

> [!info] Image placeholders
> Every image in this guide is a placeholder. The line under each one describes the screenshot to capture. Save the screenshots in an `images/` folder beside this file, using the file names shown.

---

## Contents

1. [Requirements](#1-requirements)
2. [What's in the pack](#2-whats-in-the-pack)
3. [Quick start: the demo scenes](#3-quick-start-the-demo-scenes)
4. [Placing a goblin in your scene](#4-placing-a-goblin-in-your-scene)
5. [Animations](#5-animations)
6. [Ragdoll deaths](#6-ragdoll-deaths)
7. [The playable demo goblin (third person)](#7-the-playable-demo-goblin-third-person)
8. [Materials and warpaint](#8-materials-and-warpaint)
9. [The character creator](#9-the-character-creator)
10. [The customization menu](#10-the-customization-menu)
11. [Random goblins and the Limits file](#11-random-goblins-and-the-limits-file)
12. [Saving goblins between sessions](#12-saving-goblins-between-sessions)
13. [Using the goblin from code](#13-using-the-goblin-from-code)
14. [Troubleshooting](#14-troubleshooting)

---

## 1. Requirements

| Requirement     | Details                                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| Unity           | Unity 6 (6000.0 LTS or newer)                                                                                     |
| Render pipeline | URP or HDRP with Shader Graph                                                                                     |
| TextMeshPro     | Required for the Character Creator menu, Built into Unity.<br>Import **TMP Essential Resources** once (see below) |
| Input           | Works with the Input System package or the old Input Manager. Nothing extra to install                            |

Nothing else needs to be downloaded. The ragdolls use Unity's built-in physics, and the demo's third-person controller uses Unity's built-in Character Controller, so no Cinemachine or other packages are needed.

### Import TMP Essential Resources

The customization menu uses TextMeshPro text. The first time you open a scene with the menu, Unity may ask you to import TMP Essential Resources. Click **Import**.

To do it yourself: **Window > TextMeshPro > Import TMP Essential Resources**.

![TMP Importer window](images/tmp-import.jpg)

---

## 2. What's in the pack

Everything lives under `Assets/EtherionDesigns/Goblin/`.

```
EtherionDesigns/
└─ Goblin/
   ├─ Animations/        Goblin animation clips (FBX)
   ├─ Characters/        Goblin meshes, prefabs (plain and ragdoll) and the AC_Goblin controller
   ├─ Data/              Limits file and Archetype Set for the character creator
   ├─ Demo/              Optional. Delete it if you don't need the examples
   │  ├─ Animations/     AC_Goblin_ThirdPerson controller for the playable demo goblin
   │  ├─ Prefabs/        PF_Demo_GoblinPlayer (playable goblin with its camera)
   │  ├─ Scenes/         Demo, ThirdPerson and WeaponsPreview scenes
   │  ├─ Scripts/        Third-person movement and camera, ragdoll keys, fly camera, level keys
   │  └─ Textures/       Studio cubemap for the demo reflections
   ├─ Documentation/     Tech specs and guides
   ├─ Materials/         Skin, clothes, teeth and eye materials, plus skin and eye variations
   ├─ Scripts/
   │  ├─ Runtime/        Character creator and Ragdoll
   │  └─ Editor/         Inspectors and Tools menu items
   ├─ Shaders/           Shader Graphs for the skin and eyes, warpaint function
   ├─ Textures/          All textures
   ├─ UI/                Customization menu prefabs
   └─ Weapons/           Stone age weapon meshes, materials and prefabs
```

![Project window showing the pack folders](images/project-folders.png)
> 📷 **Image:** The Project window with `EtherionDesigns/Goblin` expanded, showing all subfolders.

### The goblin prefabs

All of them are in `Goblin/Characters/`:

| Prefab | Description |
|---|---|
| `PF_Goblin` | <!-- TODO: describe outfit --> |
| `PF_Goblin_Basic` | <!-- TODO: describe outfit --> |
| `PF_Goblin_Naked` | <!-- TODO: describe outfit --> |
| `PF_Goblin_Ragdoll`, `PF_Goblin_Basic_Ragdoll`, `PF_Goblin_Naked_Ragdoll` | The same three goblins with a ragdoll ready for death. See [Ragdoll deaths](#6-ragdoll-deaths) |

The plain prefabs have no physics, movement or camera on them, so they work with any controller or AI system you already use. Use the ragdoll versions if you want the goblin to collapse when it dies.

![The three goblin variants side by side](images/goblin-variants.png)
> 📷 **Image:** All three goblins standing side by side in a neutral scene, labelled with their prefab names.

> [!tip]
> Always use the `PF_` prefabs, not the `SKM_` FBX files. The prefabs already have the Animator, avatar, controller and LODs set up.

---

## 3. Quick start: the demo scenes

### Demo scene (character creator)

1. Open `Goblin/Demo/Scenes/Demo.unity`.
2. Press **Play**.
3. Every goblin gets a random look. The customization menu opens on the left.
4. Drag the sliders to reshape the goblin. Drag with the **left mouse button** to orbit the camera, drag with the **middle mouse button** to move it up, down, left and right, and scroll to zoom.
5. Press **M** to close or open the menu.

![Demo scene in Play mode with the menu open](images/demo-scene-play.png)
> 📷 **Image:** The Game view in Play mode, showing the customization menu on the left and a goblin in the centre.

### ThirdPerson scene (playable goblin)

1. Open `Goblin/Demo/Scenes/ThirdPerson.unity`.
2. Press **Play**.
3. Controls:

| Action | Keyboard and mouse | Gamepad |
|---|---|---|
| Move | W A S D or arrow keys | Left stick |
| Run | Hold Left Shift | Click left stick |
| Jump | Space | South button (A / Cross) |
| Look | Mouse | Right stick |
| Zoom | Scroll wheel | |
| Ragdoll (die) | K | |
| Stand back up | R | |
| Free the cursor | Escape (click to lock it again) | |

![Goblin running in the ThirdPerson scene](images/thirdperson-play.png)
> 📷 **Image:** The goblin mid-run in the ThirdPerson scene, camera behind and slightly above.

### Demo helpers: fly camera and level keys

`Demo/Scripts/` has two components you can drop into any scene.

**Goblin Fly Camera** (**Add Component > Etherion Designs > Goblin Fly Camera**) goes on a camera and turns it into a smooth free-flying camera.

| Action | Keys |
|---|---|
| Move | W A S D or arrow keys |
| Up / down | E or Space / Q or Left Ctrl |
| Look | Mouse |
| Change speed | Scroll wheel |
| Go faster | Hold Left Shift |

| Setting | What it does |
|---|---|
| **Speed**, **Min Speed**, **Max Speed**, **Scroll Step**, **Boost** | Starting speed in m/s, the scroll wheel limits, the change per scroll notch (0.2 = 20 %) and the Shift multiplier |
| **Move Smooth Time**, **Look Smooth Time** | Seconds to speed up, stop and turn. 0 = instant |
| **Look Sensitivity**, **Pitch Limit**, **Invert Y** | Mouse look settings |
| **Hold Right Mouse To Look** | Look only while the right mouse button is held, so the cursor stays free |
| **Collide**, **Collision Radius**, **Collision Layers** | Stop at colliders and slide along walls instead of flying through |
| **Show Screen Text** and the four corner boxes | White text with a soft shadow, pinned to the screen corners, for example control hints. **Font Size**, **Margin** and **Shadow Offset** are in pixels at 1080p, and **Scale With Screen** keeps the size the same at any resolution |

The camera doesn't need a Rigidbody. Remove any other script that moves the same camera.

![Goblin Fly Camera in the Inspector](images/fly-camera-inspector.png)
> 📷 **Image:** A camera selected with the Goblin Fly Camera component in the Inspector, and the Game view showing corner text.

**Goblin Demo Level Keys** (**Add Component > Etherion Designs > Goblin Demo Level Keys**) switches scenes with **L** and quits with **Escape**.

1. Add it to any object in each scene you want to switch from.
2. Type scene names into **Levels**. Each press of L loads the next scene in the list, then wraps back to the first.
3. Add every listed scene to **File > Build Profiles > Scene List**. The Console warns about any that are missing.

In the editor, Escape stops Play mode. **Level Key** and **Quit Key** can be changed, and **Allow Quit** turns Escape off. UI buttons can call `LoadNextLevel()` or `LoadLevel("SceneName")`.

---

## 4. Placing a goblin in your scene

1. In the Project window, open `Goblin/Characters/`.
2. Drag a `PF_Goblin` prefab into the Scene view or Hierarchy.
3. Set its **Position** and **Rotation** to `0, 0, 0` (or wherever you want it). The goblin faces **+Z** at rotation 0.
4. Press Play. The goblin plays its idle animation.

![Goblin prefab dragged into the scene with Inspector visible](images/place-goblin.png)
> 📷 **Image:** A goblin in the Scene view with the Inspector showing the Transform at 0,0,0 and the Animator component below it.

### What's on the prefab

| Component | Purpose |
|---|---|
| **Animator** | Plays the animations. Uses the goblin's Humanoid avatar and the shared `AC_Goblin` controller. Apply Root Motion is off. |
| **LOD Group** | Swaps to lower-detail meshes at a distance: 50 %, 25 % and 10 % screen height, culled below 2 %. |
| **Goblin Appearance** | The character creator. Set to **Keep Current**, so the goblin looks exactly as you set it up. See [Random goblins](#11-random-goblins-and-the-limits-file) to make it randomize instead. |

The ragdoll prefabs have all of the above plus the ragdoll (see the next sections).

---

## 5. Animations

### Included clips

| Clip | Length | Notes |
|---|---|---|
| Idle | 7.57 s | Loops |
| Walk_Fwd | 2.73 s | Loops. Travels forward at 2.54 m/s |
| Walk_InPlace | 2.73 s | Loops. Stays in place |
| Run_Fwd | 1.90 s | Loops. Travels forward at 5.62 m/s |
| Jump | 0.87 s | Take-off |
| Fall_Loop | 3.00 s | Loops while in the air |
| Land | 0.87 s | Landing |

All clips are **Humanoid**, so they also play on any other Humanoid character, and any Humanoid animation from the Asset Store plays on the goblin.

### The Animator Controller

`Goblin/Characters/AC_Goblin.controller` holds every clip, with Idle as the default. All three goblin prefabs share this one controller. Change it once and every goblin follows.

![AC_Goblin open in the Animator window](images/animator-ac-goblin.png)
> 📷 **Image:** The Animator window with `AC_Goblin` open, showing all states with Idle in orange as the default.

### Playing a clip

To preview a clip in the editor:

1. Select a clip FBX in `Goblin/Animations/`.
2. In the Inspector, drag the goblin prefab onto the preview area at the bottom and press play.

To change what the goblin plays in your scene, open `AC_Goblin` in the **Animator** window, right-click a state and choose **Set as Layer Default State**.

### Root motion

Walk_Fwd and Run_Fwd move forward on their own. With **Apply Root Motion** off (the default), they play in place and your own script moves the character, which is how the demo's third-person controller works. Turn Apply Root Motion on in the Animator if you want the animation to move the goblin instead.

---

## 6. Ragdoll deaths

The `_Ragdoll` prefabs have a ready-made ragdoll: a Rigidbody, collider and joint on each of 11 bones (pelvis, upper and lower legs, upper and lower arms, chest and head), 30 kg in total. While the goblin is alive, the ragdoll follows the animation and has no effect. When it dies, the animation stops and physics takes over.

![Ragdoll colliders in the Scene view](images/ragdoll-colliders.png)
> 📷 **Image:** `PF_Goblin_Ragdoll` selected in the Scene view with Gizmos on, showing the capsule, box and sphere colliders on the limbs, chest and head.

### Making a goblin die

The **Ragdoll** component is on the root of each ragdoll prefab. Call it from your own damage code:

```csharp
using EtherionDesigns.Goblin;

var ragdoll = goblin.GetComponent<Ragdoll>();
ragdoll.Die();                                  // collapse on the spot
ragdoll.Die(hitDirection * 150f, hitPoint);     // knocked back from where it was hit (impulse in N·s)
ragdoll.Revive();                               // stand up again where the body ended up
```

To try it in the editor, enter Play mode, right-click the **Ragdoll** component header and choose **Die** or **Revive**.

### Ragdoll settings

| Setting | What it does |
|---|---|
| **Bodies** | The ragdoll bones, hips first. Already filled in |
| **Disable On Death** | Components turned off on death and back on by Revive. The Animator is already listed. Add your own AI, movement or input scripts here |
| **Colliders While Alive** | On: the limb colliders stay active while alive, so raycasts and projectiles can hit individual limbs. They never collide with the goblin's own Character Controller |
| **Inherit Velocity** | The body keeps the goblin's movement speed when it dies |
| **On Death / On Revive** | Events for your own sounds, effects or game logic |

> [!tip] Using your own character framework
> Many AI and controller assets (Emerald AI, Invector, Opsive and others) build and manage their own ragdoll. With those, start from the plain `PF_Goblin` prefabs and follow the framework's ragdoll setup instead.

---

## 7. The playable demo goblin (third person)

The ThirdPerson demo uses `Demo/Prefabs/PF_Demo_GoblinPlayer`. It's an example of the goblin as a playable character, not a full player controller. It has two parts side by side:

| Part | What's on it |
|---|---|
| **Goblin** | `PF_Goblin_Ragdoll` with a Character Controller, the **Third Person Character** movement script, the `AC_Goblin_ThirdPerson` Animator Controller and **Goblin Demo Ragdoll Keys** (K and R) |
| **Camera** | A camera tagged MainCamera with the **Third Person Camera** orbit script, following the Goblin |

![PF_Demo_GoblinPlayer in the Hierarchy](images/demo-player-hierarchy.png)
> 📷 **Image:** The Hierarchy with `PF_Demo_GoblinPlayer` expanded to show Goblin and Camera, and the Inspector showing Third Person Character on Goblin.

### Using it in your own scene

1. Drag `Demo/Prefabs/PF_Demo_GoblinPlayer` into the scene.
2. Delete the scene's own **Main Camera**, because the prefab brings its own.
3. Make sure there is ground under it, then press **Play**.

### The third-person Animator Controller

`Demo/Animations/AC_Goblin_ThirdPerson` uses three parameters, which the Third Person Character script sets every frame:

| Parameter | Type | Meaning |
|---|---|---|
| Speed | Float | Ground speed in m/s. Blends Idle, Walk (2.54 m/s) and Run (5.62 m/s) |
| Grounded | Bool | True while on the ground |
| Jump | Trigger | Fired on take-off |

The goblin switches to **Land** the moment it touches the ground, from either Jump or Fall.

![AC_Goblin_ThirdPerson in the Animator window](images/animator-thirdperson.png)
> 📷 **Image:** The Animator window with `AC_Goblin_ThirdPerson` open, showing the Locomotion blend tree and the Jump, Fall and Land states with their transitions.

### Driving it from your own code

Untick **Use Built In Input** on Third Person Character, then call:

```csharp
character.SetMoveInput(new Vector2(x, y), run);   // x = right, y = forward, 0 to 1
character.Jump();
```

### The camera

Third Person Camera follows its **Target**. If Target is empty, it follows the first Third Person Character in the scene. Mouse or right stick looks around, the scroll wheel zooms, and the camera moves in when something is between it and the goblin.

---

## 8. Materials and warpaint

| Material | Shader | Used for |
|---|---|---|
| `M_Goblin_Skin` | `Shader_Goblin_Skin` | Skin and body |
| `M_Goblin_Clothes` | `Shader_Goblin_Skin` | Clothing |
| `M_Goblin_Teeth` | `Shader_Goblin_Skin` | Teeth |
| `M_Goblin_Eye` | `Shader_Goblin_Eye` | Eyes |

All materials are in `Goblin/Materials/`, with extra skins in `Skin Variations/` and extra eyes in `Eye Variations/`. The shaders are Shader Graphs in `Goblin/Shaders/` and can be opened and edited.

### Warpaint

The body shader can paint warpaint on four body regions: **Head**, **Arms**, **Chest** and **Back**. Each region has 5 options, from 0 (no paint) to 1–4 (four different designs).

To set it on the material, select `M_Goblin_Skin` and change:

| Property | Region |
|---|---|
| `_Warpaint_Head_Type` | Head |
| `_Warpaint_Arms_Type` | Arms |
| `_Warpaint_Chest_Type` | Chest |
| `_Warpaint_Back_Type` | Back |

> [!tip]
> You usually don't need to touch these on the material. The character creator sets warpaint per goblin without changing the material file, so each goblin can have different paint.

![The four warpaint regions](images/warpaint-regions.png)
> 📷 **Image:** A 2×2 grid of the goblin with warpaint on one region each (head, arms, chest, back), labelled.

![All four warpaint designs](images/warpaint-designs.png)
> 📷 **Image:** The same goblin four times in a row, showing warpaint designs 1 to 4 on all regions.

---

## 9. The character creator

The character creator gives every goblin its own look. It can generate goblins at random, pick from looks you've designed, and remember each goblin between play sessions.

### The three pieces

| Piece | Where | What it does |
|---|---|---|
| **Goblin Appearance** component | On each goblin | Holds that goblin's look and decides how a new look is made |
| **Limits file** | `Data/GoblinLimits_Default` | The rulebook: everything that can change, how far, and which skin and eye materials to use |
| **Archetype Set** | `Data/GoblinArchetypes_Default` | Goblins you've designed and saved, such as "Fat Chief" or "Skinny Scout" |

### Setting it up: one click

1. Open your scene with goblins in it.
2. Choose **Tools > Etherion Designs > Goblin > Set Up Customization In Open Scene**.
3. Press **Play**.

This places the customization menu prefab and makes sure every goblin in the scene has a Goblin Appearance component with the Limits file and Archetype Set assigned. The `PF_Goblin` prefabs already have the component.

![Set Up Customization menu item](images/creator-setup-menu.png)
> 📷 **Image:** The Tools menu open at Etherion Designs > Goblin > Set Up Customization In Open Scene.

### Setting it up: by hand, or for one specific goblin

1. Select the goblin in the **Hierarchy**.
2. If it's not one of the `PF_Goblin` prefabs, **Add Component > Etherion Designs > Goblin Appearance.**
3. Set **Limits** to `Data/GoblinLimits_Default`.
4. Set **Archetype Set** to `Data/GoblinArchetypes_Default`.
5. Drag `UI/PF_GoblinCustomizationMenu` into the scene.
6. Select the menu object and drag your goblin into its **Target** field.
7. Press **Play**.

![Goblin Appearance component in the Inspector](images/goblin-appearance-inspector.png)
> 📷 **Image:** The Goblin Appearance component in the Inspector with Limits and Archetype Set assigned, and the slider section visible.

### Editing a goblin in the editor

You don't need to press Play to design a goblin. Select it, and the Goblin Appearance component shows a slider for every parameter, plus **Randomize**, **Reset** and **Save As Archetype** buttons. Changes show in the Scene view right away.

---

## 10. The customization menu

### Using the menu

![The customization menu, labelled](images/menu-labelled.png)
> 📷 **Image:** The menu in Play mode with numbered callouts on each area: 1 body sliders, 2 skin and eye sliders, 3 warpaint and clothes sliders, 4 Randomize and Skin & Eyes toggle, 5 Rotation, 6 Reset, 7 archetype controls.

| Control | What it does |
|---|---|
| **White sliders** | Body and face shape |
| **Yellow sliders** | Skin and eyes (type, hue, brightness, iris size) |
| **Green sliders** | Warpaint per region (0 = none) and clothes brightness, saturation and smoothness |
| **Randomize** | Rolls a new goblin. Untick **Skin & Eyes** first to keep the current skin and eyes |
| **Rotation** | Turns the goblin to see it from all sides |
| **Reset** | Puts every value back to default |
| **Name + Save Archetype** | Saves the current goblin as a preset |
| **< Archetype >** | Flips through saved presets |
| **Load / Delete** | Applies or removes the selected preset |
| **Copy / Paste** | Copies the look to the clipboard as text, or pastes one in |

> [!warning] Save Archetype in the editor vs. in a build
> In the Unity editor, Save Archetype adds the goblin to your Archetype Set, so it becomes part of your game. In a finished build, it saves a personal preset on the player's computer instead, and players can't delete the archetypes you shipped.

### Which goblin the menu edits

- **Target field:** select the menu object and drag a goblin into **Target**. The menu edits that goblin.
- **Target left empty:** the menu takes the first goblin it finds. Set Target if it matters which one.
- **From code:** `menu.SetTarget(goblin);`, for example when the player clicks a goblin.

![Menu object with Target assigned](images/menu-target.png)
> 📷 **Image:** The menu object selected in the Hierarchy, with the Inspector showing the Target field filled with a goblin.

### Changing how the menu looks

The menu is a normal Unity UI prefab. Double-click `Goblin/UI/PF_GoblinCustomizationMenu` to open it in Prefab Mode.

```
PF_GoblinCustomizationMenu      Goblin Customization Menu component
└─ Canvas
   ├─ Hint / Camera Hint        "M = Close Menu" and "Left Drag = Orbit   Middle Drag = Pan"
   └─ Panel                     Background panel
      ├─ Left Column
      │  └─ Sliders             Filled with parameter sliders at Play
      └─ Right Column
         ├─ Sliders             Filled with parameter sliders at Play
         └─ Footer              Randomize, Skin & Eyes, Rotation, Reset
                                and archetype controls
```

![Menu prefab open in Prefab Mode](images/menu-prefab-mode.png)
> 📷 **Image:** The menu prefab open in Prefab Mode, with the Hierarchy expanded to show Canvas, Panel, both columns and the Footer.

| To change | Do this |
|---|---|
| Layout, colours, fonts | Edit anything under **Panel** like normal UI |
| What a button does | Edit its **On Click** list. Each button calls a function on the root object, such as `GoblinCustomizationMenu.Randomize` |
| Add a button | Add a Button, press **+** on On Click, drag the root object in, and pick a function |
| Remove a button | Delete it |
| How parameter sliders look | Edit `UI/PF_GoblinMenuSliderRow`. Every parameter slider is a copy of it |
| Slider label colours | On the root object, under **Parameter Sliders** |
| Which sliders appear, and where | In the Limits file (see below) |
| Toggle key | **Toggle Key** on the root object (default M) |
| Camera speed | **Orbit Speed**, **Pan Speed** and **Zoom Speed** on the root object, under **Camera**. Untick **Enable Camera Orbit** to control the camera yourself |

Functions you can call from On Click: `Randomize`, `ResetLook`, `SetRotation`, `PreviousGoblin`, `NextGoblin`, `SaveArchetype`, `LoadArchetype`, `DeleteArchetype`, `PreviousArchetype`, `NextArchetype`, `CopyLook`, `PasteLook`, `Open`, `Close`.

![A button's On Click list](images/menu-onclick.png)
> 📷 **Image:** The Randomize button selected, with its On Click list showing the menu object and `GoblinCustomizationMenu.Randomize`.

> [!tip]
> You don't have to ship the menu. It's one prefab in the scene, so delete it if you only want it as a design tool.

---

## 11. Random goblins and the Limits file

### Generation settings

Select a goblin and open the **Generation** section of its Goblin Appearance component.

| Setting | What it does |
|---|---|
| **On Start** | **Keep Current** (the default on the prefabs) keeps the look you set in the editor. **Generate** makes a new look every time the game starts |
| **Source** | **Procedural** rolls every value at random. **Archetype Pool** picks one of your saved archetypes. **Mixed** does both |
| **Archetype Chance** | With Mixed, how often an archetype is picked (0 to 1) |
| **Archetype Variation** | 0 = an exact copy of the archetype. Around 0.2 = each copy comes out a little different |
| **Seed** | 0 = different every run. Any other number always gives the same goblin |

### The Limits file

Select `Data/GoblinLimits_Default`.

![Limits file in the Inspector](images/limits-inspector.png)
> 📷 **Image:** The Limits file in the Inspector, with the Material Sets list and one parameter (such as Belly Size) expanded to show its fields.

**Material Sets** are the skin and eye materials goblins can pick from. Drag your own materials into a list. Once a list has two or more materials, a **Skin Type** or **Eye Type** slider appears in the menu.

> [!warning]
> Always add new materials to the **end** of a list. Goblins remember their skin by its position in the list.

#### Rare materials: Weights

Each material set has a **Weights** list, one number per material in the same order as **Materials**. It sets how often random generation picks each material.

| Weight | Meaning |
|---|---|
| 1 | Normal |
| 0.5 | Half as likely |
| 3 | Three times as likely |
| 0 | Never picked at random, but still selectable in the menu |

For example, skin weights of `1, 1, 1, 0.2` make the last skin turn up on about 1 goblin in 16. New materials start at 1. If you reorder **Materials**, reorder **Weights** to match. Weights only affect new random goblins, never saved ones.

![Material set with weights](images/limits-weights.png)
> 📷 **Image:** The Skin material set in the Limits file, with Materials and Weights lists expanded side by side.

**Parameters** are everything that can change. Each one has:

| Field | Meaning |
|---|---|
| **Id** | The name used from code, for example `Belly` |
| **Display Name** | The label in the menu |
| **Target** | The blend shape, bone, or shader property **Reference** name, for example `_Hue` |
| **Material Set / Material Filter** | Material Float only. Which materials get the value: a material set such as `Eyes`, or part of a material name such as `Clothes` |
| **Value Mode** | Material Float only. **Set** replaces the material's value, **Add** adds to it, **Multiply** multiplies it |
| **Min / Max** | How far the menu slider goes |
| **Random Min / Random Max** | How far random generation goes. This is the one you'll change most |
| **Random Chance** | The odds the parameter gets a random value at all. Warpaint uses 0.6 |
| **Show In Menu** | Whether it appears in the customization menu |
| **Column** | Left or right column in the menu |
| **Space Before** | Adds a gap above it in the menu |

**Center Bias**, at the bottom, controls how extreme random goblins are. At 0, every value in the range is equally likely. Raise it and most goblins land near the middle.

#### Example: random goblins are too fat

Find **Belly Size** and lower its **Random Max** from 1 to 0.5. Players can still drag the slider all the way up, but random goblins stay slimmer.

#### Different goblin types

Duplicate the Limits file, change the ranges, and assign the copy to the goblins that should use it. A "Brute" file could push Muscularity and Shoulder Size toward the top of their ranges.

### Skin, eyes and clothes

Your material files are never changed. Each goblin picks a material, then applies its own changes on top. Hue is added to the material's hue. Brightness, saturation and smoothness multiply the material's own values, so each skin keeps its own character.

| Parameter | What it changes | Default random range |
|---|---|---|
| Skin Hue | Skin hue | ±10° |
| Skin Brightness | Skin brightness | 0.2 to 1.8 × the material |
| Eye Hue | Eye hue | ±40° |
| Eye Brightness | Eye brightness | 0.9 to 1.1 × the material |
| Iris Size | Iris and pupil size, the rest of the eye stays put. 1 = original | 0.3 to 1.5 |
| Clothes Brightness | Clothes brightness | 0.3 to 2 × the material |
| Clothes Saturation | Clothes colour strength | 0.5 to 1.4 × the material |
| Clothes Smoothness | Clothes shine | 0 to 1.5 × the material |

The clothes parameters only affect `M_Goblin_Clothes`, because their **Material Filter** is `Clothes`.

![Goblins with different clothes and iris settings](images/clothes-iris-variation.png)
> 📷 **Image:** Three goblins side by side with different clothes brightness, saturation and iris size.

### Adding your own

- **New morph targets:** select the Limits file, drag your mesh into the **Mesh** field at the bottom, and press **Add Missing Morph Targets**. Every blend shape starting with `Character_` that isn't listed yet is added.
- **New material properties:** add a parameter, set **Type** to **Material Float**, put the shader property's **Reference** name in **Target** (for example `_Roughness_Min`), and set **Material Set** to Skin. To target materials by name instead, leave Material Set empty and type part of the name in **Material Filter**, as the clothes parameters do with `Clothes`.

> [!note] Facial animation
> The ARKit facial blend shapes are never touched by the character creator, so face capture and customization work together.

---

## 12. Saving goblins between sessions

With **Save Between Sessions** ticked, a goblin keeps its look the next time the game runs. Goblins placed in a scene are saved automatically.

**Spawned goblins** need a name to be saved under. Set it right after spawning:

```csharp
var goblin = Instantiate(goblinPrefab).GetComponent<GoblinAppearance>();
goblin.SaveId = "camp_03_guard_1";
```

**Several save games:** set the active slot before the goblins appear:

```csharp
GoblinSaveSystem.Slot = "SaveGame2";
```

**Your own save system:** untick Save Between Sessions and store the look yourself:

```csharp
string look = goblin.ToJson();
goblin.FromJson(look);
```

Saves are JSON files in `Application.persistentDataPath/GoblinAppearances`. Open the folder with **Tools > Etherion Designs > Goblin > Open Save Folder**.

> [!warning] While testing
> A saved look always wins over a newly generated one. If your goblins stop changing between runs, use **Tools > Etherion Designs > Goblin > Delete Saved Appearances**.

---

## 13. Using the goblin from code

Everything is in the `EtherionDesigns.Goblin` namespace.

```csharp
using EtherionDesigns.Goblin;

goblin.Generate();                  // a new random look
goblin.Generate(1234);              // the same look every time for seed 1234
goblin.SetValue("Belly", 0.8f);     // change one parameter (by its Id)
goblin.ResetToDefault();            // back to default
goblin.Changed += OnGoblinChanged;  // get told when the look changes

menu.SetTarget(goblin);             // point the customization menu at a goblin
menu.Open();
menu.Close();
```

The ragdoll and the demo's third-person scripts are in the same namespace:

```csharp
ragdoll.Die(impulse, hitPoint);     // see Ragdoll deaths
ragdoll.Revive();
bool dead = ragdoll.IsDead;

character.SetMoveInput(new Vector2(x, y), run);
character.Jump();
bool grounded = character.IsGrounded;
Vector3 velocity = character.Velocity;
```

---

## 14. Troubleshooting

| Problem | Fix |
|---|---|
| Goblins look the same every time I press Play | The prefabs default to **Keep Current**. Set **On Start** to **Generate** on Goblin Appearance. If it's already Generate, a saved look is loading: **Tools > Etherion Designs > Goblin > Delete Saved Appearances** |
| There's no Skin Type or Eye Type slider | The Skin or Eyes list in the Limits file needs two or more materials |
| The menu doesn't show up | Check the scene has the `PF_GoblinCustomizationMenu` prefab, and press M |
| Console says the menu has no menu parts assigned | The scene has a bare menu component instead of the prefab. Run **Set Up Customization In Open Scene** again, or replace it with the prefab |
| Menu text is missing or pink | **Window > TextMeshPro > Import TMP Essential Resources** |
| The menu edits the wrong goblin | Drag the goblin you want into the menu's **Target** field |
| Skin looks lumpy when morphs are turned up | Select the goblin FBX, Model tab: Normals **Calculate**, Smoothing Angle **180**, Blend Shape Normals **Calculate**. The included models are already set this way |
| A colour or size slider does nothing on my own shader | The shader needs properties with matching **Reference** names (the name in the Blackboard doesn't count). Skin: `_Hue`, `_Brightness`. Eyes: `_Hue`, `_Dif_Brightness`, `_ScaleMultiplier`. Clothes: `_Brightness`, `_Saturation`, `_Smoothness_Master` |
| A rare material never turns up | Check its **Weight** in the material set. 0 means random goblins never get it |
| The level key does nothing | Add the scene to **File > Build Profiles > Scene List** and check its name in **Levels** |
| The goblin slides or snaps back while walking | On the walk and run clips, untick **Root Transform Position (XZ) > Bake Into Pose** |
| The ragdoll goblin keeps walking after Die() | Add your movement or AI script to **Disable On Death** on the Ragdoll component |
| Two cameras, or the view is wrong with `PF_Demo_GoblinPlayer` | Delete the scene's own Main Camera. The demo prefab brings its own |
| Inner faces show through on the belt | Select `M_Goblin_Clothes` and set **Surface Type** to **Opaque** with **Alpha Clipping** on. Transparent draws the inner straps over the outer ones |

---

*Questions or problems? Contact Etherion Designs through the store page.*
