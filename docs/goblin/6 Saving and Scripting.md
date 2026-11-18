# Saving and Scripting

## Saving goblins between sessions

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

Saves are JSON files in `Application.persistentDataPath/GoblinAppearances`: one file per save slot, plus `Presets.json` for archetypes players save from the menu in a build. Open the folder with **Tools > Etherion Designs > Goblin > Open Save Folder**.

On Windows builds that's `C:\Users\<user>\AppData\LocalLow\<Company Name>\<Product Name>\GoblinAppearances`. Company Name and Product Name come from **Project Settings > Player**, so changing them starts a new, empty save folder.

> [!warning] While testing
> A saved look always wins over a newly generated one. If your goblins stop changing between runs, use **Tools > Etherion Designs > Goblin > Delete Saved Appearances**.

---

## Using the goblin from code

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

The ragdoll is in the same namespace:

```csharp
ragdoll.Die(impulse, hitPoint);     // see Ragdoll deaths
ragdoll.Revive();
bool dead = ragdoll.IsDead;
```
