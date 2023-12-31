import importlib

import config
import testui as ui
import modules_setup

importlib.reload(config)
importlib.reload(ui)
importlib.reload(modules_setup)

main_ui = ui.main()