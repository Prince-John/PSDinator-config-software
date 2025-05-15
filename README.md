# PSDinator Configuration Software

### WashU CFD-PSD Chipboard Configuration Utility

---

## Overview

This software package contains the GUI application and the python API to generate the commands for the configuration and management of WashU's custom CFD-PSD ASIC-based chipboards.

---

## Installation

PSDinator utilizes Poetry to manage dependencies, ensuring easy installation and compatibility.

### Recommended Installation (Using pipx)

I strongly recommend using **[pipx](https://pipx.pypa.io/stable/)** for installation. Pipx creates isolated environments, keeping your system clean and avoiding dependency conflicts.

#### Steps:

1. **Download the latest release wheel:**

```shell
wget https://github.com/Prince-John/PSDinator-config-software/releases/download/v0.1.1/psdinator_configuration_software-0.1.1-py3-none-any.whl
```

2. **Install using pipx:**

```shell
pipx install ./psdinator_configuration_software-0.1.1-py3-none-any.whl
```

### Alternative Installation (Using pip)

If you prefer managing your own Python virtual environments:

1. Create and activate your virtual environment (example with `venv`):

```shell
python3 -m venv psdinator-env
source psdinator-env/bin/activate
```

2. Install PSDinator:

```shell
pip install ./psdinator_configuration_software-0.1.1-py3-none-any.whl
```

---

## Usage

After installation, launch PSDinator from your terminal:

```shell
psdinator
```

**Note:** Global usage of the `psdinator` command is only available if installed using pipx.

The application window will open, allowing you to configure and manage your CFD-PSD chipboards.

---

**Maintainer:** Prince John

