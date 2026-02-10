# Common Plugin Conflicts

This document provides a reference list of third-party plugins known to cause startup failures, freezes, or crashes in JetBrains IDEs. Use this list to guide the diagnosis process when a plugin conflict is suspected.

## High-Impact Conflicts (Frequently Cause Crashes or Freezes)

| Plugin Name | Common Symptoms | Immediate Remediation |
| :--- | :--- | :--- |
| **GitHub Copilot** | `AccessDeniedException` on `copilot-agent-win.exe`; blocks startup on Windows. | Manually terminate the `copilot-agent` process and restart the IDE. |
| **Codeium** | `AccessDeniedException` on `language_server_windows_x64.exe`; blocks plugin updates and IDE startup. | Manually terminate the `language_server` process from the Task Manager. |
| **SonarLint** | Repetitive IDE freezes (4-15 seconds) on startup; can cause crashes with misconfigured certificates. | Disable the plugin and remove its directory from the plugins folder. |
| **Illuminated Cloud 2** | IDE crashes immediately on startup (affects older versions like 2.0.6.9). | Manually remove the plugin and install an updated version (2.0.7.0+). |
| **Grazie / Grazie Pro** | Causes persistent IDE freezing, making it unusable; conflicts with AI-based plugins. | Disable the Grazie and Grazie Professional plugins. |

## Moderate-Impact Conflicts (Cause UI/Performance Issues)

| Plugin Name | Common Symptoms | Immediate Remediation |
| :--- | :--- | :--- |
| **IdeaVim** | Causes IDE to hang during initialization, especially when used with other plugins like Copilot. | Temporarily disable IdeaVim, allow the IDE to start, and then re-enable it. |
| **Material Theme UI** | Breaks UI elements like folder icons and drop-down menus; can cause internal errors. | Disable the plugin and restart the IDE. |
| **Rainbow Brackets** | Disables semantic highlighting on startup; can conflict with other language plugins. | Disable the plugin. |
| **Kubernetes** | Slow startup (20+ seconds on splash screen) if the backend component is missing or misconfigured. | Ensure the plugin is fully installed or disable it if not needed. |

## Compatibility and Configuration Conflicts

| Plugin Name | Common Symptoms | Immediate Remediation |
| :--- | :--- | :--- |
| **Conflicting Lua Plugins** | A frozen, unresponsive "Conflicting Plugins" dialog on startup (e.g., EmmyLua vs. SumnekoLua). | Manually remove one of the conflicting Lua plugins from the plugins directory. |
| **Lombok** | "Plugin incompatible" errors after an IDE upgrade. | Update the plugin to a version matching the IDE and ensure Annotation Processing is enabled. |
| **Code With Me** | Can cause an "Unhandled exception" on startup, leading to loss of code completion. | Disable or update the plugin. |
| **Classic UI** | "Plugin conflicts with IDE" error, especially in remote development sessions. | Disable the plugin for remote development. |
