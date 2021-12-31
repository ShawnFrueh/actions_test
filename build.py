from os import mkdir
from pathlib import Path
from shutil import rmtree
from zipfile import ZipFile, ZIP_DEFLATED

# Get the root path to this repo
repo_dir = Path(__file__).parent
# Get the kit directory
kit_dir = repo_dir / "test_kit"
# Get the build directory
build_dir = repo_dir / "build"
# Get the license file
license_file = repo_dir / "LICENSE"
version = 10

# Get all files in the kit directory and male sure no pyc files come along
kit_files = [f for f in kit_dir.glob("**/*") if f.is_file() and not f.name.endswith(".pyc")]

# Clear the build directory
if build_dir.exists():
    rmtree(build_dir)
# Remake the build directory
mkdir(build_dir)

# Format the lpk file name with the version number from the VERSION file
lpk_name = f"test_kit_{version}.lpk"
lpk_path = build_dir / lpk_name

# Build the LPK file.
with ZipFile(lpk_path, mode="w", compression=ZIP_DEFLATED) as lpk:
    # Add the license
    lpk.write(license_file, "license")

    # Write all file into the lpk
    for file in kit_files:
        print(file.relative_to(kit_dir))
        lpk.write(file, file.relative_to(kit_dir))
