# Troubleshooting

| Problem                                                       | Fix |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Goblins look the same every time I press Play                 | The prefabs default to **Keep Current**. Set **On Start** to **Generate** on Goblin Appearance. If it's already Generate, a saved look is loading: **Tools > Etherion Designs > Goblin > Delete Saved Appearances** |
| There's no Skin Type or Eye Type slider                       | The Skin or Eyes list in the Limits file needs two or more materials |
| The menu doesn't show up                                      | Check the scene has the `PF_GoblinCustomizationMenu` prefab, and press M |
| Console says the menu has no menu parts assigned              | The scene has a bare menu component instead of the prefab. Run **Set Up Customization In Open Scene** again, or replace it with the prefab |
| Menu text is missing or pink                                  | **Window > TextMeshPro > Import TMP Essential Resources** |
| The menu edits the wrong goblin                               | Drag the goblin you want into the menu's **Target** field |
| Skin looks lumpy when morphs are turned up                    | Select the goblin FBX, Model tab: Normals **Calculate**, Smoothing Angle **180**, Blend Shape Normals **Calculate**. The included models are already set this way |
| A colour or size slider does nothing on my own shader         | The shader needs properties with matching **Reference** names (the name in the Blackboard doesn't count). Skin: `_Hue`, `_Brightness`. Eyes: `_Hue`, `_Dif_Brightness`, `_ScaleMultiplier`. Clothes: `_Brightness`, `_Saturation`, `_Smoothness_Master` |
| A rare material never turns up                                | Check its **Weight** in the material set. 0 means random goblins never get it |
| The goblin slides or snaps back while walking                 | On the walk and run clips, untick **Root Transform Position (XZ) > Bake Into Pose** |
| The ragdoll goblin keeps walking after Die()                  | Add your movement or AI script to **Disable On Death** on the Ragdoll component |
| The camera stops moving when I close the menu                 | Tick **Orbit When Closed** on the menu, under **Camera** |
| HDRP: the skin has no soft subsurface look                    | Add `DiffusionProfile_GoblinSkin` to a **Diffusion Profile List** (see [Using HDRP](<1 Installation.md#using-hdrp>)) |
| Inner faces show through on the belt                          | Select `M_Goblin_Clothes` and set **Surface Type** to **Opaque** with **Alpha Clipping** on. Transparent draws the inner straps over the outer ones |

---

## Contact support

If your problem isn't listed above, get in touch:

1. **Discord (fastest):** join the [Etherion Designs support server](http://dsc.gg/etheriondesigns). This is the quickest way to get a fix.
2. **Contact form:** use the form on [etheriondesigns.com/contact](https://www.etheriondesigns.com/contact).
