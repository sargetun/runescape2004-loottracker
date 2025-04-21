project_summary = """
# RuneScape Loot Tracker — Project Summary (v1.0)

**Focus:** Build the application GUI and backend logic in modern, clean Python using updated practices. Future integrations (like memory, stats, or syncing) will be added later.

---

## Project Purpose
A desktop application that allows users to track monster kills and loot in RuneScape. It includes monster details, a kill tracker, and organized loot logs. The user should be able to interact with the app through a clean, multi-screen interface.
Help me create a loot tracker application for 2004 lostcity runescape private server, i want it to be an all in one application as well so it is easy to share.
---

## Key Modules & Screens

### 1. Main Window
- Acts as the central navigation hub
- Displays a title, navigation buttons, and dynamic screen content
- Displays current kill list with loot table from all the kill data

### 2. Monster List Screen
- Shows a list of RuneScape monsters
- Each monster entry displays:
  - Name
  - Image
  - Combat details
  - Total kills
  - Loot summary for that monster

### 3. Kill Entry Screen
- Allows the user to:
  - Select a monster
  - Add a kill
  - Select from predefined loot options (specific to that monster)
  - Optionally add custom loot
  - Remove a kill or remove loot as well

### 4. Data Management
- Data should persist between sessions
- Will use JSON or SQLite (modular backend support)
- Stores:
  - Monsters
  - Loot items
  - Kill history
  
### 5. 

---

## Modern Python Stack

- **GUI Framework:** `PySide6` (preferred for modern UI and cross-platform compatibility)
- **Language:** Python 3.11+
- **Structure:**
  - `main.py` — Entry point
  - `screens/` — Contains all GUI screen classes (e.g. `monster_list.py`, `kill_entry.py`)
  - `models/` — Data representations (`monster.py`, `loot.py`, etc.)
  - `storage/` — File/database handling
  - `assets/` — Images, icons
  - `utils/` — Helper functions, data loading, etc.

---

## Initial Development Goals

1. Build the application window and navigation system (multi-screen support)
2. Create and display the monster list using placeholders so i can fill the information in (names, images, details)
3. Build a kill entry screen where users can input kill data
4. Implement data saving/loading logic in JSON format
5. Ensure changes persist and display correctly across screens

---

## Coding Guidelines

- Use **object-oriented design**
- Apply **MVC or MVVM** patterns where appropriate
- Follow **PEP8** and include inline comments/docstrings
- Ensure **modularity**: every screen and feature in its own file/class
- Code should be consistently structured and easily extensible
"""