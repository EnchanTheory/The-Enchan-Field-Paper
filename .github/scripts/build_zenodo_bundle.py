#!/usr/bin/env python3
"""Build the source ZIP and companion PDF for the current manuscript's Zenodo record.

The source archive preserves the v1.0.4 package's flat nine-file structure
and adds the revision notes so the v1.0.5 updates remain self-contained.
This script never uploads or modifies a Zenodo record.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "zenodo_bundle"

FIGURE_HASHES = {
    "figures/enchan_ising_tabu_comparison.png": "a0f6226b03a7bb5add9cad4fd47ec2dc13728d3094dc6f41e54b15bbd0c72b19",
    "figures/enchan_solar_system_delta_accel_boost.png": "60f180f74471036404472f2730b1055451e747813285b658422e8155bb1f8959",
    "figures/enchan_solar_system_delta_accel_delta_g.png": "603043042857047fab1f2ae4c20400fb04010ab971a131167a091496f9db37c5",
    "figures/enchan_web_google_audit.png": "002529c4926244a4b714550023aa25b4c02d10e8a8d877bf7c9fab9f1ae1be10",
}

paper = (ROOT / "main.tex").read_text(encoding="utf-8")
match = re.search(r"\\date\{[^\n]*v(\d+\.\d+\.\d+)", paper)
if not match:
    raise SystemExit("Cannot determine the manuscript version from main.tex date")
version = match.group(1)
if version != "1.0.5":
    raise SystemExit(f"Unexpected manuscript version v{version}: this bundle is for v1.0.5")
pdf = ROOT / "main.pdf"
pdf_bytes = pdf.read_bytes()
if not pdf_bytes.startswith(b"%PDF-") or len(pdf_bytes) < 100_000:
    raise SystemExit("main.pdf is not a compiled manuscript PDF")
if b"%%EOF" not in pdf_bytes[-2048:]:
    raise SystemExit("main.pdf missing final PDF EOF marker")

paths = [
    "main.tex",
    "README.md",
    "LICENSE",
    "DATA_PROVENANCE.md",
    "FIGURE_PROVENANCE.md",
    "REVISION_v1.0.5.md",
    *FIGURE_HASHES,
]

for name in paths:
    if not (ROOT / name).is_file():
        raise SystemExit(f"Missing source package file: {name}")
    if name in FIGURE_HASHES:
        found = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if found != FIGURE_HASHES[name]:
            raise SystemExit(f"Figure checksum mismatch: {name}: {found}")

OUT.mkdir(exist_ok=True)
pdf_name = f"The_Enchan_Field_v{version}.pdf"
zip_name = f"The-Enchan-Field-Paper-v{version}.zip"

# Only one version's distribution files belong in this current-release directory.
for old in OUT.glob("The-Enchan-Field-Paper-v*.zip"):
    old.unlink()
for old in OUT.glob("The_Enchan_Field_v*.pdf"):
    old.unlink()

shutil.copyfile(pdf, OUT / pdf_name)
shutil.copyfile(ROOT / "LICENSE", OUT / "LICENSE")

zip_path = OUT / zip_name
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as arc:
    for name in paths:
        info = zipfile.ZipInfo(name, date_time=(2026, 11, 19, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = (0o100644 << 16)
        arc.writestr(info, (ROOT / name).read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

with zipfile.ZipFile(zip_path) as arc:
    if arc.testzip() is not None or arc.namelist() != paths:
        raise SystemExit("Distribution ZIP integrity or file list check failed")
    if arc.read("main.tex") != (ROOT / "main.tex").read_bytes():
        raise SystemExit("The ZIP's main.tex differs from the current manuscript")
    if arc.read("LICENSE") != (OUT / "LICENSE").read_bytes():
        raise SystemExit("Bundled LICENSE does not match the standalone LICENSE")

print(f"OK: v{version} release files generated")
print(f"  PDF: {pdf_name} ({(OUT / pdf_name).stat().st_size} bytes)")
print(f"  ZIP: {zip_name} ({zip_path.stat().st_size} bytes; {len(paths)} source files)")
print("  ZIP contains: " + ", ".join(paths))
print("  Figure SHA-256 hashes match the preserved original release")
