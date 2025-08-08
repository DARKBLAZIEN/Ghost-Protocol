# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['poltergeist.py'],
    pathex=[],
    binaries=[],
    datas=[('1.mp4', '.'), ('3.mp4', '.'), ('5.mp4', '.'), ('7.mp4', '.'), ('8.mp4', '.'), ('9.mp4', '.'), ('10.mp4', '.'), ('11.mp4', '.'), ('12.mp4', '.'), ('knock.wav', '.'), ('valak.mp4', '.'), ('whisper.wav', '.'), ('scream.wav', '.'), ('static.wav', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='poltergeist',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
