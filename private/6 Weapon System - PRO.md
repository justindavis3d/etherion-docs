# Overview

The weapon system allows you to use and manage different weapons in the game effectively. It consists of two main parts: the Weapon System Component and the Weapon Component. The Weapon System Component handles overall weapon management, including switching weapons and firing mechanics, while the Weapon Component defines the specific behaviors and characteristics of each weapon

## Weapon System Component

The Weapon System Component is the central part of the weapon management system. It handles weapon registration and controls weapon selection, enabling players to switch between different weapons. This component also manages firing actions, including aim-down-sights functionality.

_**Note:** To get started with weapon system components, you can either create a custom component from scratch, or you can refer to the Demo Weapon System Component Blueprint provided in the project. You can find the it here:_

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_DemoWeaponSystemComponent.webp)

### Create a Weapon System Component Blueprint

In Unreal Engine, go to **Content Browser** > Right-click > **Blueprint Class**.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_CreateBlueprint.webp)

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_SelectBlueprintParent.webp)

Select **EDWeaponSystemComponent** as the parent class.

Open the newly created actor and configure it’s values in the **Class Defaults** section.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_SetDefaultValues-1024x695.webp)

### Handle Input

For the **weapon system component** to work you need to set up it’s input functions:

- **Cycle Weapons:** This function will cycle through the weapons as the name suggests, You can bind it to an **InputAxis** node and assign it’s axis value to the direction.
- **Fire Input:** This function tells the component whether the fire button is pressed or not, Allowing you to set-up custom inputs for the fire mechanism. You can bind it to an **InputAction** node as shown in the image below.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_HandleInputs.webp)

### Register Weapon Components

In order to add weapons to your **Weapon System Component** you need to create and register them inside a specific event/function called **Create Weapons**.

To do that, First override the **Create Weapons** function in your blueprint.

This will add an event in the **Event Graph** called **Event Create Weapons** which you can then use to register your weapons.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_OverrideCreateWeapons-1024x700.webp)

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_ConvertEventToFunction-1024x700.webp)

If you’re like me and prefer to use it as a function instead, you can **Right Click** the node and select **Convert event to function**.

Navigate into the **CreateWeapons** function and register your first weapon by following these steps:

- Create a new instance of your **Weapon Component** using the **Add Component by Class** node with the desired **weapon component** class.
- Make sure You pass **Get Owner** to the **Target** input so that it belongs to the same character in which the **Weapon System Component** does.
- Also Make sure you pass **Self** to the **Weapon System** input so that the **Weapon Component** knows what **System** it belongs to.
- Finally, Register the weapon component using the **Register Weapon Component** node, providing it with a unique identifier and whether it’s in rapid fire mode.  
    You can use **Unique Identifier** to select this weapon using the **Select Weapon** node later on.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_RegisterWeaponComponent-1024x700.webp)

### Add It to Your Character

Navigate to your character blueprint and add the **Weapon System Component** that you created in the last section.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_AddWeaponSystemToCharacter-1024x700.webp)

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_SetupWeaponSystemOnCharacter-1024x668.webp)

Select the newly added component and set-up it’s values in the **Details Panel** if needed.

Use the **Set Fire Origin** node to tell the component where the **Fire Origin** is located so that it can fire from that location.

Weapons only fire in ADS mode, so make sure you correctly set it up using the **Set ADS** node.

For example, here is the **Set ADS** logic implemented in the **ALS_AnimMan_CharacterBP** character blueprint which only allows ADS when it’s not in **Ragdoll** mode.

This is the reason why it’s implemented in the character rather than the **Weapon Component System** like the function **Fire Input**.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_SetADSInALSPawn-1024x668.webp)

### Selecting a Specific Weapon

You can select a specific weapon using it’s registered **Unique Identifier** explained in the previous steps using the **Select Weapon** node.

