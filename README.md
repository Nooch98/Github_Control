# 🚀 GitHub Control

**GitHub Control** is a powerful open-source desktop app for managing multiple GitHub accounts with advanced features that even surpass official tools like GitHub Desktop.

It’s designed with flexibility, extensibility, and productivity in mind — featuring a plugin system, real-time GitHub status, integrated terminal, and more.

---

## ✨ Main Features

- 🔑 **Multi-account support** via GitHub API Keys

![Captura de pantalla 2025-04-22 012414](https://github.com/user-attachments/assets/00d31255-f53d-4413-9613-1d4cbd4aeb5e)

- 📁 **Complete repo explorer** (files, releases, issues, stats, vulnerabilities)

![Captura de pantalla 2025-04-22 012457](https://github.com/user-attachments/assets/e2adc275-8623-48d5-aa9f-6b6e43c2db46)

- 🔄 **Commit and branch management**, including cloning and backups
- 🧪 **Experimental code analysis** (currently Python-only)
- 🌐 **Global repo search** Search any repo on github

![Captura de pantalla 2025-04-22 012724](https://github.com/user-attachments/assets/4c18f7e4-2b6d-4a9d-b8a2-6f92b4a5d938)

- ⚙️ **Edit repo files** directly from the UI
- 📊 **Detailed user and repo statistics**

![Captura de pantalla 2025-04-22 012910](https://github.com/user-attachments/assets/62167931-e898-476f-bf04-95a3d3be0042)

- 🔐 **Confidential mode** to hide user identity

![Captura de pantalla 2025-04-22 013017](https://github.com/user-attachments/assets/0e354bd6-9543-45d7-b6ea-3ab19e716b8f)

- 💻 **Integrated terminal** with custom command support

![Captura de pantalla 2025-04-22 013058](https://github.com/user-attachments/assets/ee68fa70-4690-4433-b9f6-562745a8d09a)

- 📦 **Plugin system** with automatic install/update
- ⬇️ **App downgrade and update support** via command
- 💾 **Repo backup and restore system**
- 🚦 **Real-time GitHub status monitor** (refresh every 60s)

![Captura de pantalla 2025-04-22 013142](https://github.com/user-attachments/assets/3af679b8-09f6-4983-a8fd-ec7423f5dec3)

- ⚡ **Local cache system** (offline GitHub API fallback)

---

## 📦 Installation

Download the latest version from [Releases](https://github.com/Nooch98/Github_Control/releases)


```bash
# Windows
GithubControl_Setup_x64.exe
```

---

## 🔹 Option 2: Integrated into Organizer

**‼️‼️‼️ This is not yet available. ‼️‼️‼️**

If you already use [Organizer](https://github.com/Nooch98/Organizer), you can install GitHub Control as a module:
1. Open Organizer
2. Go to Settings > Extensions
3. Enable **GitHub Control**

---

## 💻 Requirements

* Python 3.12.10
* Git installed and in PATH (to clone repositories)
* Internet access
* Recommended font: CaskaydiaMono Nerd Font (for a better experience in the integrated terminal)

---

## 🛠️ Available commands (integrated terminal)

```bash
help # Displays help
install <plugin> # Installs plugin
uninstall <plugin> # Uninstalls plugin
plugins list # Lists available plugins
update # Updates the app
versions # Displays all versions
versions <version> # Displays details about a version
plugins update # Updates installed plugins
clear # Clears the terminal
```

---

## 📦 Plugin structure in the official repository

Each plugin will be in its own subdirectory within `github_control_plugins/`, and should contain:

```bash
github_control_plugins/
├── nombre_plugin/
│   ├── plugin.py       # Readable source code
│   ├── plugin.exe      # Compiled executable
│   └── plugin.json     # Metadata (name, version, description, author, SHA256 hash of the executable, etc.)
```
---

### 📃 Example `plugin.json`

```json
{
    "name": "Example",
    "version": "1.0.0",
    "description": "Example plugin.",
    "author": "Nooch98",
    "entry": "Example.exe",
    "source": "Example.py",
    "hash": "B0A12F11AAB09165888131356F61DBB0E9A69647997DB59B7F220B687AF5DD99"
}
```

---

## 🚧 Project status

- ✔️ Functional integrated terminal
- ✔️ Multi-account support
- ✔️ Remote file editor
- ✔️ Advanced repo management
- ✔️ Plugin system
- ⚠️ Multi-language code analysis (currently only Python)
- ⏳ GitLab/Bitbucket support (future)
- ⏳ Multi-language support for code analysis

---

## 🔮 Roadmap

- 📎 GitHub Actions viewer
- 


---

## 🧠 License

**Creative Commons Attribution-NonCommercial 4.0 International** © Nooch98

---

## ❤️ Credits

Created by someone who is not a professional engineer or programmer.

---
