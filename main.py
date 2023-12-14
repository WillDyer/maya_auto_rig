import importlib
import joints_select as js
import parent_joints as pj

importlib.reload(js)
importlib.reload(pj)

js.get_joints()
js.duplicate_ik_fk_joints()
#js.ik_rename()
#js.fk_rename()

pj.unparent_joints()