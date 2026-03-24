from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(r'ImgFile', ImageFilesViews)
router.register(r'VideoFile', VideoFilesViews)
router.register(r'Files', FilesViews)

urlpatterns = router.urls



# ------ Refactorization -------->

# def routers(router_name, view):
#     router = DefaultRouter()
#     return router.register(rf'{router_name}', view)
    
    
# routers('ImgFile', ImageFilesViews)

# class Routerrs:
#     def __init__(self,  router, router_name, view):
#         self.router = router
#         self.router_name = router_name,
#         self.view = view
        
#     def create_router(self):
#         self.router = DefaultRouter()
#         return self.router.register(rf'{self.router_name}', self.view)
    
# routeerrs = Routerrs("router", "img_router", ImageFilesViews)
# urlpatterns = routeerrs.create_router.url