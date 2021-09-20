# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['bot.py','C:\\Users\\Administrator.DESKTOP-CC2UIIT\\Desktop\\Yomaki\\bot\\KARuli\\karuli\\plugins\\setu.py','C:\\Users\\Administrator.DESKTOP-CC2UIIT\\Desktop\\Yomaki\\bot\\KARuli\\karuli\\plugins\\word_bank\\util.py','C:\\Users\\Administrator.DESKTOP-CC2UIIT\\Desktop\\Yomaki\\bot\\KARuli\\karuli\\plugins\\word_bank\\data_source.py','C:\\Users\\Administrator.DESKTOP-CC2UIIT\\Desktop\\Yomaki\\bot\\KARuli\\karuli\\plugins\\word_bank\\__init__.py],
             pathex=['C:\\Users\\Administrator.DESKTOP-CC2UIIT\\Desktop\\Yomaki\\bot\\KARuli'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='bot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='bot')
