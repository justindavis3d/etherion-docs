# Checklist
This checklist is designed for those who have followed our guide but are encountering difficulties with their project or want to ensure no steps have been missed.

---

### [Required Project Settings](https://etheriondesigns.com/docs/foliage-setup-required-project-settings/)

**In Edit>Project Settings**

- [Add “BlockedBulletCollision”](https://etheriondesigns.com/docs/foliage-setup-required-project-settings/#blockedbullet)
- [Enable Virtual Textures](https://etheriondesigns.com/docs/foliage-setup-required-project-settings/#virtualtexturesupport)
- [Enable DBuffer Decals](https://etheriondesigns.com/docs/foliage-setup-required-project-settings/#decal)

**In Edit>Plugins**

- Enable **Foliage Physics** Plugin
- [Enable **Water** Plugin](https://etheriondesigns.com/docs/foliage-setup-required-project-settings/#fluidsimulationsupport)
- [Enable **Chaos Vehicle** Plugin](https://etheriondesigns.com/docs/foliage-setup-required-project-settings/#vehiclesupport)

---

### [Painting Foliage](https://etheriondesigns.com/docs/foliage-setup-painting-foliage/)

- Collision Enabled: “**Query Only**”, or  “**Query and physics**”
- **“Visibility”** trace response must be checked
- “**BlockedBullet**” Collision Response must be “**Block**” if weapons are to hit it
- “**BlockedBullet**” Collision Response must be “**Ignore**” if weapons are to ignore it
- All other Collision Response channels act as a fallback incase foliage physics is disabled.

---

### [Foliage System Setup](https://etheriondesigns.com/docs/foliage-setup-foliage-system-setup/)

- Ensure your project has a foliage map with correct foliage entries
- Drag **BP_FoliageInfluencer** into your Pawn, Vehicle or Object blueprint
- Toggle “**Debug**” and adjust radius value of **BP_FoliageInfluencer**
- Duplicate as needed to cover mesh area tightly for good performance
- Adjust additional settings as needed, for all influencers in your blueprint.

---

### [Packaging](https://etheriondesigns.com/docs/system-setup/#11-toc-title)

- Under **Project Settings > Asset Manager**, you have to add the **EDFoliageMap** class.
- **[Click here](https://etheriondesigns.com/wp-content/uploads/2024/11/Documentation_Packaging_FoliageMap.webp)** to see reference image