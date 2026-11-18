# Saving and Scripting

Everything is in the `EtherionDesigns.Goblin` namespace.

```csharp
using EtherionDesigns.Goblin;
```

## Changing a goblin from code

```csharp
var goblin = goblinObject.GetComponent<GoblinAppearance>();

goblin.Generate();                  // a new random look
goblin.Generate(1234);              // the same look every time for seed 1234
goblin.SetValue("Belly", 0.8f);     // change one parameter, by its Id in the Limits file
float belly = goblin.GetValue("Belly");
goblin.ResetToDefault();            // back to default
goblin.Changed += OnGoblinChanged;  // get told when the look changes
```

For example, to spawn an enemy with a fresh random look:

```csharp
var enemy = Instantiate(goblinPrefab, position, rotation);
enemy.GetComponent<GoblinAppearance>().Generate();
```

If the prefab's **On Start** is set to **Generate**, this happens by itself and you don't need the second line.

The ragdoll calls are on [Using Goblins with Your AI](<2 Using Goblins with Your AI.md#ragdoll-deaths>).

---

## Saving goblin looks

With **Save Between Sessions** ticked on Goblin Appearance, a goblin keeps its look the next time the game runs. It is ticked on the prefabs.

| Goblin | What happens |
|---|---|
| Placed in a scene | Saved automatically |
| Spawned from code | Not saved, unless you give it a name to be saved under |

To save a spawned goblin, set its name right after spawning:

```csharp
var goblin = Instantiate(goblinPrefab).GetComponent<GoblinAppearance>();
goblin.SaveId = "camp_03_guard_1";
```

**Several save games:** set the active slot before the goblins appear:

```csharp
GoblinSaveSystem.Slot = "SaveGame2";
```

**Your own save system:** untick Save Between Sessions and store the look yourself as text:

```csharp
string look = goblin.ToJson();
goblin.FromJson(look);
```

Saves are JSON files in `Application.persistentDataPath/GoblinAppearances`, one file per save slot. Open the folder with **Tools > Etherion Designs > Goblin > Open Save Folder**.

> [!warning] While testing
> A saved look always wins over a newly generated one. If your goblins stop changing between runs, use **Tools > Etherion Designs > Goblin > Delete Saved Appearances**.