You can call this node where-ever you have access to the **Weapon System Component**.  
For example, In this image we are selecting the weapon registered above inside of the character blueprint.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_SelectWeapon-1024x668.webp)

### Getting the Current Weapon

You can retrieve the currently selected weapon using the **Get Current Weapon Validated** node.

If there is currently a weapon selected it will return it and continue with the **Valid** execution pin, otherwise it will return an empty struct and continue with the **Invalid** execution pin.  
  
The **WeaponType** struct includes the **Weapon Component**, **Unique Identifier**, and **IsRapid** values.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_GetCurrentWeapon-1024x668.webp)

### Handle ADS Events

You can implement **ADS** events on the **Weapon System Component** to provide customized logic for when **ADS** happens.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_ADSEvents-1024x668.webp)

### Disabling the Weapon system Component

You can **Enable** and **Disable** the **Weapon System Component** using the **Set Enabled** node.

While disabled, the weapon system component doesn’t respond to events and doesn’t update it’s internal state.

Upon being disabled the weapon system component will **Deselect** the currently selected weapon.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_Disable-1024x668.webp)

---

## Weapon Component

The Weapon Component represents a specific weapon in the game. This component handles the firing logic, allowing for custom weapon implementation.

### Create a Weapon Component Blueprint

In Unreal Engine, go to **Content Browser** > Right-click > **Blueprint Class**.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_CreateBlueprint.webp)

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_Weapon_SelectBlueprintParent.webp)

Select **EDWeaponComponent** as the parent class.

Open the newly created actor and configure it’s values in the **Class Defaults** section.

The **Name** variable is an arbitrary variable which you can use to display weapon information on HUD.  
In the **Demo** it’s used in the **Get HUD Text** function of the **BP_Weapon_Base** blueprint.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_Weapon_SetDefaultValues-1024x668.webp)

_**Note:** The **IsRapid** variable is not defined as an instance editable variable on the **Weapon Component** instead it’s exposed on the **Register Weapon Component** allowing the same component being registered multiple times with different **IsRapid** and **Unique Identifier** variables. You can however read it’s value in the blueprints._

### Handle Weapon Selection

The **Selected** event triggers when this weapon is selected via cycling, a **Select Weapon** call, or when the **Weapon System Component** is enabled by a **Set Enabled** call.

Similarly, The **Deselected** event triggers when another weapon is selected via cycling or a **Select Weapon** call, or when the **Weapon System Component** is disabled by a **Set Enabled** call.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_Weapon_SelectionEvents-1024x668.webp)

### Handle Fire Logic

The **Fire** event serves as the main point to handle your fire logic. There are additional events that give you the flexibility to customize your weapons.

The **Begin Fire** event triggers right before the weapon starts warming up. The **Tick Fire** event is also triggered during the warmup phase. To determine if a weapon is in warmup, you can use the **Is In Warmup** node.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_Weapon_FireEvents-1024x668.webp)

### Handle ADS Logic

Similar to **Weapon System Component**, You can implement **ADS** events on the **Weapon Component** as well to provide customized logic for when **ADS** happens.

For example, if you want to play a sound when player Aims and it’s specific to this weapon type, the **Begin ADS** event is the perfect place to spawn the **Sound**.

![](https://etheriondesigns.com/wp-content/uploads/2024/10/Documentation_WeaponSystem_Weapon_ADSEvents-1024x668.webp)

---

## Using Trace Weapons in the Demo

When using our demo weapon system, weapons that utilize trace mechanics, such as **Beam** and **Instant** weapons, do not automatically penetrate static mesh components or foliage blueprints. They will only penetrate these objects and hit the objects behind them if they have the **BeamPenetrable** actor tag.  
Furthermore, The trace weapons don’t account for hit objects with components that ignore the **BlockedBullet** collision response channel.

These functionalities are defined in the **Apply Trace Damage** function of the **BP_Weapon_Base** blueprint, which is used in the **Beam** and **Instant** weapons.