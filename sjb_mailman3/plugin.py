from mailman.interfaces.plugin import IPlugin
from public import public
from zope.interface import implementer

@public
@implementer(IPlugin)
class SJBMM3Plugin:
    def pre_hook(self):
        pass
    
    def post_hook(self):
        pass

    @property
    def resource(self):
        return None
